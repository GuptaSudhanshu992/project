# Generated by Django 5.1.4 on 2024-12-31 09:05

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0008_blogpost_reading_time"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogpost",
            name="snippet",
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]