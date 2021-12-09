# Generated by Django 4.0 on 2021-12-09 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('dt_evento', models.DateTimeField()),
                ('dt_criacao', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'evento',
            },
        ),
    ]
