# Generated by Django 3.2.7 on 2021-09-15 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academico', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudiante',
            name='sexo',
        ),
        migrations.AddField(
            model_name='estudiante',
            name='sexoM',
            field=models.BooleanField(default=False, verbose_name='Masculino'),
        ),
    ]