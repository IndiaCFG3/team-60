# Generated by Django 3.1 on 2020-08-16 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mob_login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mob_email', models.CharField(max_length=100)),
                ('mob_pass', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='mob_to_task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mob_name', models.CharField(max_length=100)),
                ('mob_task', models.CharField(max_length=100)),
                ('task_date', models.CharField(max_length=100)),
                ('task_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='mobilizer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mob_name', models.CharField(max_length=100)),
                ('mob_contact', models.IntegerField()),
                ('mob_email', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='op_login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('op_email', models.CharField(max_length=100)),
                ('op_pass', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='op_manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('op_name', models.CharField(max_length=100)),
                ('op_contact', models.IntegerField()),
                ('op_email', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='op_to_mob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('op_name', models.CharField(max_length=100)),
                ('mob_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('user_contact', models.IntegerField()),
                ('user_email', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='user_to_skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('user_skills', models.CharField(max_length=100)),
            ],
        ),
    ]
