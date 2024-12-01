from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .apps import ApiConfig


class HealthCheckAPIView(APIView):
    """A view to check the api application being up and running"""
    def get(self, request):
        try:
            return JsonResponse({"status": "ok"}, status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=500)


class PredictAPIView(APIView):
    """A view to get a text and predict the positive or negative emotions according the Persian Bert model"""
    def post(self, request):
        text =  request.data.get('text')
        results = ApiConfig.pipe.predict(text)
        return Response(results, status=status.HTTP_200_OK)
        
