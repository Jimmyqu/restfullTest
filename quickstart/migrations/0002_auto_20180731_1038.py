# Generated by Django 2.0.7 on 2018-07-31 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artical',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
