# Generated by Django 4.1.4 on 2023-01-03 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0003_delete_home_page_blog_post_isi'),
    ]

    operations = [
        migrations.CreateModel(
            name='home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('welcome', models.TextField()),
                ('cover', models.ImageField(upload_to='images/')),
            ],
        ),
    ]