# Generated by Django 3.2 on 2022-08-14 12:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('favourites', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productfavourites',
            old_name='favcat',
            new_name='favourite_category',
        ),
        migrations.RenameField(
            model_name='productfavourites',
            old_name='favprod',
            new_name='favourite_product',
        ),
        migrations.RenameField(
            model_name='productfavourites',
            old_name='ordfreq',
            new_name='order_frequency',
        ),
        migrations.AddField(
            model_name='productfavourites',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
