from rest_framework import viewsets
from imagens.models import ImagensHistorico
from imagens.api.serializers import ImagensHistoricoSerializer

class ImagensHistoricoViewset(viewsets.ModelViewSet):
    queryset = ImagensHistorico.objects.all()
    serializer_class = ImagensHistoricoSerializer