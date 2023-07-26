from django.urls import path,include
from . import views

urlpatterns = [
    # index
    path('',views.index, name='index'),
    path('user_profile/',views.user_profile, name='user_profile'),
]