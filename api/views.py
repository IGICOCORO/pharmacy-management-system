from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import *
from .models import *

    
class StaffViewset(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication)
    permission_classes = [IsAuthenticated]
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

class ClientViewset(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ProductViewset(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication)
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class PurchaseViewset(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication)
    permission_classes = [IsAuthenticated]
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

class SaleViewset(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication)
    permission_classes = [IsAuthenticated]
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer


class CommandeViewset(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication)
    permission_classes = [IsAuthenticated]
    queryset = Commande.objects.all()
    serializer_class = CommandeSerializer

        
class PaiementViewset(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication)
    permission_classes = [IsAuthenticated]
    queryset = Paiement.objects.all()
    serializer_class = PaiementSerializer