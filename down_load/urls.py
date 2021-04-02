from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('pre_down',views.pre_down,name='pre_down'),
]