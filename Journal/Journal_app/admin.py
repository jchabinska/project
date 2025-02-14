from django.contrib import admin
from .models import Osoba, Stanowisko


@admin.register(Stanowisko)
class StanowiskoAdmin(admin.ModelAdmin):
    list_display = ('nazwa', 'opis')

@admin.register(Osoba)
class OsobaAdmin(admin.ModelAdmin):
    list_display = ('imie', 'nazwisko', 'plec', 'stanowisko', 'data_utworzenia')
    list_filter = ('stanowisko', 'data_utworzenia')
    readonly_fields = ('data_utworzenia',)

    admin.display(description='Stanowisko (ID)')
    def stanowisko_z_id(self, obj):
       return f"{obj.stanowisko} ({obj.stanowisko.id})"
    

