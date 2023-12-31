# Generated by Django 4.2.4 on 2023-08-29 03:35

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('sobrenome', models.CharField(max_length=255)),
                ('cpf', models.CharField(max_length=14)),
                ('tempo_de_servico', models.PositiveIntegerField(default=0)),
                ('remuneracao', models.DecimalField(decimal_places=3, max_digits=8)),
            ],
            managers=[
                ('objeto', django.db.models.manager.Manager()),
            ],
        ),
    ]
