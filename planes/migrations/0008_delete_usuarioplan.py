# Generated by Django 5.2 on 2025-07-04 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planes', '0007_alter_plan_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UsuarioPlan',
        ),
    ]
