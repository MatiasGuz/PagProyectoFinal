# Generated by Django 3.2.4 on 2021-06-26 04:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoFinal', '0005_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='categorias',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='ProyectoFinal.categoria'),
        ),
    ]
