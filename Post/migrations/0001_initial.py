# Generated by Django 2.0.3 on 2018-04-07 22:50

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
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments_text', models.TextField()),
                ('comments_date', models.DateTimeField(auto_now_add=True)),
                ('comments_parent', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'comments',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=100)),
                ('post_text', models.TextField()),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('post_date_update', models.DateTimeField(auto_now=True)),
                ('post_speciality_number', models.CharField(default='', max_length=15)),
                ('post_short_description', models.CharField(max_length=100)),
                ('post_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'post',
            },
        ),
    ]
