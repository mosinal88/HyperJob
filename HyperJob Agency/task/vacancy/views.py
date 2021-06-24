from django import forms
from django.shortcuts import render
from django.views import View
from .models import Vacancy
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect


# Create your views here.
class VacancyList(View):
    def get(self, request, *args, **kwargs):
        vacancy = Vacancy.objects.all()
        return render(
            request, 'vacancy/vacancyList.html', context={
                'vacancy': vacancy
            }
        )


class CreateVacancy(forms.Form):
    description = forms.CharField(max_length=1024)


class ViewCreateVacancy(View):
    def get(self, request):
        if User.is_active:
            if request.user.is_staff:
                print(request.user.is_staff)
                create_vacancy = CreateVacancy(request.POST)
                return render(request, 'vacancy\\createVacancy.html', context={'create_vacancy': create_vacancy})
            else:
                return HttpResponse(status=403)
        else:
            return HttpResponse(status=403)

    def post(self, request):
        if User.is_active:
            if request.user.is_staff:
                create_vacancy = CreateVacancy(request.POST)
                if create_vacancy.is_valid():
                    Vacancy.objects.create(author=request.user, description=create_vacancy.cleaned_data['description'])
                    return redirect('/home')
            else:
                return HttpResponse(status=403)
        else:
            return HttpResponse(status=403)
