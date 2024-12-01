from django.urls import path

from . import views

urlpatterns = [
    path('health/', views.HealthCheckAPIView.as_view(), name='health-check'),
    path('predict/', views.PredictAPIView.as_view(), name='predict'),
]