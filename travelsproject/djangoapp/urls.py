from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    ]
    #path('about/', views.about, name='about'),
    #path('contact/', views.contact, name='contact'),
    #path('detail/', views.detail, name='detail'),
    #path('thanks/', views.thanks, name='thanks'),

#path('add/', views.operations, name='operations'),
    #path('sub/', views.operations, name='operations'),
    #path('mul/', views.operations, name='operations'),
    #path('div/', views.operations, name='operations'),
