# Generated by Django 2.0.7 on 2018-07-31 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0006_auto_20180731_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artical',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='../static/uploadImg'),
        ),
    ]
