# Generated by Django 2.0.3 on 2018-05-08 21:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ArgumentsAgainst',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('argument', models.TextField(max_length=500)),
                ('publication_date', models.DateField(auto_now_add=True)),
                ('created_by', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ArgumentsFor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('argument', models.TextField(max_length=500)),
                ('publication_date', models.DateField(auto_now_add=True)),
                ('created_by', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Debate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('publication_date', models.DateField(auto_now_add=True)),
                ('arguments_against', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='debate.ArgumentsAgainst')),
                ('arguments_for', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='debate.ArgumentsFor')),
                ('created_by', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
