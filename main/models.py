from django.db import models

def get_prioridad(objeto):
        prioridad = 0
        print(objeto)
        if objeto.edad <= 5:
            prioridad = objeto.peso - objeto.estatura + 3
        elif objeto.edad > 5 and objeto.edad <= 12:
            prioridad = objeto.peso - objeto.estatura + 2
        elif objeto.edad > 12 and objeto.edad <= 15:
            prioridad = objeto.peso - objeto.estatura + 1
        elif objeto.edad >= 16 and objeto.edad < 41:
            if objeto.fumador:
                prioridad = (objeto.noAñosFumando / 4) + 2
            else:
                prioridad = 2
        elif objeto.edad >= 60 and objeto.edad <= 100 and objeto.tieneDieta:
            prioridad = (objeto.edad / 20) + 4
        else:
            prioridad = (objeto.edad / 30) + 3
        return prioridad

def get_riesgo(edad, prioridad):
    riesgo = 0
    if edad < 41:
        riesgo = (edad * prioridad) / 100
    else:
        riesgo = ((edad * prioridad) / 100) + 5.3
    return riesgo

class Paciente(models.Model):
    nombre = models.CharField(max_length=250)
    edad = models.IntegerField()
    noHistoriaClinica = models.AutoField(primary_key=True)

    def __str__(self):
        return self.nombre

    def Listar_Pacientes_Mayor_Riesgo(self):
        riesgo_usuario = get_riesgo(self.edad, get_prioridad(self))
        lista_riesgo = []
        if self.edad < 16:
            lista_riesgo = lista_riesgo + [get_riesgo(x.edad, get_prioridad(x)) for x in PNinno.objects.all().exclude(noHistoriaClinica=self.noHistoriaClinica)]
        elif self.edad > 15 and self.edad < 41:
            lista_riesgo = lista_riesgo + [get_riesgo(x.edad, get_prioridad(x)) for x in PJoven.objects.all().exclude(noHistoriaClinica=self.noHistoriaClinica)]
        else:
            lista_riesgo = lista_riesgo + [get_riesgo(x.edad, get_prioridad(x)) for x in PAnciano.objects.all().exclude(noHistoriaClinica=self.noHistoriaClinica)]
        
        return lista_riesgo

class PAnciano(Paciente):
    tieneDieta = models.BooleanField(default=False)

class PNinno(Paciente):
    peso = models.IntegerField()
    estatura = models.FloatField()

class PJoven(Paciente):
    fumador = models.BooleanField(default=False)
    noAñosFumando = models.IntegerField()

class TipoConsulta(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return "Tipo de Consulta: {}".format(self.nombre)

class Estado(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return "Estado: {}".format(self.nombre)

class Consulta(models.Model):
    id = models.IntegerField(primary_key=True)
    tipoConsulta = models.ForeignKey(TipoConsulta, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    cantPaciente = models.IntegerField(default=0)
    nombreEspecialista = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return "Consulta Numero: {}".format(self.id)
