from django.contrib import admin
from .models import Paciente, PAnciano, PJoven, PNinno, Consulta, TipoConsulta, Estado

# Register your models here.
#admin.site.register(Paciente)
admin.site.register(PAnciano)
admin.site.register(PJoven)
admin.site.register(PNinno)
admin.site.register(Consulta)
admin.site.register(TipoConsulta)
admin.site.register(Estado)