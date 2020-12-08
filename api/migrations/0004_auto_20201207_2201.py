# Generated by Django 3.1 on 2020-12-08 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20201207_2154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paiement',
            name='commande',
        ),
        migrations.RemoveField(
            model_name='produit',
            name='rapport',
        ),
        migrations.AddField(
            model_name='paiement',
            name='produit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.produit'),
        ),
    ]
