# Generated by Django 4.0.3 on 2022-03-09 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogFollow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_role', models.CharField(choices=[('POST+', 'post without review from editor'), ('POST', 'post after review approve from editor'), ('UNPOST', "can't post"), ('NON', 'not')], default='NON', max_length=10)),
                ('join_date', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('WAITING', 'WAITING'), ('ACTIVE', 'ACTIVE'), ('SUSPENDED', 'SUSPENDED'), ('STOPPED', 'STOPPED')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='UserFollow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
