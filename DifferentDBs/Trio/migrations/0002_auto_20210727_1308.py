# Generated by Django 3.2.3 on 2021-07-27 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trio_data',
            name='content',
        ),
        migrations.AddField(
            model_name='trio_data',
            name='company',
            field=models.CharField(default='', max_length=50, verbose_name='company'),
        ),
        migrations.AlterField(
            model_name='trio_data',
            name='app_name',
            field=models.CharField(default='', max_length=50, verbose_name='app_name'),
        ),
        migrations.AlterField(
            model_name='trio_data',
            name='title',
            field=models.CharField(default='', max_length=50, verbose_name='title'),
        ),
    ]
