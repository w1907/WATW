from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UsuarioForo(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	nombre_usuario=models.CharField(max_length=45, null=True, blank=True)
	contrasena=models.CharField(max_length=45, null=True, blank=True)
	nombre=models.CharField(max_length=45, null=True, blank=True)
	pais=models.CharField(max_length=45, null=True, blank=True)
	email=models.EmailField(null=True, blank=True)
	fecha_creacion=models.DateField(auto_now_add=True)

	def __str__(self):
		return self.nombre_usuario


class Tema(models.Model):
	titulo=models.CharField(max_length=45)
	contenido=models.TextField()
	imagen=models.ImageField(upload_to='tema_imagen')
	fecha_creacion=models.DateField(auto_now_add=True)
	fecha_actualizacion=models.DateField(auto_now=True)

	def __str__(self):
		return self.titulo


class Noticia(models.Model):
	codigo_noticia=models.CharField(max_length=3)
	titulo=models.CharField(max_length=45)
	contenido=models.TextField()
	total_likes=models.PositiveIntegerField(null=True,blank=True)
	total_comentarios=models.PositiveIntegerField(null=True,blank=True)
	tema=models.ForeignKey(Tema,null=True,blank=True,on_delete=models.CASCADE, related_name="get_news")
	fecha_creacion=models.DateField(auto_now_add=True)
	fecha_actualizacion=models.DateField(auto_now=True)

	def __str__(self):
		return self.titulo


class PropuestaSolucion(models.Model):
	titulo=models.CharField(max_length=45)
	contenido=models.TextField()
	total_likes=models.PositiveIntegerField(null=True,blank=True)
	total_comentarios=models.PositiveIntegerField(null=True,blank=True)
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario=models.OneToOneField(UsuarioForo,null=True,blank=True,on_delete=models.CASCADE)
	tema=models.ForeignKey(Tema,null=True,blank=True,on_delete=models.CASCADE, related_name="get_proposals")

	def __str__(self):
		return self.titulo


class Comentario(models.Model):
	contenido=models.TextField()
	noticia=models.ForeignKey(Noticia,null=True,blank=True,on_delete=models.CASCADE)
	fecha_creacion=models.DateField(auto_now_add=True)
	propuesta=models.ForeignKey(PropuestaSolucion,null=True,blank=True,on_delete=models.CASCADE)

	def __str__(self):
		return self.contenido

