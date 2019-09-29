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
    pauta1 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta2 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta3 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta4 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta5 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta6 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta7 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta8 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta9 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta10 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta11 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta12 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta13 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta14 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta15 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta16 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta17 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta18 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta19 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta20 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta21 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta22 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta23 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta24 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta25 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta26 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta27 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta28 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta29 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta30 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta31 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta32 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta33 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta34 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta35 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta36 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta37 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta38 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta39 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta40 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta41 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta42 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta43 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta44 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta45 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta46 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta47 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta48 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta49 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta50 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta51 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta52 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta53 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta54 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta55 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta56 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta57 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta58 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta59 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta60 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name='Pautas de Mantenimiento'

    def __str__ (self):
        return "{0} ({1})".format(self.servicio, self.inventario )
