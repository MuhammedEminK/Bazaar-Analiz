# Generated by Django 4.2.1 on 2023-05-07 21:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('analiz', '0010_alter_revenue_ciro'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductProfit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profit', models.FloatField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analiz.product')),
            ],
        ),
        migrations.AddField(
            model_name='revenue',
            name='products',
            field=models.ManyToManyField(to='analiz.productprofit'),
        ),
    ]
