from typing import Any
from django.db import models
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.cache import never_cache
# Create your views here.
# @login_required(login_url='/accounts/login')
class IndexView(LoginRequiredMixin, ListView):
    template_name = 'home.html'
    
    def get_queryset(self):
        pass