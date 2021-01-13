from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response



class StaffViewset(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer


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


class DetailCommandeViewset(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = DetailCommande.objects.all()
    serializer_class = DetailCommandeSerializer


class StockViewset(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class DetailStockViewset(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = DetailStock.objects.all()
    serializer_class = DetailStockSerializer


class PaiementViewset(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Paiement.objects.all()
    serializer_class = PaiementSerializer

    @action(["GET"], False)
    def PaiementInfo(self, request):
        queryset = Paiement.objects.get(client=request.user.client)
        serializer = PaiementSerializer(queryset, many=False)
        return Response(serializer.data)
