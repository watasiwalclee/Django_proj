# Generated by Django 3.0.8 on 2020-11-13 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainfeatures', '0003_auto_20201113_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='uid',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]