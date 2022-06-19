<<<<<<< HEAD
# Generated by Django 4.0.5 on 2022-06-18 18:45

from django.db import migrations, models
# Generated by Django 4.0.5 on 2022-06-18 11:20
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
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='IMAGE', upload_to='posts/')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField()),
            ]
            name='business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bsn_name', models.CharField(max_length=100)),
                ('bsn_email', models.EmailField(max_length=254)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
