# Generated by Django 4.2.7 on 2023-12-05 11:45

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('grades_app', '0005_alter_english_grade_10_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomGroupData',
            fields=[
                ('group', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='custom_data', serialize=False, to='auth.group')),
                ('name', models.CharField(choices=[('admin', 'Administrator'), ('editor', 'Editor'), ('viewer', 'Viewer')], max_length=50, unique=True, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='CustomGroup',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('auth.group',),
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
    ]
