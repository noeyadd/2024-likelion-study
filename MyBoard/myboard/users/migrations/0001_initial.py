# Generated by Django 5.1.1 on 2024-09-19 15:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('nickname', models.CharField(max_length=128)),
                ('position', models.CharField(max_length=128)),
                ('subjects', models.CharField(max_length=128)),
                ('image', models.ImageField(default='default.png', upload_to='profile/')),
            ],
        ),
    ]
