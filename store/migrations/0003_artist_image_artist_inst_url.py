# Generated by Django 4.2.7 on 2023-11-21 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_rename_iamge_painting_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/artist/'),
        ),
        migrations.AddField(
            model_name='artist',
            name='inst_url',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
