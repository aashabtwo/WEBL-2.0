# Generated by Django 3.1.6 on 2021-02-19 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0004_auto_20210219_1310'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignments',
            name='teachers_remarks',
        ),
        migrations.AddField(
            model_name='assignmentsubmissions',
            name='teachers_remarks',
            field=models.TextField(default=''),
        ),
    ]
