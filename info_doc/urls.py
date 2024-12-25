from django.urls import path
from . import views

urlpatterns = [
    path('privacy/', views.privacy_policy, name='privacy'),
    path('terms/', views.terms_of_use, name='terms'),
    path('about/', views.about_us, name='about'),
    path('contact/', views.contact_us, name='contact'),
    
]