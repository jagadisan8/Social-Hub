from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from socialapp import forms

# Create your views here.
class signup(CreateView):
    template_name = 'socialapp/signup.html'
    form_class = forms.UserForm
    success_url = reverse_lazy('socialapp:login')
