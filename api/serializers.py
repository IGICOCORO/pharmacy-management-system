from rest_framework import serializers

from .models import *


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = "__all__"

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class PurchaseSerializer(serializers.ModelSerializer):
    produit_id = serializers.SerializerMethodField()

    def to_representation(self, obj):
        representation = super().to_representation(obj)
        representation['produit'] = str(obj.produit)
        representation['personnel'] = str(obj.personnel)
        return representation

    def get_produit_id(self, obj):
        return obj.produit.id

    class Meta:
        model = Purchase
        fields = "__all__"
        read_only_fields = "date", "personnel"

class SaleSerializer(serializers.ModelSerializer):
    commande_id = serializers.SerializerMethodField()
    produit_id = serializers.SerializerMethodField()

    def to_representation(self, obj):
        representation = super().to_representation(obj)
        representation['produit'] = str(obj.produit)
        representation['commande'] = str(obj.commande)
        return representation

    def get_produit_id(self, obj):
        return obj.produit.id

    def get_commande_id(self, obj):
        return obj.commande.id

    class Meta:
        model = Sale
        fields = '__all__'


class CommandeSerializer(serializers.ModelSerializer):
    personnel_id = serializers.SerializerMethodField()
    client_id = serializers.SerializerMethodField()
    personnel = serializers.ReadOnlyField()

    def to_representation(self, obj):
        representation = super().to_representation(obj)
        representation['personnel'] = str(obj.personnel)
        representation['client'] = str(obj.client)
        return representation

    def get_personnel_id(self, obj):
        return obj.personnel.id

    def get_client_id(self, obj):
        if(obj.client): return obj.client.id
        return None

    class Meta:
        model = Commande
        fields = "__all__"

class PaiementSerializer(serializers.ModelSerializer):
    commande_id = serializers.SerializerMethodField()

    def to_representation(self, obj):
        representation = super().to_representation(obj)
        representation['commande'] = str(obj.commande)
        return representation

    def get_commande_id(self, obj):
        return obj.commande.id

    class Meta:
        model = Paiement
        fields = "__all__"