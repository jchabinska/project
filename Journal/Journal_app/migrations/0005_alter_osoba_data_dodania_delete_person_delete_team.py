# Generated by Django 5.1.1 on 2025-01-27 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Journal_app', '0004_alter_osoba_options_osoba_nazwa_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='osoba',
            name='data_dodania',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.DeleteModel(
            name='Team',
        ),
    ]
