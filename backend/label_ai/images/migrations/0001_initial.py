# Generated by Django 3.1.12 on 2021-06-15 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('iid', models.TextField(primary_key=True, serialize=False)),
                ('original_url', models.TextField()),
                ('small_url', models.TextField()),
                ('rotation', models.IntegerField()),
            ],
            options={
                'db_table': 'image',
            },
        ),
    ]
