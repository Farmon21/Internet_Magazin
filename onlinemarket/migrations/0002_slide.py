# Generated by Django 4.2 on 2023-05-10 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinemarket', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='slide_images')),
            ],
        ),
    ]
