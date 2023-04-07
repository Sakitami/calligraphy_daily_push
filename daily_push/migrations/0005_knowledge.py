# Generated by Django 4.0.10 on 2023-04-06 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daily_push', '0004_alter_article_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Knowledge',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(help_text='文章日期，格式为YYYY-MM-DD')),
                ('classification', models.CharField(max_length=50)),
                ('article', models.TextField()),
                ('author', models.CharField(default='李白', max_length=45)),
                ('title', models.CharField(default='test', max_length=255)),
            ],
        ),
    ]