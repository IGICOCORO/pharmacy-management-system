from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

#from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import *
from .serializers import *


class ClientViewset(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ProduitViewset(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializer


class FournisseurViewset(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Fournisseur.objects.all()
    serializer_class = FournisseurSerializer


class CommandeViewset(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Commande.objects.all()
    serializer_class = CommandeSerializer


class StockViewset(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class VenteViewset(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Vente.objects.all()
    serializer_class = VenteSerializer

    @action(["GET"], False, r"myaccount", "myaccount")
    def venteInfo(self, request):
        queryset = Vente.objects.get(client=request.user.client)
        serializer = VenteSerializer(queryset, many=False)
        return Response(serializer.data)
