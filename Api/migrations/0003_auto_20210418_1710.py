# Generated by Django 2.2.4 on 2021-04-18 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0002_auto_20210418_1603'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='generos',
            name='codGenero',
        ),
        migrations.AlterField(
            model_name='generos',
            name='dataatualizacao',
            field=models.DateTimeField(auto_now_add=True, db_column='DataAtualizacao', null=True),
        ),
        migrations.AlterField(
            model_name='generos',
            name='datacriacao',
            field=models.DateTimeField(auto_now=True, db_column='DataCriacao', null=True),
        ),
    ]
