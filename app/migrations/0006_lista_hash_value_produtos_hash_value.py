# Generated by Django 5.2 on 2025-05-07 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_categoria_hash_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='lista',
            name='hash_value',
            field=models.CharField(blank=True, editable=False, max_length=64),
        ),
        migrations.AddField(
            model_name='produtos',
            name='hash_value',
            field=models.CharField(blank=True, editable=False, max_length=64),
        ),
    ]
