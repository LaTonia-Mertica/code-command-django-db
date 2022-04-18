# Generated by Django 4.0.3 on 2022-04-07 18:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=256, unique=True)),
                ('description', models.TextField()),
                ('uuid', models.UUIDField(default=uuid.uuid4)),
            ],
        ),
    ]
