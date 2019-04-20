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

    # def post(self, request):
    #     form = self.form_class(request.POST or None, request.FILES)
    #
    #     print(form)
    #
    #     return render(request, 'home.html', {'form': form})
    def post(self, request):
        if request.method == 'POST':
            form = self.form_class(request.POST)
            form_i = self.form_class(request.FILES)
            # print(form_i.data)
            print(form_i)
            #print(form_i.is_valid())
            #print(form_image.data)
            print(form_i.is_valid())
            if form.is_valid():
                new_user = form.save()
                messages.info(request, "Thanks for registering. You are now logged in.")
                new_user = authenticate(email=form.cleaned_data['email'],
                                        password=form.cleaned_data['password1'],
                                        )
                login(request, new_user)
                return HttpResponseRedirect('/home')
        else:
            form = self.form_class()
            url = reverse('/registration', kwargs={'error_messages': form})
        return HttpResponseRedirect(url)


