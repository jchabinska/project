# Generated by Django 5.1.1 on 2025-01-28 03:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Journal_app', '0007_person_remove_osoba_data_dodania_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='osoba',
            options={'ordering': ['nazwisko'], 'permissions': [('can_view_other_persons', 'Can view other persons')]},
        ),
        migrations.AlterField(
            model_name='osoba',
            name='właściciel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='osoby', to=settings.AUTH_USER_MODEL),
        ),
    ]
