# Generated by Django 4.1.4 on 2023-01-03 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0004_home'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='text',
            field=models.TextField(null=True),
        ),
    ]
