# Generated by Django 4.1.1 on 2022-10-30 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Pedido', '0016_estadoentrega_cadete'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estadoentrega',
            name='cadete',
        ),
    ]
