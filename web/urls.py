"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
import blog.views as bv
import phystunion.views as pv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Hello/',bv.hello),
    path('manage/<str:function>',pv.Manage),
    path('init/',pv.Begin),
    path('Home/',pv.Home),
    path('NewsList/',pv.NewsList),
    path('ActivityList/',pv.ActivityList),
    path('ResourceList/',pv.ResourceList),
    path('News/<str:news>',pv.News),
    path('activity/<str:activity>',pv.Activity),
    path('section/<str:section>',pv.Section),
    path('Download/<str:filename>',pv.DownloadFile),
    path('mail/<str:subject>/<str:name>/<str:phone>/<str:email>/<str:studentid>/<str:tomail>',pv.Mail)

]
