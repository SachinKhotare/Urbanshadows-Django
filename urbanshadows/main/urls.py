from django.urls import path
from . import views

urlpatterns = [
    path('register_page/', views.contact_form, name='register_page'),
]
