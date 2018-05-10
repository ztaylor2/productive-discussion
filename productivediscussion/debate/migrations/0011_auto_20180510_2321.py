# Generated by Django 2.0.3 on 2018-05-10 23:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('debate', '0010_auto_20180510_2229'),
    ]

    operations = [
        migrations.CreateModel(
            name='Argument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('argument', models.TextField(max_length=500)),
                ('side', models.CharField(choices=[('For', 'For'), ('Against', 'Against')], max_length=50)),
                ('publication_date', models.DateField(auto_now_add=True)),
                ('created_by', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('debate', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='debate.Debate')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('argument', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='debate.Argument')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='argumentsagainst',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='argumentsagainst',
            name='debate',
        ),
        migrations.RemoveField(
            model_name='argumentsfor',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='argumentsfor',
            name='debate',
        ),
        migrations.DeleteModel(
            name='ArgumentsAgainst',
        ),
        migrations.DeleteModel(
            name='ArgumentsFor',
        ),
    ]
