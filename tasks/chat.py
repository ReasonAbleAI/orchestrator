import requests
from celery_app import app
from src.query_classifier.query_classifier import QueryClassifier
from src.utils.load_settings import SEMANTIC_NETWORKS, ABILITIES, DESIRES

def process_incoming_message(message, agent):
    print(f'Processing incoming message from {agent}: "{message}"')
    print('Classifying message...')
    query_classification = QueryClassifier(message).classify()
    print(f'Classification results: {query_classification}')
    message = f"These are the results of the query classification: {query_classification}"
