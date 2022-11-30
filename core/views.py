from django.contrib.auth.decorators import permission_required, login_required
from django.shortcuts import render
import csv
import io
from .models import Atendime
from django.http import JsonResponse, HttpResponseRedirect , HttpResponse
from django.contrib import messages



def index(request):
    atendimentos = Atendime.objects.all()

    context = {
        'curso': 'Programação Web com Django Framework',
        'atendimentos': atendimentos,
    }

    return render(request, 'index.html', context)

@login_required
def export_csv(request):
    atendimentos = Atendime.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="atendime.csv"'

    writer = csv.writer(response, delimiter=';')
    writer.writerow(['cd_atendimento','dt_atendimento','cd_convenio','cd_pro_int'])

    for obj in atendimentos:
        writer.writerow([obj.cd_atendimento, obj.dt_atendimento, obj.cd_convenio, obj.cd_pro_int])
    return response

def atendimento(request, pk):
    atend = Atendime.objects.get(cd_atendimento=pk)
    context = {
        'atendimento:': atend
               }
    return render(request, 'atendimento.html', context)
