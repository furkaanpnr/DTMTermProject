# Generated by Django 4.2.7 on 2024-01-05 15:29

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thesisApp', '0002_subjecttopic_alter_thesis_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thesis',
            name='abstract',
            field=ckeditor.fields.RichTextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='thesis',
            name='text',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='thesis',
            name='thesis_no',
            field=models.CharField(editable=False, max_length=7, unique=True),
        ),
    ]
