# Generated by Django 3.2.3 on 2021-07-27 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Uni_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(default='', max_length=50, verbose_name='user')),
                ('email_id', models.EmailField(default='', max_length=50, verbose_name='email')),
            ],
        ),
    ]
