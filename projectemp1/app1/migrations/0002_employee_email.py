# Generated by Django 4.0.4 on 2022-04-23 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.EmailField(default='som@gamil.com', max_length=254),
        ),
    ]
