# Generated by Django 4.2.1 on 2023-05-06 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analiz', '0006_alter_placeofsale_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placeofsale',
            name='products',
            field=models.ManyToManyField(to='analiz.sell'),
        ),
    ]