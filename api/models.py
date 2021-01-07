from django.db import models
from django.db.models import Sum
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import datetime, timedelta, date


class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    tel = models.CharField(max_length=20)

    def __str__(self):

        return f"{self.user.username}"


class Produit(models.Model):
    lot = models.CharField(max_length=30)
    nom_produit = models.CharField(max_length=50, unique=True)
    nom_generic = models.CharField(max_length=50, unique=True)
    prix = models.PositiveIntegerField()
    disponible = models.BooleanField(default=True)
    quantite = models.FloatField(default=0, editable=False)
    exp_date = models.DateField(editable=True, null=False)

    def __str__(self):
        return f'{self.nom_produit} {self.disponible} {self.lot}'

    class Meta:
        ordering = ["nom_produit", "prix"]


class Stock(models.Model):
    produit = models.ForeignKey(
        Produit, default=None, on_delete=models.CASCADE)
    quantite_initiale = models.FloatField(
        default=None, verbose_name='quantité initial')
    quantite_actuelle = models.FloatField(
        editable=False, default=None, verbose_name='quantité actuelle')
    date = models.DateField(blank=True, default=timezone.now)
    expiration = models.PositiveIntegerField(default=5, null=True, blank=True)
    expiration_date = models.DateField(editable=False, null=True)
    Staff = models.ForeignKey("Staff", null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.produit} {self.quantite_actuelle} {self.produit.unite} du {self.date}"

    def save(self, *args, **kwargs):
        if self.quantite_actuelle == None:
            self.quantite_actuelle = self.quantite_initiale
        if self.expiration:
            self.expiration_date = self.date+timedelta(days=self.expiration)
        super(Stock, self).save(*args, **kwargs)
        self.calculateProxy()

    def calculateProxy(self):
        somme = Stock.objects.filter(produit=self.produit,
                                     quantite_actuelle__gt=0)\
            .aggregate(somme=Sum('quantite_actuelle'))
        self.produit.quantite = somme['somme']
        self.produit.save()

    def somme(self):
        return self.quantite_initiale*self.produit.prix

    class Meta:
        ordering = ["produit"]


class DetailStock(models.Model):
    stock = models.ForeignKey("Stock", on_delete=models.CASCADE)
    quantite = models.FloatField()
    date = models.DateTimeField(blank=True, default=timezone.now)
    motif = models.CharField(max_length=50, blank=True, null=True)

    def save(self, *args, **kwargs):
        stock = self.stock
        stock.quantite_actuelle -= abs(self.quantite)
        stock.save()
        super(DetailStock, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.stock.produit} du {self.stock.date} -\
            {self.quantite} {self.stock.produit.unite}"


class Fournisseur(models.Model):
    nom = models.CharField(verbose_name='nom et prenom', max_length=50)
    adresse = models.CharField(max_length=60, null=True)
    tel = models.CharField(
        max_length=40, verbose_name='numero de télephone', null=True)

    def __str__(self):
        return f"{self.nom}"


class DetailCommande(models.Model):
    commande = models.ForeignKey(
        "Commande", null=True, on_delete=models.CASCADE, related_name='details')
    quantite = models.PositiveIntegerField(default=1)
    somme = models.PositiveIntegerField(
        editable=False, blank=True, verbose_name='à payer')
    date = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        self.somme = self.produit.prix()*self.quantite
        super(DetailCommande, self).save(*args, **kwargs)
        self.save()

    class Meta:
        ordering = ['date']

    def __str__(self):
        return f"{self.produit}"


class Commande(models.Model):
    tel = models.CharField(max_length=20, blank=True, default=0)
    date = models.DateField(blank=True, default=timezone.now)
    a_payer = models.FloatField(default=0, blank=True)
    payee = models.FloatField(default=0, blank=True)
    reste = models.FloatField(default=0, blank=True)

    def save(self, *args, **kwargs):
        self.reste = self.a_payer-self.payee
        super(Commande, self).save(*args, **kwargs)


class Paiement(models.Model):
    produit = models.ForeignKey(
        "Produit", null=True, on_delete=models.SET_NULL)
    somme = models.PositiveIntegerField(verbose_name='somme payée', default=0)
    date = models.DateField(blank=True, default=timezone.now)

    def save(self, *args, **kwargs):
        produit = self.produit
        super(Paiement, self).save(*args, **kwargs)
        paiements = Paiement.objects.filter(
            produit=produit).aggregate(Sum("somme"))["somme__sum"]
        produit.payee += self.somme
        commande.reste = produit.a_payer-paiements
        produit.save()
