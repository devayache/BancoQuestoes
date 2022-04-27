from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tabela/', views.tabela, name='tabela'),
    path('cadastrar_questoes/', views.cadastrar_questoes, name='cadastrar_questoes'),
]
