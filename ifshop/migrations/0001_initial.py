# Generated by Django 5.1.3 on 2024-11-22 12:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Camiseta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data_limite_pedidos', models.DateField()),
                ('data_para_entrega', models.DateField()),
                ('cores', models.CharField(max_length=200)),
                ('tamanhos', models.CharField(max_length=50)),
                ('turnos', models.CharField(max_length=50)),
                ('cursos', models.CharField(max_length=50)),
                ('estilos', models.CharField(default='', max_length=50)),
                ('imagens', models.ImageField(blank=True, null=True, upload_to='imagens_camisetas/')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_estampa', models.CharField(max_length=50)),
                ('numero_estampa', models.IntegerField()),
                ('cor', models.CharField(max_length=20)),
                ('tamanho', models.CharField(max_length=10)),
                ('estilo', models.CharField(default='', max_length=20)),
                ('data_pedido', models.DateTimeField(auto_now_add=True)),
                ('camiseta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ifshop.camiseta')),
            ],
        ),
    ]