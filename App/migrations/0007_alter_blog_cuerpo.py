# Generated by Django 4.1 on 2022-10-10 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_delete_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='cuerpo',
            field=models.CharField(max_length=10000),
        ),
    ]