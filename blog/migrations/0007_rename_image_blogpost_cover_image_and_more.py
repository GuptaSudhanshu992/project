# Generated by Django 5.1.4 on 2024-12-27 05:37

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0006_alter_category_options"),
    ]

    operations = [
        migrations.RenameField(
            model_name="blogpost",
            old_name="image",
            new_name="cover_image",
        ),
        migrations.RenameField(
            model_name="blogpost",
            old_name="image_alt",
            new_name="cover_image_alt",
        ),
        migrations.RemoveField(
            model_name="blogpost",
            name="content",
        ),
        migrations.CreateModel(
            name="BlogSection",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "section_title",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("content_text", ckeditor.fields.RichTextField(blank=True, null=True)),
                (
                    "section_image",
                    models.ImageField(
                        blank=True, null=True, upload_to="media/blog_images/"
                    ),
                ),
                (
                    "section_image_alt",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "section_video_url",
                    models.URLField(blank=True, max_length=500, null=True),
                ),
                (
                    "blog_post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sections",
                        to="blog.blogpost",
                    ),
                ),
            ],
        ),
    ]
