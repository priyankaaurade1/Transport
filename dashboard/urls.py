from django.urls import path,include
from . import views

urlpatterns = [
    # index
    path('index/',views.index, name='index'),
    path('pages_error_404/',views.pages_error_404, name='pages_error_404'),
    path('pages_contact/',views.pages_contact, name='pages_contact'),
    path('user_profile/',views.user_profile, name='user_profile'),
    path('pages_faq/',views.pages_faq, name='pages_faq'),
]