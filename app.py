from flask import Flask, request, jsonify
from celery_app import app as celery_app
import tasks

app = Flask(__name__)


@app.route('/trigger_task', methods=['POST'])
def trigger_task():
    task_name = request.json.get('task_name')
    priority = request.json.get('priority', 'low')

    priority_map = {'low': 9, 'medium': 6, 'high': 3, 'urgent': 0}
    priority_value = priority_map.get(priority, 9)

    task = getattr(tasks, task_name, None)
    if task is None:
        return jsonify({'error': 'Invalid task name'}), 400

    result = task.apply_async(queue='your_queue', priority=priority_value)
    return jsonify({'task_id': str(result.id)}), 202


# This will eventually be replaced by the communicator service
@app.route('/message', methods=['POST'])
def send_message():
    message = request.form.get('message')
    agent = request.form.get('agent')
    print(f'Recieved message from {agent}: "{message}"')
    celery_app.send_task('process_incoming_message', kwargs={'message': message, 'agent': agent})
    return jsonify({})


if __name__ == '__main__':
    app.run(debug=True)
