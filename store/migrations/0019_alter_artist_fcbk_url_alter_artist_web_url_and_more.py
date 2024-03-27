# Generated by Django 4.2.7 on 2024-03-27 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_rename_url_artist_web_url_alter_artist_inst_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='fcbk_url',
            field=models.URLField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='web_url',
            field=models.URLField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='x_url',
            field=models.URLField(blank=True, max_length=100, null=True),
        ),
    ]
