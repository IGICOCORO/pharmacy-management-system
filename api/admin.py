from django.contrib import admin
from .models import *


class ClientAdmin(admin.ModelAdmin):
    list_display = "user", "phone"
    list_filter = "user", "phone"
    ordering = "user",


class ProduitAdmin(admin.ModelAdmin):
    list_display = "nom", "prix", "description", "qté"
    list_filter = "nom", "prix", "description", "qté"
    ordering = "nom", "prix", "description", "qté"


class CommandeAdmin(admin.ModelAdmin):
    list_display = "number", "description", "produit"
    list_filter = "number", "produit"
    ordering = "produit",


class StockAdmin(admin.ModelAdmin):
    list_display = "produits", "description"
    list_filter = "produits", "description"
    ordering = "produits",


class VenteAdmin(admin.ModelAdmin):
    list_display = "montant", "date", "produit"
    list_filter = "montant",  "date"
    ordering = "date",


admin.site.register(Client, ClientAdmin)
admin.site.register(Produit, ProduitAdmin)
admin.site.register(Fournisseur)
admin.site.register(Commande, CommandeAdmin)
admin.site.register(Stock, StockAdmin)
admin.site.register(Vente, VenteAdmin)
