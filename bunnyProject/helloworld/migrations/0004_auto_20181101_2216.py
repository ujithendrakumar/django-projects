# Generated by Django 2.1.2 on 2018-11-01 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helloworld', '0003_auto_20181101_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='name',
            name='publish',
            field=models.BooleanField(default=True),
        ),
    ]
