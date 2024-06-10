from django.shortcuts import render
from django.views.generic import ListView
from .models import ImgModel

# Create your views here.
class ImgView(ListView):
    model=ImgModel
    template_name='img.html'