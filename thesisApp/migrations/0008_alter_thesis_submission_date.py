# Generated by Django 4.2.7 on 2024-01-06 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thesisApp', '0007_language_alter_thesis_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thesis',
            name='submission_date',
            field=models.DateField(auto_created=True, auto_now_add=True),
        ),
    ]
