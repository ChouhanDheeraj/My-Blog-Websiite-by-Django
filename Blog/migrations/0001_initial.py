# Generated by Django 4.0 on 2022-01-01 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=300)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=30)),
                ('timestamp', models.DateTimeField(blank=True)),
            ],
        ),
    ]
