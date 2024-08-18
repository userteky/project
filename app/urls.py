from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='home'),
   path('blog/', views.blog, name='blog'),
   path('contact/', views.contact, name='contact'),
]
