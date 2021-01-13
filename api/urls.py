from django.urls import path, include
from rest_framework import routers
from .views import *
from . import views

router = routers.DefaultRouter()
router.register("staff", StaffViewset)
router.register("produit", ProduitViewset)
router.register("fournisseur", FournisseurViewset)
router.register("Commande", CommandeViewset)
router.register("Commande", CommandeViewset)
router.register("Detail_stock", DetailStockViewset)
router.register("Detail_stock", DetailStockViewset)
router.register("Paiement", PaiementViewset)
urlpatterns = [
    path("", include(router.urls)),
]
