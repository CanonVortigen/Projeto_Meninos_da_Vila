# Generated by Django 3.2.6 on 2022-06-15 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('valor', models.CharField(max_length=30)),
                ('imagem', models.ImageField(blank=True, upload_to='produtos/')),
                ('descricao', models.CharField(max_length=200)),
                ('horario', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
        migrations.DeleteModel(
            name='Produtos',
        ),
    ]
