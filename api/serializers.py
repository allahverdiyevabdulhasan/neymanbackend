from rest_framework import serializers
from .models import (
    Hero, HeroFeature, HeroAdvantage,
    Category,
    HomeAbout, HomeAboutFeature,
    WorkProcess, WorkProcessFeature,
    Partner
)

class HeroFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroFeature
        fields = ['title', 'desc']

class HeroAdvantageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroAdvantage
        fields = ['title', 'desc']

class HeroSerializer(serializers.ModelSerializer):
    features = HeroFeatureSerializer(many=True, read_only=True)
    advantages = HeroAdvantageSerializer(many=True, read_only=True)
    imageUrl = serializers.ImageField(source='image_url', read_only=True)

    class Meta:
        model = Hero
        fields = ['subtitle', 'title', 'description', 'features', 'imageUrl', 'advantages']

class CategorySerializer(serializers.ModelSerializer):
    metaTitle = serializers.CharField(source='meta_title')
    metaDescription = serializers.CharField(source='meta_description')
    metaKeywords = serializers.CharField(source='meta_keywords', allow_blank=True, required=False)

    class Meta:
        model = Category
        fields = ['title', 'description', 'metaTitle', 'metaDescription', 'metaKeywords']

class HomeAboutFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeAboutFeature
        fields = ['title', 'desc']

class HomeAboutSerializer(serializers.ModelSerializer):
    features = HomeAboutFeatureSerializer(many=True, read_only=True)
    highlightWord = serializers.CharField(source='highlight_word', allow_blank=True, required=False)
    mainWord = serializers.CharField(source='main_word', allow_blank=True, required=False)

    class Meta:
        model = HomeAbout
        fields = ['subtitle', 'title', 'highlightWord', 'mainWord', 'features']

class WorkProcessFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkProcessFeature
        fields = ['title', 'desc']

class WorkProcessSerializer(serializers.ModelSerializer):
    features = WorkProcessFeatureSerializer(many=True, read_only=True)

    class Meta:
        model = WorkProcess
        fields = ['title', 'description', 'duration', 'features']

class PartnerSerializer(serializers.ModelSerializer):
    imageUrl = serializers.ImageField(source='image_url', read_only=True)

    class Meta:
        model = Partner
        fields = ['title', 'subtitle', 'description', 'time', 'link', 'imageUrl']
