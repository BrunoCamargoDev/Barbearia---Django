from django.urls import path
from . import views

urlpatterns = [
    path('', views.agendar, name='agendar'),
    path('agendamentos/', views.listar_agendamentos, name='listar_agendamentos'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]