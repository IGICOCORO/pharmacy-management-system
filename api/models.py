from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from datetime import datetime, timedelta, date


class staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tel = models.CharField(max_length=25)

    class Meta:
        unique_together = ('tel', 'user')

    def __str__(self):
        return self.user.username


class Client(models.Model):
    nom = models.CharField(max_length=30)
    tel = models.CharField(max_length=25, unique=True)

    class Meta:
        unique_together = ('nom', 'tel')

    def __str__(self):
        return f"{self.nom} {self.tel}"

class Product(models.Model):
    nom = models.CharField(max_length=60, unique=True)
    unite = models.CharField(max_length=60)
    unite_sortant = models.CharField(max_length=60)
    rapport = models.FloatField(default=1)
    quantite = models.FloatField(editable=False, default=0)
    prix_vente = models.FloatField(default=0)

    def __str__(self):
        return f"{self.nom}"

    class Meta:
        ordering = "nom",

class Purchase(models.Model):
    produit = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantite = models.FloatField()
    date = models.DateTimeField(blank=True, default=timezone.now)
    staff = models.ForeignKey(Staff, default=1, on_delete=models.PROTECT)
    details = models.TextField(blank=True, null=True)
    prix_achat = models.FloatField()

    def __str__(self):
        return f"{self.produit.nom} par {self.staff.user.username}"

    def save(self, *args, **kwargs):
        produit = self.produit
        produit.quantite += self.quantite
        produit.save()
        super(Purchase, self).save(*args, **kwargs)

    class Meta:
        ordering = ["produit"]

    def delete(self):
        produit = self.produit
        produit.quantite -= self.quantite
        if(produit.quantite<0):
            raise Exception("le stock ne peut pas tomber dans le manquant")
        super(Vente, self).delete()
        commande.save()
        produit.save()

class Sale(models.Model):
    produit = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantite = models.FloatField()
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    details = models.TextField(blank=True, null=True)
    prix = models.FloatField(editable=False, default=0)
    total = models.FloatField(editable=False, default=0)

    def save(self, *args, **kwargs):
        self.prix = self.produit.prix_vente
        self.total = self.quantite*self.prix
        
        if(not self.pk):
            self.updateThings()
        else:
            raise Exception("Edition Desactivée")

        if(self.produit.quantite < self.quantite):
            raise Exception("Cette quantite n'est pas disponible en Stock")
            
        super(Sale, self).save(*args, **kwargs)

    def updateThings(self):
        produit = self.produit
        produit.quantite -= self.quantite
        produit.save()

        commande = self.commande
        commande.a_payer += self.total
        commande.save()

    def editThings(self):
        produit = self.produit
        produit.quantite = produit.quantite + self.old_quantite - self.quantite
        produit.save()

        commande = self.commande
        old_somme = self.old_quantite*produit.prix_vente
        commande.a_payer = commande.a_payer + self.total - old_somme
        commande.save()
    
    def delete(self):
        produit = self.produit
        produit.quantite += self.quantite

        commande = self.commande
        commande.payee -= self.quantite*self.produit.prix_vente

        super(Sale, self).delete()
        commande.save()
        produit.save()

    class Meta:
        ordering = ["produit"]

class Commande(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.PROTECT)
    client = models.ForeignKey(Client, blank=True, null=True, on_delete=models.SET_NULL)
    date = models.DateTimeField(blank=True, default=timezone.now)
    a_payer = models.PositiveIntegerField(default=0, editable=False, blank=True)
    payee = models.PositiveIntegerField(default=0, editable=False, blank=True)
    reste = models.PositiveIntegerField(default=0, editable=False, blank=True)
    uncommited = models.PositiveIntegerField(default=0, editable=False, blank=True)

    def __str__(self):
        return f"commande du {self.date} valant {self.a_payer}"

    def save(self, *args, **kwargs):
        self.a_payer = int(self.a_payer)
        self.payee = int(self.payee)

        if(int(self.a_payer) < self.payee):
            self.reste = 0
        else :
            self.reste = self.a_payer-self.payee
        super(Commande, self).save(*args, **kwargs)

    class Meta:
        ordering = "-pk",

class Paiement(models.Model):
    commande = models.ForeignKey(Commande, null=True, on_delete=models.SET_NULL)
    somme = models.PositiveIntegerField(verbose_name='somme payée', default=0)
    date = models.DateTimeField(editable=False, default=timezone.now)
    validated = models.BooleanField(default=False, editable=False)

    def save(self, *args, **kwargs):
        if self.pk:
            raise Exception("Les paiements ne sont pas editables")
        commande = self.commande
        commande.uncommited += self.somme
        commande.save()
        super(Paiement, self).save(*args, **kwargs)

    def validate(self, *args, **kwargs):
        commande = self.commande
        commande.payee += self.somme
        commande.uncommited -= self.somme
        self.validated = True
        super(Paiement, self).save(*args, **kwargs)
        commande.save()

    def delete(self):
        commande = self.commande
        commande.payee -= somme
        super(Paiement, self).delete()
        commande.save()