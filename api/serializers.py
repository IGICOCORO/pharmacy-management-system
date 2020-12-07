from .models import *
from rest_framework import serializers


class ClientSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    def get_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"

    class Meta:
        model = Client
        fields = "__all__"


class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = "__all__"


class FournisseurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fournisseur
        fields = "__all__"


class CommandeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commande
        fields = "__all__"


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = "__all__"


class VenteSerializer(serializers.ModelSerializer):
    str_montant = serializers.SerializerMethodField()

    def get_str_montant(self, obj):
        return f"+{obj.montant}" if obj.montant > 0 else f"{obj.montant}"

    class Meta:
        model = Vente
        fields = "__all__"
