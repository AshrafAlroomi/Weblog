# Generated by Django 4.0.3 on 2022-03-09 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=100)),
                ('subtitle', models.TextField(max_length=100)),
                ('img', models.URLField()),
                ('img_thumbnail', models.URLField()),
                ('body', models.TextField(max_length=3000)),
                ('status', models.CharField(choices=[('WAITING', 'WAITING'), ('ACTIVE', 'ACTIVE'), ('SUSPENDED', 'SUSPENDED'), ('STOPPED', 'STOPPED')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ArticleImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.URLField()),
                ('place', models.IntegerField(default=0)),
                ('index', models.IntegerField(default=0)),
                ('type', models.TextField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(max_length=100)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(max_length=100)),
                ('date', models.DateTimeField(auto_now=True)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.comment')),
            ],
        ),
        migrations.CreateModel(
            name='EditHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('type', models.CharField(choices=[('STATUS', 'STATUS'), ('AUTHOR_UPDATE', 'AUTHOR_UPDATE')], max_length=14)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.article')),
            ],
        ),
    ]
