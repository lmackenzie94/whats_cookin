# Generated by Django 3.0.8 on 2020-07-23 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0002_auto_20200720_0218'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='tips',
            field=models.TextField(blank=True, verbose_name='Helpful Tips'),
        ),
    ]
