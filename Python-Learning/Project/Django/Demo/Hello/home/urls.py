from django.contrib import admin
from django.urls import path
from home import views # <-- Addd the home with import views 
from django.conf import settings
from django.conf.urls.static import static
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

urlpatterns = [
    path('', views.index, name='home'),  # <-- If anyone comes with blank path, then redirect him to views.index with name='home'
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('contact', views.contact, name='contact'),

] 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=os.path.join(BASE_DIR, 'static'))
