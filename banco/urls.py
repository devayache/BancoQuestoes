from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tabela/', views.tabela, name='tabela'),
    path('cadastrarQuestoes/', views.cadastrarQuestoes, name='cadastrarQuestoes'),
]
