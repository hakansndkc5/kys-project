from django.urls import path
from . import views
from .views import login_view

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', login_view, name='login'),


]