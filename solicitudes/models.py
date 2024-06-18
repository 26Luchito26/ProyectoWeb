from django.db import models
from autenticacion.models import Usuario_Registro

class Solicitudes_Epps(models.Model):
    id_solicitudEpps = models.AutoField(primary_key=True)
    nombreEpps = models.CharField(max_length=100, verbose_name='Nombre del EPP')
    fecha_realizarEP = models.DateField(verbose_name='Fecha de realización')
    descripcionEpps = models.CharField(max_length=300, verbose_name='Comentario Adicional - Especifique adecuadamente talla y tipo de vestimenta para todos los EPPs')
    estadoEpps = models.BooleanField(default=False, verbose_name='EPP verificado')
    tipo_materialEpps = models.CharField(max_length=300, choices=[('unitario', 'Unitario'), ('más de un elemento', 'Más de un elemento')], verbose_name='Tipo de material de Epps')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    id_usuario = models.ForeignKey(Usuario_Registro, on_delete=models.CASCADE)
    tipo_usuario = models.CharField(max_length=30, choices=Usuario_Registro.TIPO_USUARIO_CHOICES)

    class Meta:
        verbose_name = 'Solicitud de EPP'
        verbose_name_plural = 'Solicitudes de EPPs'

    def __str__(self):
        return self.nombreEpps

class Solicitudes_Retiro(models.Model):
    id_solicitudRetiro = models.AutoField(primary_key=True)
    nombre_retiro = models.CharField(max_length=100, verbose_name='Nombre del retiro')
    fecha_realizarR = models.DateField(verbose_name='Fecha de realización')
    descripcionRetiro = models.CharField(max_length=300, verbose_name='Comentario Adicional - Detalle correctamente los campos, como cantidad y descripción, es crucial para las solicitudes de retiro.')
    cantidadRetiro = models.IntegerField(verbose_name='Cantidad a retirar')
    estadoRetiro = models.BooleanField(default=False, verbose_name='Retiro verificado')
    tipo_materialRetiro = models.CharField(max_length=10, choices=[('fardo', 'Fardo'), ('kilo', 'Kilo')], verbose_name='Tipo de material de retiro')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    id_usuario = models.ForeignKey(Usuario_Registro, on_delete=models.CASCADE)
    tipo_usuario = models.CharField(max_length=30, choices=Usuario_Registro.TIPO_USUARIO_CHOICES)

    class Meta:
        verbose_name = 'Solicitud de retiro'
        verbose_name_plural = 'Solicitudes de retiros'

    def __str__(self):
        return self.nombre_retiro

class Solicitudes_Material(models.Model):
    id_solicitudMaterial = models.AutoField(primary_key=True)
    nombre_material = models.CharField(max_length=100, verbose_name='Nombre del material')
    tipo_material = models.CharField(max_length=10, choices=[('fardo', 'Fardo'), ('kilo', 'Kilo')], verbose_name='Tipo de material')
    fecha_realizarM = models.DateField(verbose_name='Fecha de realización')
    descripcionMaterial = models.CharField(max_length=300, verbose_name='Comentario Adicional - Detalle correctamente los campos, como cantidad y descripción, es crucial para las solicitudes de material')
    cantidadMaterial = models.FloatField(verbose_name='Cantidad del material')
    estadoMaterial = models.BooleanField(default=False, verbose_name='Material verificado')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    id_usuario = models.ForeignKey(Usuario_Registro, on_delete=models.CASCADE)
    tipo_usuario = models.CharField(max_length=30, choices=Usuario_Registro.TIPO_USUARIO_CHOICES)

    class Meta:
        verbose_name = 'Solicitud de material'
        verbose_name_plural = 'Solicitudes de materiales'

    def __str__(self):
        return self.nombre_material