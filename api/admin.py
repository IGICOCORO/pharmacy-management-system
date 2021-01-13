from django.contrib import admin
from .models import *


class StaffAdmin(admin.ModelAdmin):
    list_display = "user", "tel"
    list_filter = "user", "tel"
    search_field = "user", "tel"
    ordering = "user", "tel"

    select_related = True

class ClientAdmin(admin.ModelAdmin):
    list_display = "nom", "tel"
    list_filter = "nom", "tel"
    search_field = "nom", "tel"
    ordering = "nom", "tel"


class ProductAdmin(admin.ModelAdmin):
    list_display = "nom", "unite", "unite_sortant", "rapport", "quantite", "prix_vente"
    list_filter = "nom", "unite", "unite_sortant", "rapport", "quantite", "prix_vente"
    search_field = "nom", "unite", "unite_sortant", "rapport", "quantite", "prix_vente"
    ordering = "nom", "unite", "unite_sortant", "rapport", "quantite", "prix_vente"

class PurchaseAdmin(admin.ModelAdmin):
    list_display = "produit", "quantite", "date", "personnel"
    list_filter = "produit", "quantite", "date", "personnel"
    search_field = "quantite", "date", "personnel", "details"
    ordering = "quantite", "date", "personnel", "details"


class SaleAdmin(admin.ModelAdmin):
    list_display = "produit", "quantite", "commande", "prix", "total"
    list_filter = "produit", "quantite", "commande",
    search_field = "produit", "quantite", "commande",
    ordering = "produit", "quantite", "commande",


class CommandeAdmin(admin.ModelAdmin):
    list_display = "personnel", "client", "date", "a_payer", "payee", "reste"
    list_filter = "personnel", "client", "date", "a_payer", "payee", "reste"
    search_field = "personnel", "client", "date", "a_payer", "payee", "reste"
    ordering = "personnel", "client", "date", "a_payer", "payee", "reste"
    select_related = True

class PaiementAdmin(admin.ModelAdmin):
    list_display = "commande", "somme", "date"
    list_filter = "commande", "somme", "date"
    search_field = "commande", "somme", "date"
    ordering = "commande", "somme", "date"
    select_related = True


admin.site.register(Staff, StaffAdmin)
admin.site.register(Product, ProduitAdmin)
admin.site.register(Client , ClientAdmin)
admin.site.register(Sale , SaleAdmin)
admin.site.register(Commande ,CommandeAdmin)
admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(Paiement,  PaiementAdmin)
