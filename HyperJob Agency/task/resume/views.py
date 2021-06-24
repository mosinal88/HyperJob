from django import forms
from django.shortcuts import render
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.shortcuts import redirect
from .models import Resume


# Create your views here.
menus = [
    {
        "name": "Login",
        "href": "/login"
    },
    {
        "name": "Sign up",
        "href": "/signup"
    },
    {
        "name": "Vacancy",
        "href": "/vacancies"
    },
    {
        "name": "Resume",
        "href": "/resumes"
    },
    {
        "name": "Personal",
        "href": "/home"
    }
]


class ResumeMainMenu(View):
    def get(self, request, *args, **kwargs):
        return render(
            request, 'resume\\mainmenu.html', context={
                'menus': menus
            }
        )


class ResumeList(View):
    def get(self, request, *args, **kwargs):
        resume = Resume.objects.all()
        return render(
            request, 'resume\\resumeList.html', context={
                'resume': resume
            }
        )


class MySignupView(CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'resume\\signup.html'


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'resume\\login.html'


class CreateResume(forms.Form):
    description = forms.CharField(max_length=1024)


class Home(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect('/resume/new')
        else:
            return redirect('/vacancy/new')


class ViewCreateResume(View):
    def get(self, request):
        if User.is_active:
            if not request.user.is_staff:
                create_resume = CreateResume(request.POST)
                return render(request, 'resume\\CreateResume.html',
                              context={'create_resume': create_resume})
            else:
                return HttpResponse(status=403)
        else:
            return HttpResponse(status=403)

    def post(self, request):
        resume = Resume(author=request.user, description=request.POST.get('description'))
        resume.save()
        return redirect('/home')
