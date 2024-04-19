from django.db import models

from django.db import models


class Usuario(models.Model):
    proyectos = models.ManyToManyField('Proyecto')
    nombre = models.CharField(max_length=64)
    hash_contraseña = models.CharField(max_length=128)
    correo = models.CharField(max_length=40)
    ultimo_ingreso = models.DateTimeField()
    es_administrador = models.BooleanField()
    es_financiero = models.BooleanField()
    es_director = models.BooleanField()
    es_contador = models.BooleanField()
    es_obra = models.BooleanField()

class Lote(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    descripcion = models.CharField(max_length=128)
    OPCIONES_ESTADO = [
        ('Aprobado', 'Aprobado'),
        ('Rechazado', 'Rechazado'),
        ('En proceso', 'En proceso'),
        ('Algunos reversos', 'Algunos reversos'),
        ('Devuelto', 'Devuelto')
    ]
    
    estado = models.CharField(max_length=20, choices=OPCIONES_ESTADO)
    libro_contable = models.FileField()
    formato = models.FileField()
    
class Proyecto(models.Model):
    usuarios = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    lote = models.ForeignKey(Lote, on_delete=models.DO_NOTHING)
    nombre = models.CharField(max_length=64)
    descripcion = models.CharField(max_length=128) 



class Pago(models.Model):
    lote = models.ForeignKey(Lote, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField()
    fecha_modificación = models.DateTimeField()
    desenglose = models.CharField(max_length=128)
    aprobado_contador = models.BooleanField()
    justificacion_contador = models.CharField(max_length=128)
    aprobado_director = models.BooleanField()
    justificacion_director = models.CharField(max_length=128)
    tipo = models.CharField(max_length=32)
    OPCIONES_ESTADO = [
        ('Pagado', 'Pagado'),
        ('Rechazado', 'Rechazado'),
        ('En proceso', 'En proceso'),
        ('Reversado', 'Reversado'),
        ('Saldo pendiente', 'Saldo pendiente'),
        ('Devuelto', 'Devuelto'),
        ('Pagado por socio', 'Pagado por socio')
    ]
    
    estado = models.CharField(max_length=20, choices=OPCIONES_ESTADO)
    beneficiario = models.CharField(max_length=64)
    monto = models.PositiveIntegerField()

class Proveedores(models.Model):
    tipo_documento = models.CharField(max_length=32)
    numero_documento = models.CharField(max_length=32)
    numero_cuenta = models.CharField(max_length=20)
    banco = models.CharField(max_length=30)
    tipo_transaccion = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=128)
    telefono = models.CharField(max_length=30)
    correo = models.CharField(max_length=40)

class Registro(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    fecha = models.DateTimeField()
    descripcion = models.CharField(max_length=128)

