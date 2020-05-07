"""Django_GetScore_Baitan_python URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from . import Gettoresult, Index, Main_get,Baitan_python


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^result$', Gettoresult.gettoresult),
    url(r'^index$', Index.index),
    url(r'^result$', Main_get.main_get),
    url(r'^baitan_python/index$', Baitan_python.index),
    url(r'^baitan_python/check$', Baitan_python.check),
]
