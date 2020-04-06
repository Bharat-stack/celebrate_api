"""letsplay URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from celebrate_api.views import (
    create_user_01, 
    get_user_01,
    get_token,
    get_decoded_token,
    send_otp_01
)



""" from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
) """


urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'status/api/signup01/', create_user_01),
    path(r'status/api/login01/', get_user_01),
    path(r'status/api/gettoken/', get_token),
    path(r'status/api/getdecodedtoken/', get_decoded_token),
    path(r'status/api/sendotp01/', send_otp_01),

]



