from django.urls import path
from accounts.views import UsuarioCreateAPIView, UsuarioListAPIView

urlpatterns = [
    path('cadastrar/', UsuarioCreateAPIView.as_view()),
    path('listar/', UsuarioListAPIView.as_view()),
]