from django.urls import path
from accounts.views import UsuarioCreateAPIView, UsuarioListAPIView

urlpatterns = [
    path('api/', UsuarioCreateAPIView.as_view()),
    path('api/listar/', UsuarioListAPIView.as_view()),
]