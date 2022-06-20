# Generated by Django 4.0.5 on 2022-06-20 19:55

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('watch', '0002_posts_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='neighbourhood',
            name='health',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None),
        ),
        migrations.AddField(
            model_name='neighbourhood',
            name='police',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None),
        ),
    ]
