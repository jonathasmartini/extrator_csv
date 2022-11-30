from django.urls import path
from .views import index, atendimento, export_csv

urlpatterns = [
    path('', index, name='index'),
    path('atendimento/<int:pk>', atendimento, name='atendimento'),
    path('export_csv/', export_csv , name='export_csv'),
]