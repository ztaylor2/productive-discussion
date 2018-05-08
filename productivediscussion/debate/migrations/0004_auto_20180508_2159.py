# Generated by Django 2.0.3 on 2018-05-08 21:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('debate', '0003_auto_20180508_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='argumentsagainst',
            name='created_by',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='argumentsfor',
            name='created_by',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
