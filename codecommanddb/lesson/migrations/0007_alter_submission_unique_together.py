# Generated by Django 4.0.3 on 2022-05-16 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0006_alter_answer_question_alter_answer_submissions_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='submission',
            unique_together={('token', 'question')},
        ),
    ]
