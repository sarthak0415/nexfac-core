# Generated by Django 3.2.9 on 2021-11-16 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nexfac_core_api', '0004_task_task_inputs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_inputs',
            field=models.JSONField(null=True),
        ),
    ]
