# Generated by Django 2.0.3 on 2018-05-10 21:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('debate', '0006_auto_20180510_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='debate',
            name='created_by',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
