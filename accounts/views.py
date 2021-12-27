
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from accounts.models import Usuario
from accounts.serializers import UsuarioSerializer

class UsuarioCreateAPIView(CreateAPIView):
    '''Cadastrar'''
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioListAPIView(ListAPIView):
    '''Listar'''
    permission_classes = (IsAuthenticated,)
    serializer_class = UsuarioSerializer

    def get_queryset(self):
        return Usuario.objects.filter(email=self.request.user.email)
