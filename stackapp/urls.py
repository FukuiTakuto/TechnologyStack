from django.urls import path,include
from .views import ImgView

urlpatterns = [
    path('img/',ImgView.as_view()),
]
