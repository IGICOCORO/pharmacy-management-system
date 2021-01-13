from django.urls import path, include
from rest_framework import routers
from .views import *
from . import views

router = routers.DefaultRouter()
router.register("staff",StaffViewset)
router.register("client",ClientViewset)
router.register("produit",ProductViewset)
router.register("achat",PurchaseViewset)
router.register("vente",SaleViewset)
router.register("commande",CommandeViewset)
router.register("paiement",PaiementViewset)
urlpatterns = [
    path("", include(router.urls)),
]
