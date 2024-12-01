from django.apps import AppConfig
from transformers import pipeline


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    pipe = pipeline("text-classification", model="HooshvareLab/bert-fa-base-uncased-sentiment-digikala")
