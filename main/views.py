from django.shortcuts import render
from main.models import PAnciano, PNinno, PJoven
from django.http import JsonResponse

def get_list(request):
    p = PAnciano.objects.get(noHistoriaClinica = 2)
    l = p.Listar_Pacientes_Mayor_Riesgo()

    return JsonResponse({'respuesta': l})
