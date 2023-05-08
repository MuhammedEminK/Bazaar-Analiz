# Generated by Django 4.2.1 on 2023-05-06 18:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('analiz', '0005_alter_placeofsale_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placeofsale',
            name='products',
            field=models.ManyToManyField(limit_choices_to={'seller': models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)}, to='analiz.sell'),
        ),
    ]
