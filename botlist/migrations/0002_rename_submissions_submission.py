# Generated by Django 4.0.1 on 2022-01-17 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('botlist', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Submissions',
            new_name='Submission',
        ),
    ]