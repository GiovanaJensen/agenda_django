# Generated by Django 4.0 on 2021-12-14 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_evento_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='local',
            field=models.TextField(blank=True, null=True),
        ),
    ]