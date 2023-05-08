# Generated by Django 4.2.1 on 2023-05-06 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analiz', '0007_alter_placeofsale_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='placeofsale',
            name='date',
        ),
        migrations.AddField(
            model_name='placeofsale',
            name='day',
            field=models.CharField(choices=[('Pazartesi', 'Pazartesi'), ('Salı', 'Salı'), ('Çarşamba', 'Çarşamba'), ('Perşembe', 'Perşembe'), ('Cuma', 'Cuma'), ('Cumartesi', 'Cumartesi'), ('Pazar', 'Pazar')], default=1, max_length=20),
            preserve_default=False,
        ),
    ]
