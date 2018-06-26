# Generated by Django 2.0.4 on 2018-06-26 08:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('foro', '0005_auto_20180626_0535'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuarioforo',
            name='contrasena',
        ),
        migrations.RemoveField(
            model_name='usuarioforo',
            name='email',
        ),
        migrations.RemoveField(
            model_name='usuarioforo',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='usuarioforo',
            name='nombre_usuario',
        ),
        migrations.AddField(
            model_name='usuarioforo',
            name='key_activacion',
            field=models.CharField(default=1, max_length=255),
        ),
        migrations.AddField(
            model_name='usuarioforo',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='usuarioforo',
            name='validacion_email',
            field=models.BooleanField(default=False),
        ),
    ]
