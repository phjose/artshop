# Generated by Django 4.2.7 on 2024-01-20 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_painting_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='painting',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]
