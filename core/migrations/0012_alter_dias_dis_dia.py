# Generated by Django 4.1.2 on 2022-11-07 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_dias_dis_dia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dias',
            name='dis_dia',
            field=models.CharField(max_length=20),
        ),
    ]