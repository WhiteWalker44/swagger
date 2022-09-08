from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.UserView.as_view(), name='user'),   
]