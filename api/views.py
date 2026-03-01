from rest_framework import views, response, status
from .models import Hero, Category, HomeAbout, WorkProcess, Partner
from .serializers import (
    HeroSerializer, CategorySerializer, HomeAboutSerializer,
    WorkProcessSerializer, PartnerSerializer
)

class HeroAPIView(views.APIView):
    def get(self, request):
        hero = Hero.objects.first()
        if hero:
            serializer = HeroSerializer(hero, context={'request': request})
            return response.Response(serializer.data)
        return response.Response({}, status=status.HTTP_404_NOT_FOUND)

class CategoryAPIView(views.APIView):
    def get(self, request):
        category = Category.objects.first()
        if category:
            serializer = CategorySerializer(category)
            return response.Response(serializer.data)
        return response.Response({}, status=status.HTTP_404_NOT_FOUND)

class HomeAboutAPIView(views.APIView):
    def get(self, request):
        about = HomeAbout.objects.first()
        if about:
            serializer = HomeAboutSerializer(about)
            return response.Response(serializer.data)
        return response.Response({}, status=status.HTTP_404_NOT_FOUND)

class WorkProcessAPIView(views.APIView):
    def get(self, request):
        process = WorkProcess.objects.first()
        if process:
            serializer = WorkProcessSerializer(process)
            return response.Response(serializer.data)
        return response.Response({}, status=status.HTTP_404_NOT_FOUND)

class PartnerAPIView(views.APIView):
    def get(self, request):
        partner = Partner.objects.first()
        if partner:
            serializer = PartnerSerializer(partner, context={'request': request})
            return response.Response(serializer.data)
        return response.Response({}, status=status.HTTP_404_NOT_FOUND)
