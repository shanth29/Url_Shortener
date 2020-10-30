# Generated by Django 3.1.1 on 2020-10-29 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Urls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('long_url', models.URLField(max_length=1000)),
                ('short_url', models.CharField(max_length=12)),
                ('total_hits', models.IntegerField(default=0)),
            ],
        ),
    ]
