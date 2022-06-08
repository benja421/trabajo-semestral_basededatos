# Generated by Django 4.0.4 on 2022-06-08 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0009_alter_usuario_idusu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comuna',
            name='idComuna',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='id de la comuna'),
        ),
        migrations.AlterField(
            model_name='duennio',
            name='idDuennio',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='id del dueño'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='contra',
            field=models.CharField(max_length=30, verbose_name='Contraseña del usuario'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='correo',
            field=models.EmailField(max_length=254, verbose_name='Correo del usuario'),
        ),
    ]
