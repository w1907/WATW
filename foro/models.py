from django.db import models

# Create your models here.

class UsuarioForo(models.Model):
	nombre_usuario=models.CharField(max_length=45)
	contrasena=models.CharField(max_length=45)
	nombre=models.CharField(max_length=45)
	pais=models.CharField(max_length=45)
	email=models.EmailField()

	def __str__(self):
		return self.nombre_usuario


class Tema(models.Model):
	titulo=models.CharField(max_length=45)
	contenido=models.TextField()
	imagen=models.ImageField(upload_to='tema_imagen')
	fecha_creacion=models.DateField(auto_now=True)

	def __str__(self):
		return self.titulo


class Noticia(models.Model):
	codigo_noticia=models.CharField(max_length=3)
	titulo=models.CharField(max_length=45)
	contenido=models.TextField()
	total_likes=models.PositiveIntegerField(null=True,blank=True)
	total_comentarios=models.PositiveIntegerField(null=True,blank=True)
	tema=models.ForeignKey(Tema,null=True,blank=True,on_delete=models.CASCADE)

	def __str__(self):
		return self.titulo


class PropuestaSolucion(models.Model):
	titulo=models.CharField(max_length=45)
	contenido=models.TextField()
	total_likes=models.PositiveIntegerField(null=True,blank=True)
	total_comentarios=models.PositiveIntegerField(null=True,blank=True)
	fecha_creacion=models.DateField(auto_now=True)
	usuario=models.OneToOneField(UsuarioForo,null=True,blank=True,on_delete=models.CASCADE)
	tema=models.OneToOneField(Tema,null=True,blank=True,on_delete=models.CASCADE)

	def __str__(self):
		return self.titulo


class Comentario(models.Model):
	contenido=models.TextField()
	noticia=models.ForeignKey(Noticia,null=True,blank=True,on_delete=models.CASCADE)
	propuesta=models.ForeignKey(PropuestaSolucion,null=True,blank=True,on_delete=models.CASCADE)

	def __str__(self):
		return self.contenido

