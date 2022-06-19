# Generated by Django 4.0.5 on 2022-06-19 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('watch', '0008_alter_business_neig_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='neighborhood',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='watch.neighbourhood'),
        ),
        migrations.AlterField(
            model_name='business',
            name='neig_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='watch.neighbourhood'),
        ),
    ]
