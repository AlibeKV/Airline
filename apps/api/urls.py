from django.urls import path, include

from .views import ArplanAPIView , AiplaneDetailAPIView , PlaneAPIView , PlaneDetailAPIView

urlpatterns = [
    path('Air/',ArplanAPIView.as_view()),
    path('Air/<int:pk>',AiplaneDetailAPIView.as_view()),
    path('Plane/',PlaneAPIView.as_view()),
    path('Plane/<int:pk>',PlaneDetailAPIView.as_view())
]