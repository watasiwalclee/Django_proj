# Generated by Django 3.0.8 on 2020-11-13 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainfeatures', '0002_auto_20201113_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='compensate',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='member',
            name='in_battle',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Status',
        ),
    ]
