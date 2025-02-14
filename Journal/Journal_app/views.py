from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Osoba, Stanowisko, Person, Team
from .serializers import OsobaSerializer, StanowiskoSerializer, PersonSerializer, TeamSerializer
from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse, JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
import datetime
from rest_framework.generics import UpdateAPIView, DestroyAPIView, ListAPIView
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import permission_required
from django.views import View
from django.contrib.auth.models import User
from Journal_app.models import Osoba, Stanowisko
from .permissions import CustomDjangoModelPermissions

class OsobaList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        osoby = Osoba.objects.filter(właściciel=request.user)
        serializer = OsobaSerializer(osoby, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OsobaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(właściciel=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OsobaView(APIView):
    permission_classes = [DjangoModelPermissions]

    def get(self, request):
        return Response({"message": "GET response"})

    def post(self, request):
        return Response({"message": "POST response"})

    def put(self, request):
        return Response({"message": "PUT response"})

    def delete(self, request):
        return Response({"message": "DELETE response"})

class OsobaDetail(APIView):
    def get(self, request, pk):
        try:
            osoba = Osoba.objects.get(pk=pk)
            serializer = OsobaSerializer(osoba)
            return Response(serializer.data)
        except Osoba.DoesNotExist:
            return Response({"error": "Osoba not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            osoba = Osoba.objects.get(pk=pk)
            serializer = OsobaSerializer(osoba, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Osoba.DoesNotExist:
            return Response({"error": "Osoba not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            osoba = Osoba.objects.get(pk=pk)
            osoba.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Osoba.DoesNotExist:
            return Response({"error": "Osoba not found"}, status=status.HTTP_404_NOT_FOUND)

class StanowiskoList(APIView):
    def get(self, request):
        stanowiska = Stanowisko.objects.all()
        serializer = StanowiskoSerializer(stanowiska, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StanowiskoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StanowiskoDetail(APIView):
    def get(self, request, pk):
        try:
            stanowisko = Stanowisko.objects.get(pk=pk)
            serializer = StanowiskoSerializer(stanowisko)
            return Response(serializer.data)
        except Stanowisko.DoesNotExist:
            return Response({"error": "Stanowisko not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            stanowisko = Stanowisko.objects.get(pk=pk)
            serializer = StanowiskoSerializer(stanowisko, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Stanowisko.DoesNotExist:
            return Response({"error": "Stanowisko not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            stanowisko = Stanowisko.objects.get(pk=pk)
            stanowisko.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Stanowisko.DoesNotExist:
            return Response({"error": "Stanowisko not found"}, status=status.HTTP_404_NOT_FOUND)

class StanowiskoMembersView(ListAPIView):
    serializer_class = OsobaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        stanowisko_id = self.kwargs['id']
        return Osoba.objects.filter(stanowisko_id=stanowisko_id)

def welcome_view(request):
    now = datetime.datetime.now()
    html = f"""
        <html><body>
        Witaj użytkowniku! </br>
        Aktualna data i czas na serwerze: {now}.
        </body></html>"""
    return HttpResponse(html)

@api_view(['GET'])
@authentication_classes([TokenAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def person_list(request):
    persons = Person.objects.all()
    serializer = PersonSerializer(persons, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def person_detail(request, pk):
    try:
        person = Person.objects.get(pk=pk)
        serializer = PersonSerializer(person)
        return Response(serializer.data)
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT', 'DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def person_update_delete(request, pk):
    try:
        person = Person.objects.get(pk=pk)
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "Hello, authenticated user!"})

class OsobaUpdateView(UpdateAPIView):
    queryset = Osoba.objects.all()
    serializer_class = OsobaSerializer
    permission_classes = [IsAuthenticated, CustomDjangoModelPermissions]

class OsobaDeleteView(DestroyAPIView):
    queryset = Osoba.objects.all()
    permission_classes = [IsAuthenticated]

def osoba_search(request, substring):
    persons = Person.objects.filter(name__icontains=substring)
    serializer = PersonSerializer(persons, many=True)
    return JsonResponse(serializer.data, safe=False)

def person_list_html(request):
    persons = Person.objects.all()
    return render(request, 'Journal_app/person/list.html', {'persons': persons})

def person_detail_html(request, id):
    person = get_object_or_404(Person, id=id)
    return render(request, 'Journal_app/person/detail.html', {'person': person})

def team_list_html(request):
    teams = Team.objects.all()
    return render(request, 'Journal_app/team_list.html', {'teams': teams})

def team_detail_html(request, id):
    team = get_object_or_404(Team, id=id)
    return render(request, 'Journal_app/team_detail.html', {'team': team})

@permission_required('ankiety.view_person')
def person_view(request, pk):
    try:
        person = Person.objects.get(pk=pk)
        return HttpResponse(f"Ten użytkownik nazywa się {person.name}")
    except Person.DoesNotExist:
        return HttpResponse(f"W bazie nie ma użytkownika o id={pk}.")
    
def create_osoba(request):
    
    user = User.objects.get(username='wer47')  

    stanowisko, created = Stanowisko.objects.get_or_create(nazwa='fotograf')  
    osoba = Osoba(
        imie='Jan',
        nazwisko='Kowalski',
        nazwa='JanKowalski',
        plec=1,
        stanowisko=stanowisko,
        właściciel=user
    )
    osoba.save()