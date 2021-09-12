# Generated by Django 3.2.7 on 2021-09-12 04:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('codigo', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('Periodo_Academico', models.CharField(max_length=25)),
                ('Fecha_inicio_Periodo', models.DateField()),
                ('Duracion_Ciclo', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('dni', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('Nombres', models.CharField(max_length=25)),
                ('Apellidos', models.CharField(max_length=25)),
                ('Fecha_Nacimiento', models.DateField()),
                ('Edad', models.IntegerField()),
                ('sexo', models.CharField(choices=[('H', 'Masculino'), ('F', 'Femenino')], default='H', max_length=1)),
                ('PeriodoAcademico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academico.carrera')),
            ],
        ),
    ]
