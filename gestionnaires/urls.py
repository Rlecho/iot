from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    
    # path('admin/', admin.site.urls),
    
    path('', views.index, name='index'),
    path('facturation', views.facturation, name='facturation'),
    path('user', views.user, name='user'),
    path('plainte', views.plainte, name='plainte'),
    path('rapport', views.rapport, name='rapport'),
    path('reglage', views.reglage, name='reglage'),
    path('connect', views.connect, name='connect'),
]
