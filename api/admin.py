from django.contrib import admin
from .models import (
    Hero, HeroFeature, HeroAdvantage,
    Category,
    HomeAbout, HomeAboutFeature,
    WorkProcess, WorkProcessFeature,
    Partner
)

class HeroFeatureInline(admin.TabularInline):
    model = HeroFeature
    extra = 1

class HeroAdvantageInline(admin.TabularInline):
    model = HeroAdvantage
    extra = 1

@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    inlines = [HeroFeatureInline, HeroAdvantageInline]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

class HomeAboutFeatureInline(admin.TabularInline):
    model = HomeAboutFeature
    extra = 1

@admin.register(HomeAbout)
class HomeAboutAdmin(admin.ModelAdmin):
    inlines = [HomeAboutFeatureInline]

class WorkProcessFeatureInline(admin.TabularInline):
    model = WorkProcessFeature
    extra = 1

@admin.register(WorkProcess)
class WorkProcessAdmin(admin.ModelAdmin):
    inlines = [WorkProcessFeatureInline]

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    pass
