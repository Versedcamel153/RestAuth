"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 3ce4b0e (FIxes)
from .views import *

urlpatterns = [
    path('google/', GoogleLogin.as_view(), name='google_login'),
    path('registration/', include('dj_rest_auth.registration.urls')),
    path('', include('dj_rest_auth.urls')),
<<<<<<< HEAD
=======
=======
from .views import GoogleLogin, CustomPasswordResetConfirmView, CustomPasswordResetView


urlpatterns = [
    path('google/', GoogleLogin.as_view(), name='rest_google_login'),
    path('registration/', include('dj_rest_auth.registration.urls')),
    path('', include('dj_rest_auth.urls')),
    path('password-reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password/reset/confirm/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
>>>>>>> 82b70b0 (Fixes)
>>>>>>> 3ce4b0e (FIxes)
]
