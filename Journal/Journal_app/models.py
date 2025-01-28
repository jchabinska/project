from django.db import models
from datetime import date
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.utils.timezone import now

class Stanowisko(models.Model):
    nazwa = models.CharField(max_length=100, null=False, blank=False)
    opis = models.TextField(blank=True, null=True)  
    data_utworzenia = models.DateTimeField(default=now)
    data_modyfikacji = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nazwa

class Plec(models.IntegerChoices):
    KOBIETA = 1, 'Kobieta'
    MEZCZYZNA = 2, 'Mężczyzna'
    INNE = 3, 'Inne'

class Osoba(models.Model):
    imie = models.CharField(max_length=100, null=True)
    nazwisko = models.CharField(max_length=100, null=True)
    nazwa = models.CharField(max_length=255, default="")
    plec = models.IntegerField(choices=Plec.choices, null=False)
    stanowisko = models.ForeignKey("Stanowisko", on_delete=models.CASCADE)
    właściciel = models.ForeignKey(User, on_delete=models.CASCADE, related_name="osoby")
    data_utworzenia = models.DateTimeField(default=now)
    data_modyfikacji = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['nazwisko']
        permissions = [
            ("can_view_other_persons", "Can view other persons"),
        ]

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"

    def clean(self):
        if not self.nazwa.isalpha():
            raise ValidationError("Nazwa może zawierać tylko litery.")

class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    members = models.ManyToManyField(Person, related_name='teams')  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
