# Generated by Django 3.0.3 on 2020-02-18 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Documents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='image_name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
