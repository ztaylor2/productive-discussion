# Generated by Django 2.0.3 on 2018-05-10 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('debate', '0007_auto_20180510_2120'),
    ]

    operations = [
        migrations.AddField(
            model_name='debate',
            name='description',
            field=models.TextField(default='default', max_length=500),
            preserve_default=False,
        ),
    ]
