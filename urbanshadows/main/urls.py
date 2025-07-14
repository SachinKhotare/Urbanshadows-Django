from django.urls import path
from . import views

urlpatterns = [
    path('', views.solve_the_curse, name='home'),  # 👈 This makes "/" load your main page
    path('index/', views.solve_the_curse, name='index'),
]
