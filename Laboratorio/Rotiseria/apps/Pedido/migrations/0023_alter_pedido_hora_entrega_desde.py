# Generated by Django 3.2.4 on 2022-11-03 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pedido', '0022_alter_pedido_hora_entrega_desde'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='hora_entrega_desde',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
