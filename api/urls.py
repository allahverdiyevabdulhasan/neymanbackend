from django.urls import path
from .views import (
    HeroAPIView, CategoryAPIView, HomeAboutAPIView,
    WorkProcessAPIView, PartnerAPIView
)

urlpatterns = [
    path('hero', HeroAPIView.as_view(), name='hero'),
    path('categories', CategoryAPIView.as_view(), name='categories'),
    path('home-about', HomeAboutAPIView.as_view(), name='home-about'),
    path('work-process', WorkProcessAPIView.as_view(), name='work-process'),
    path('partners', PartnerAPIView.as_view(), name='partners'),
]
