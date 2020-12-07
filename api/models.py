from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Fournisseur(models.Model):
    nom = models.CharField(max_length=50)
    telephone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    adresse = models.CharField(max_length=200)

    class Meta:
        ordering = ["nom", ]

    def __str__(self):
        return f'{self.nom} {self.telephone} {self.email} {self.adresse}'


class Produit(models.Model):
    reference = models.CharField(unique=True, max_length=50)
    designation = models.CharField(max_length=50)
    prixU = models.DecimalField(max_digits=8, decimal_places=2)
    quantite = models.IntegerField()
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.reference} {self.designation} {self.quantite} {self.fournisseur}'


class Client(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    telephone = models.CharField(max_length=50)
    adresse = models.CharField(max_length=50)
    produits = models.ManyToManyField(Produit, through='Achat', blank=True)

    def __str__(self):
        return f'{self.nom} by {self.prenom}'


class Achat(models.Model):
    date_Achat = models.DateField(default=timezone.now)
    quantite = models.IntegerField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.date_Achat} by {self.quantite}'

    class Meta:
        ordering = ['date_Achat', ]
