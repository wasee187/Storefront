# Generated by Django 4.2.16 on 2024-12-24 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='zip_code',
            field=models.CharField(default='0000', max_length=255),
            preserve_default=False,
        ),
    ]