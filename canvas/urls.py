"""canvas URL Configuration

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
import proc.views as v
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v.index),
    path('index/', v.index,name="index"),
    path('showLogin/', v.showLogin,name="showLogin"),
    path('setLoginOut/', v.setLoginOut,name="setLoginOut"),
    path('getLogin/', v.getLogin,name="getLogin"),
    path('getImport/', v.getImport,name="getImport"),
    path('setImport/', v.setImport,name="setImport"),
    path('getStudentsInfo/', v.getStudentsInfo,name="getStudentsInfo"),
    path('getRestPasswd/', v.getRestPasswd,name="getRestPasswd"),
    path('resetPasswd/', v.resetPasswd,name="resetPasswd"),
    path('getProfessorList/', v.getProfessorList,name="getProfessorList"),
    path('getHomeworkList/', v.getHomeworkList,name="getHomeworkList"),

    path('addHomework/', v.addHomework,name="addHomework"),
    path('setHomework/', v.setHomework,name="setHomework"),
    path('getExamList/', v.getExamList,name="getExamList"),
    path('setExam/', v.setExam,name="setExam"),
    path('addExam/', v.addExam,name="addExam"),










]
