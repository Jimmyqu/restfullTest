# Generated by Django 2.0.7 on 2018-08-01 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0010_auto_20180801_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='artical',
            name='comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='quickstart.Vote'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='bbs_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='quickstart.Artical'),
        ),
    ]
