from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register("client", ClientViewset)
router.register("produit", ProduitViewset)
router.register("fournisseur", FournisseurViewset)
router.register("Commande", CommandeViewset)
router.register("stock", StockViewset)
router.register("Vente", VenteViewset)
urlpatterns = [
    path("", include(router.urls)),
]
