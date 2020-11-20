"""Turismo_Joinville URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user),
    path('cadastro/', views.cadastro),
    path('cadastro/submit', views.submit_cadastro),
    path('about/', views.about_us),
    path('photos/', views.photos),
    path('parceiros/', views.parceiros),
    path('team/', views.team),
    path('contact/', views.contact),
    path('contact/submit', views.submit_contact),
    path('eventos/', views.eventos),
    path('moinho/', views.moinho),
    path('moinho/submit', views.submit_comentario),
    path('serra/', views.serra),
    path('serra/submit', views.submit_comentario),
    path('rpalmeiras/', views.rpalmeiras),
    path('rpalmeiras/submit', views.submit_comentario),
    path('estradabonita/', views.estradabonita),
    path('estradabonita/submit', views.submit_comentario),
    path('mercado/', views.mercado),
    path('mercado/submit', views.submit_comentario),
    path('mirante/', views.mirante),
    path('mirante/submit', views.submit_comentario),
    path('morrofinder/', views.morrofinder),
    path('morrofinder/submit', views.submit_comentario),
    path('castelobugres/', views.castelobugres),
    path('castelobugres/submit', views.submit_comentario),
    path('parquemar/', views.parquemar),
    path('parquemar/submit', views.submit_comentario),
    path('zoobotanico/', views.zoobotanico),
    path('zoobotanico/submit', views.submit_comentario),
    path('estacao/', views.estacao),
    path('estacao/submit', views.submit_comentario)
    #path('polls/', include('polls.urls')),
]