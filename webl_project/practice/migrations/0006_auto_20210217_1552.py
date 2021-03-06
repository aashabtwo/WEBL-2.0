# Generated by Django 3.1.6 on 2021-02-17 15:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('practice', '0005_submissions_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='submissions',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='submissions',
            name='problem',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='practice.problems'),
        ),
    ]
