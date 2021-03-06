# Generated by Django 3.1.12 on 2021-06-15 00:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('members', '0001_initial'),
        ('classifications', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('correct_label', models.BooleanField()),
                ('cid', models.ForeignKey(db_column='cid', on_delete=django.db.models.deletion.DO_NOTHING, to='classifications.classification')),
                ('mid', models.ForeignKey(db_column='mid', on_delete=django.db.models.deletion.DO_NOTHING, to='members.member')),
            ],
            options={
                'db_table': 'submission',
            },
        ),
    ]
