# Generated by Django 3.0.5 on 2022-09-17 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0012_studentextra_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentextra',
            name='cl',
            field=models.CharField(choices=[('one', 'Programacion'), ('Calculo', 'two'), ('three', 'three'), ('four', 'four'), ('five', 'five'), ('six', 'six'), ('seven', 'seven'), ('eight', 'eight'), ('nine', 'nine'), ('ten', 'ten')], default='one', max_length=10),
        ),
    ]
