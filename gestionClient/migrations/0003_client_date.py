# Generated by Django 3.2 on 2021-05-12 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionClient', '0002_souscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='date',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]