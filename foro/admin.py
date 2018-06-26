from django.contrib import admin
from .models import UsuarioForo, Tema, Noticia, PropuestaSolucion, Comentario

# Register your models here.

'''
@admin.register(UsuarioForo)
class UsuarioForoAdmin(admin.ModelAdmin):
	list_display=('nombre','nombre_usuario','pais','email',)
'''


@admin.register(Tema)
class TemaAdmin(admin.ModelAdmin):
	list_display=('id','titulo','fecha_creacion',)


@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
	list_display=('id','titulo','total_likes','total_comentarios','tema',)


@admin.register(PropuestaSolucion)
class PropuestaSolucionAdmin(admin.ModelAdmin):
	list_display=('id','titulo','total_likes','total_comentarios','fecha_creacion','usuario','tema',)


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
	list_display=('contenido','noticia','propuesta',)