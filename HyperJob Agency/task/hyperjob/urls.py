"""hyperjob URL Configuration

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
import site

from django.contrib import admin
from django.urls import path, include
from resume.views import ResumeMainMenu, ResumeList, MySignupView, MyLoginView, ViewCreateResume, Home
from vacancy.views import VacancyList, ViewCreateVacancy
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ResumeMainMenu.as_view()),
    path('resumes/', ResumeList.as_view()),
    path('vacancies/', VacancyList.as_view()),
    path('login/', RedirectView.as_view(url='/login')),
    path('signup/', RedirectView.as_view(url='/signup')),
    path('login', MyLoginView.as_view()),
    path('signup', MySignupView.as_view()),
    path('resume/new', ViewCreateResume.as_view()),
    path('vacancy/new', ViewCreateVacancy.as_view()),
    path('home/', Home.as_view())
]
