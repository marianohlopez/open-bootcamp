# Generated by Django 4.2.1 on 2023-05-23 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Director",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nombre",
                    models.CharField(help_text="Nombre del director", max_length=100),
                ),
                ("fecha_nacimiento", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="Pelicula",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titulo", models.CharField(max_length=100)),
                ("descripcion", models.TextField()),
                (
                    "director",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="director.director",
                    ),
                ),
            ],
        ),
    ]
