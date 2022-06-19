# Generated by Django 4.0.5 on 2022-06-19 16:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Neighbourhood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('bio', models.TextField(max_length=255)),
                ('location', models.CharField(max_length=55)),
                ('profile_photo', models.ImageField(upload_to='media', verbose_name='image')),
                ('neighborhood', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='watch.neighbourhood')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='IMAGE', upload_to='posts/')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='watch.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bsn_image', models.ImageField(blank=True, upload_to='media', verbose_name='image')),
                ('bsn_name', models.CharField(max_length=100)),
                ('bsn_email', models.EmailField(max_length=254)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('category', models.CharField(choices=[('Police Station', 'Police Station'), ('Hair&Grooming', 'Hair&Grooming'), ('Hospital', 'Hospital'), ('Mall&Markets', 'Mall&Markets'), ('Fast Foods', 'Fast Foods')], max_length=50, null=True)),
                ('weburl', models.URLField(blank=True)),
                ('neig_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='watch.neighbourhood')),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='watch.profile')),
            ],
        ),
    ]
