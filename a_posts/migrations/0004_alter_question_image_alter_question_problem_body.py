# Generated by Django 5.0.4 on 2024-04-18 20:00

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_posts', '0003_remove_question_attempt_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='question',
            name='problem_body',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
