# Generated by Django 5.1.4 on 2024-12-15 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0005_alter_blogpost_content"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name_plural": "Category"},
        ),
    ]
