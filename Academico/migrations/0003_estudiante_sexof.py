# Generated by Django 3.2.7 on 2021-09-15 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academico', '0002_auto_20210915_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='sexoF',
            field=models.BooleanField(default=False, verbose_name='Femenino'),
        ),
    ]
