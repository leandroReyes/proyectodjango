from django.shortcuts import render
from main.models import PAnciano, PNinno, PJoven, Paciente
from django.http import JsonResponse
import random
import string

def randomNombre(largo=10):
    """Genera un nombre de paciente aleatorio"""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(largo))

def index(request):
    template_name = "index.html"
    context = {}
    return render(request, template_name, context)

def listar_riesgo(request):
    template_name = "listar_riesgo.html"
    context = {}
    return render(request, template_name, context)

def get_list(request):
    p = Paciente.objects.get(noHistoriaClinica = int(request.GET['n']))
    l,m = p.Listar_Pacientes_Mayor_Riesgo()

    return JsonResponse({'riesgos_altos': l, 'datos_paciente':m})

def load_data(request):
    from django.contrib.auth.models import User as auth_user

    u = auth_user(username='root')
    u.set_password('1234567890')
    u.is_superuser = True
    u.is_staff = True
    u.save()

    for i in range(1000):
        e = random.randint(1, 78)
        p = random.randint(30, 100)
        es = round(random.uniform(1, 2), 2)
        n = randomNombre()
        if e >= 1 and e <= 15:
            PNinno.objects.create(nombre=n, edad=e, peso=p, estatura=es)
        elif e >= 16 and e <= 40:
            is_fumador = bool(random.getrandbits(1))
            f = 0
            if is_fumador:
                f = random.randint(1,20)
            PJoven.objects.create(nombre=n, edad=e, fumador=is_fumador, noAñosFumando=f)
        else:
            PAnciano.objects.create(nombre=n, edad=e, tieneDieta=bool(random.getrandbits(1)))            

    return JsonResponse({'response':'ok'})
