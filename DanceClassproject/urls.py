"""DanceClassproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from danceapp.views import *

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('dashboard/', dashboard, name="dashboard"),
    path('index_class/', index_class, name="index_class"),
    path('index_team/', index_team, name="index_team"),
    path('admin_login/', admin_login, name="admin_login"),
    path('logout_admin/', logout_admin, name="logout_admin"),
    path('admin_change_password/', admin_change_password, name="admin_change_password"),
    path('registration/', registration, name="registration"),
    path('add_class/', add_class, name="add_class"),
    path('edit_class/<int:pid>', add_class, name="edit_class"),
    path('view_class/', view_class, name="view_class"),
    path('delete_class/<int:pid>', delete_class, name="delete_class"),
    path('add_teacher/', add_teacher, name="add_teacher"),
    path('edit_teacher/<int:pid>', add_teacher, name="edit_teacher"),
    path('view_teacher/', view_teacher, name="view_teacher"),
    path('delete_teacher/<int:pid>', delete_teacher, name="delete_teacher"),
    path('about/', about, name="about"),
    path('index_about/', index_about, name="index_about"),
    path('contact/', contact, name="contact"),
    path('index_contact/', index_contact, name="index_contact"),
    path('registrationlist/', registrationlist, name="registrationlist"),
    path('delete_registration/<int:pid>', delete_registration, name="delete_registration"),
    path('registration_detail/<int:pid>', registration_detail, name="registration_detail"),
    path('admin_report/', admin_report, name="admin_report"),
    path('invoice/', invoice, name="invoice"),
    path('invoice_detail/<int:pid>', invoice_detail, name="invoice_detail"),
    path('search_registration/', search_registration, name="search_registration"),
    path('search_invoice/', search_invoice, name="search_invoice"),
    path('report/', report, name="report"),



]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
