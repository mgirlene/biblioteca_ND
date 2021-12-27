from django.urls import path
from livro import views

urlpatterns = [
    path('api/', views.LivrosListCreateAPIView.as_view()),
    path('api/<int:pk>/', views.LivrosRetrieveUpdateDestroyAPIView.as_view()),
]