from Journal_app.models import Osoba
print(Osoba.objects.all())

print(Osoba.objects.get(id=3))

print(Osoba.objects.filter(nazwisko__startswith='K'))

print(Osoba.objects.values_list('stanowisko', flat=True).distinct())

from Journal_app.models import Stanowisko
print(Stanowisko.objects.order_by('-nazwa'))

from Journal_app.models import Stanowisko
nowa_osoba = Osoba(imie="Jan", nazwisko="Kowalski", plec=1, stanowisko=Stanowisko.objects.first())
nowa_osoba.save()

