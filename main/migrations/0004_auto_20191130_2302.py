# Generated by Django 2.2.7 on 2019-11-30 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20191130_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='edad',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pninno',
            name='estatura',
            field=models.FloatField(),
        ),
    ]