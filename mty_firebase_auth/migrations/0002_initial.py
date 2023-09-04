# Generated by Django 4.2.2 on 2023-08-08 22:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mty_firebase_auth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='firebaseuser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='firebase_user', related_query_name='firebase_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
