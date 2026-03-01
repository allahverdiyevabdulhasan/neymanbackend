from django.db import models

class Hero(models.Model):
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image_url = models.ImageField(upload_to='hero/')

    def __str__(self):
        return self.title

class HeroFeature(models.Model):
    hero = models.ForeignKey(Hero, related_name='features', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True, null=True)
    desc = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.hero.title} - Feature: {self.title}"

class HeroAdvantage(models.Model):
    hero = models.ForeignKey(Hero, related_name='advantages', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True, null=True)
    desc = models.TextField(blank=True, null=True)

class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    meta_title = models.CharField(max_length=255)
    meta_description = models.TextField()
    meta_keywords = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title

class HomeAbout(models.Model):
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255)
    highlight_word = models.CharField(max_length=255, blank=True, null=True)
    main_word = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title

class HomeAboutFeature(models.Model):
    home_about = models.ForeignKey(HomeAbout, related_name='features', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    desc = models.TextField()

class WorkProcess(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title

class WorkProcessFeature(models.Model):
    work_process = models.ForeignKey(WorkProcess, related_name='features', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True, null=True)
    desc = models.TextField(blank=True, null=True)

class Partner(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    time = models.CharField(max_length=255, blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    image_url = models.ImageField(upload_to='partners/', blank=True, null=True)

    def __str__(self):
        return self.title
