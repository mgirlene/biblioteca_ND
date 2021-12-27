from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from livro.models import Livros
from livro.serializers import LivrosSerializer

class LivrosListCreateAPIView(ListCreateAPIView):
    '''Cadastrar e listar'''
    permission_classes = (IsAuthenticated,)
    queryset = Livros.objects.all()
    serializer_class = LivrosSerializer

class LivrosRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    '''Detalhar, editar e excluir'''
    permission_classes = (IsAuthenticated,)
    queryset = Livros.objects.all()
    serializer_class = LivrosSerializer
