# Generated by Django 4.0.4 on 2022-06-06 22:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('idComuna', models.IntegerField(primary_key=True, serialize=False, verbose_name='Chip de la Mascota')),
                ('nombreComuna', models.CharField(max_length=40, verbose_name='nombre de la comuna')),
            ],
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('codigoChip', models.IntegerField(primary_key=True, serialize=False, verbose_name='Chip de la Mascota')),
                ('nombreMascota', models.CharField(max_length=20, verbose_name='Nombre de la mascota')),
                ('edad', models.IntegerField(verbose_name='Edad de la mascota')),
            ],
        ),
        migrations.CreateModel(
            name='Rol_usuario',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False, verbose_name='Codigo de usuario')),
                ('tipoUsuario', models.CharField(max_length=20, verbose_name='Tipo de usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idusu', models.IntegerField(primary_key=True, serialize=False, verbose_name='Codigo de usuario')),
                ('nombreUsuario', models.CharField(max_length=20, verbose_name='Nombre del usuario')),
                ('apellido', models.CharField(max_length=20, verbose_name='Apellido del usuario')),
                ('contra', models.CharField(max_length=20, verbose_name='Contraseña del usuario')),
                ('correo', models.CharField(max_length=20, verbose_name='Correo del usuario')),
                ('fechNacimiento', models.DateTimeField(verbose_name='Fecha')),
                ('foto', models.ImageField(null=True, upload_to='mascotas')),
                ('rol_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.rol_usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Duennio',
            fields=[
                ('idDuennio', models.IntegerField(primary_key=True, serialize=False, verbose_name='Chip de la Mascota')),
                ('nombreDuennio', models.CharField(max_length=20, verbose_name='nombre del dueño')),
                ('comuna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.comuna')),
                ('mascota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.mascota')),
            ],
        ),
        migrations.CreateModel(
            name='Atenciones',
            fields=[
                ('idTratamiento', models.IntegerField(primary_key=True, serialize=False, verbose_name='Chip de la Mascota')),
                ('nombreTratamiento', models.CharField(max_length=35, verbose_name='Tratamiento')),
                ('mascota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.mascota')),
            ],
        ),
    ]