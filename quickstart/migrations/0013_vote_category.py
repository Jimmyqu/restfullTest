# Generated by Django 2.0.7 on 2018-08-02 01:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0012_remove_artical_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='comments', to='quickstart.Artical'),
        ),
    ]
