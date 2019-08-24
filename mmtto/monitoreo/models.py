from django.db import models
import datetime


class monitoreo(models.Model):
    servicio = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    serie = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    inventario = models.CharField(max_length=100)
    justificacion = models.CharField(max_length=255)
    fecha = models.DateField(default=datetime.date.today)
    tecnico1 = models.CharField(max_length=255)
    tecnico2 = models.CharField(max_length=255)
    responsable = models.CharField(max_length=255)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta1 = models.CharField(max_length=2,choices=SI_NO, default='SI')
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta2 = models.CharField(max_length=2,choices=SI_NO, default='SI')
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta3 = models.CharField(max_length=2,choices=SI_NO, default='SI')
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta4 = models.CharField(max_length=2,choices=SI_NO, default='SI')
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta5 = models.CharField(max_length=2,choices=SI_NO, default='SI')
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta6 = models.CharField(max_length=2,choices=SI_NO, default='SI')
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta7 = models.CharField(max_length=2,choices=SI_NO, default='SI')
  
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta8 = models.CharField(max_length=2,choices=SI_NO, default='SI')
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta9 = models.CharField(max_length=2,choices=SI_NO, default='SI')
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta10 = models.CharField(max_length=2,choices=SI_NO, default='SI')
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta11 = models.CharField(max_length=2,choices=SI_NO, default='SI')
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta12 = models.CharField(max_length=2,choices=SI_NO, default='SI')
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta13 = models.CharField(max_length=2,choices=SI_NO, default='SI')
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta14 = models.CharField(max_length=2,choices=SI_NO, default='SI')
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta15 = models.CharField(max_length=2,choices=SI_NO, default='SI')

    def __str__ (self):
        return "{0} ({1})".format(self.servicio, self.inventario )
