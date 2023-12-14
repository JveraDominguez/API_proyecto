# Generated by Django 4.2.7 on 2023-11-18 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='fabricante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='automovile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca_auto', models.CharField(max_length=30)),
                ('color_auto', models.CharField(max_length=10)),
                ('placa_auto', models.CharField(max_length=6)),
                ('propietario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='personas.persona')),
            ],
        ),
    ]