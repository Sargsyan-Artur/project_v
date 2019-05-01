from django.shortcuts import render


from django.views import generic
from .forms import UserCreationForm

from django.views.generic.edit import BaseCreateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


class Registration(generic.CreateView, BaseCreateView):
    form_class = UserCreationForm
    template_name = "register.html"
    success_url = "/home"

    def post(self, request):
        if request.method == 'POST':
            form = self.form_class(request.POST, request.FILES)

            if form.is_valid():
                new_user = form.save()
                messages.info(request, "Thanks for registering. You are now logged in.")
                new_user = authenticate(email=form.cleaned_data['email'],
                                        password=form.cleaned_data['password1'],
                                        )
                login(request, new_user)
                print('home')
                return HttpResponseRedirect('/home')
            else:

                return super(Registration, self).post(request)


