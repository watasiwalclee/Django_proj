# Generated by Django 3.0.8 on 2020-11-15 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainfeatures', '0004_auto_20201113_2110'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='turn',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
