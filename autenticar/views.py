# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.shortcuts import (
    render,
    get_object_or_404,
    redirect
)
from django.http import HttpResponse
from django.views import View
from .forms import FormRegistro
# Create your views here.

class RegisterView(View):

    def post(self, request):
        form = FormRegistro(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
        return redirect('/')

class LoginView(View):

    def post(self, request):
        username = request.POST.get('usuario', None)
        password = request.POST.get('password', None)
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('servicios:dashboard')

    def get(self, request):
        return HttpResponse('peticion get')
