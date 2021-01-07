from django.contrib import admin
from .models import *


class StaffAdmin(admin.ModelAdmin):
    list_display = "user", "tel"
    list_filter = "user", "tel"
    ordering = "user",


class ProduitAdmin(admin.ModelAdmin):
    list_display = "disponible", "lot"
    list_filter = "disponible",
    ordering = "quantite",


class DetailStockAdmin(admin.ModelAdmin):
    list_display = "quantite", "date", "motif"
    list_filter = "quantite", "date"
    ordering = "date",


class StockAdmin(admin.ModelAdmin):
    list_display = "quantite_initiale", "quantite_actuelle", "expiration_date"
    list_filter = "quantite_initiale", "quantite_actuelle", "expiration_date"
    ordering = "quantite_initiale",


class FournisseurAdmin(admin.ModelAdmin):
    list_display = "nom", "adresse", "tel"
    list_filter = "nom",  "adresse"
    ordering = "nom",


class DetailCommandeAdmin(admin.ModelAdmin):
    list_display = "quantite", "date", "somme"
    list_filter = "quantite",  "date"
    ordering = "date",


class PaiementAdmin(admin.ModelAdmin):
    list_display = "somme", "date"
    list_filter = "somme",  "date"
    ordering = "date",


admin.site.register(Staff, StaffAdmin)
admin.site.register(Produit, ProduitAdmin)
admin.site.register(Fournisseur)
admin.site.register(Commande)
admin.site.register(Stock, StockAdmin)
admin.site.register(DetailStock, DetailStockAdmin)
admin.site.register(DetailCommande, DetailCommandeAdmin)
admin.site.register(Paiement,  PaiementAdmin)
