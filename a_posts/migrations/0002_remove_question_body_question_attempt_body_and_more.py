# Generated by Django 5.0.4 on 2024-04-18 08:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("a_posts", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="question",
            name="body",
        ),
        migrations.AddField(
            model_name="question",
            name="attempt_body",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="question",
            name="problem_body",
            field=models.TextField(null=True),
        ),
    ]
