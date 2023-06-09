# Generated by Django 4.1.7 on 2023-03-24 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image_url', models.URLField(blank=True)),
                ('type', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('date', models.DateField()),
                ('view', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
