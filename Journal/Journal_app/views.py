from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Osoba, Stanowisko
from .serializers import OsobaSerializer, StanowiskoSerializer


class OsobaList(APIView):
    def get(self, request):
        osoby = Osoba.objects.all()
        serializer = OsobaSerializer(osoby, many=True)
        return Response(serializer.data)
    

    def post(self, request):
        serializer = OsobaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



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
        
       