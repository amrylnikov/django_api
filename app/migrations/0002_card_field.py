# Generated by Django 4.2.3 on 2023-11-11 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('difficulty', models.CharField(max_length=255)),
                ('layout', models.JSONField()),
                ('history', models.JSONField()),
                ('players', models.JSONField()),
                ('current_player', models.CharField(max_length=255)),
            ],
        ),
    ]
