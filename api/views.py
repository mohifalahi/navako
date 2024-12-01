from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .apps import ApiConfig


class HealthCheckAPIView(APIView):
    """A view to check the api application being up and running"""
    def get(self, request):
        if request.method == 'GET':
            try:
                return JsonResponse({"status": "ok"}, status=status.HTTP_200_OK)
            except Exception as e:
                return JsonResponse({"status": "error", "message": str(e)}, status=500)
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class PredictAPIView(APIView):
    """A view to get a text and predict the positive or negative emotions according the Persian Bert model"""
    def post(self, request):
        if request.method == 'POST':
            text =  request.data.get('text')
            results = ApiConfig.pipe.predict(text)
            return Response(results, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        
