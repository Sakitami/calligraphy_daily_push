# Generated by Django 4.1.7 on 2023-03-24 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daily_push', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='type',
            new_name='classification',
        ),
        migrations.AddField(
            model_name='article',
            name='auther',
            field=models.CharField(default='李白', max_length=45),
        ),
        migrations.AddField(
            model_name='article',
            name='title',
            field=models.CharField(default='test', max_length=255),
        ),
    ]
