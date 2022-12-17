from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    #class Meta:
        #app_label ='Categoria'

    def __str__(self):
        return self.nombre 
    
class Noticia(models.Model):
    titulo = models.CharField(max_length=50, null=False)
    subtitulo = models.CharField(max_length=100, null=True,blank=True)
    fecha = models.TimeField(auto_now_add=True)
    texto = models.TextField(null=False)
    activo = models.BooleanField(default=True)
    Categoria = models.ForeignKey(Categoria,on_delete=models.SET_NULL,null=True)
    imagen = models.ImageField(null=True,blank=True,upload_to='noticia',default='noticia/default.png')  
    publicado = models.DateField(default=timezone.now)
    class Meta:
        ordering = ('-publicado',)
        #app_label = 'Noticia'

    def __str__(self):
        return self.titulo

    def delete(self, using = None, keep_parents = False):
        self.imagen.delete(self.image.name)
        super().delete()

class User(AbstractUser):
    rol_admin = models.BooleanField(default=False)
    rol_estado_activo = models.BooleanField(default=False)

    class Meta:
        db_table="auth_user"

    def __str__(self):
        return self.username

class Comentario(models.Model):
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    noticia = models.ForeignKey(Noticia,on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_hora = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.usuario.username