# Generated by Django 2.0.3 on 2018-05-10 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('debate', '0008_debate_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='debate',
            name='number_arguments',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]