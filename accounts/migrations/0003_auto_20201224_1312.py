# Generated by Django 3.1.1 on 2020-12-24 07:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20201224_1227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='username',
        ),
        migrations.AddField(
            model_name='person',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
