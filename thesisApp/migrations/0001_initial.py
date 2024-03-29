# Generated by Django 4.2.7 on 2023-11-25 14:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('user', 'User'), ('author', 'Author'), ('supervisor', 'Supervisor'), ('co_supervisor', 'Co-Supervisor'), ('admin', 'Admin')], default='user', max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Thesis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thesis_no', models.CharField(max_length=7)),
                ('title', models.CharField(max_length=500)),
                ('abstract', models.TextField(max_length=5000)),
                ('text', models.TextField()),
                ('thesis_type', models.CharField(max_length=255)),
                ('language', models.CharField(max_length=255)),
                ('page_amount', models.IntegerField()),
                ('year', models.IntegerField()),
                ('submission_date', models.DateField()),
                ('topic', models.CharField(max_length=255)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authored_thesis_set', to='thesisApp.person')),
                ('co_supervisor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='co_supervised_thesis_set', to='thesisApp.person')),
                ('institute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thesisApp.institute')),
                ('keywords', models.ManyToManyField(to='thesisApp.keyword')),
                ('supervisor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='supervised_thesis_set', to='thesisApp.person')),
            ],
        ),
        migrations.AddField(
            model_name='institute',
            name='university',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thesisApp.university'),
        ),
    ]
