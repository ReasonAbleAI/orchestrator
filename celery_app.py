from celery import Celery
from dotenv import load_dotenv
import os

load_dotenv()

REDIS_URL = os.getenv("REDIS_URL")
ORCHESTRATOR_WEB_URL = os.getenv("ORCHESTRATOR_WEB_URL")

app = Celery('tasks', broker=REDIS_URL)
app.conf.update(
    CELERY_IMPORTS=("tasks",)
)
