# Generated by Django 4.0 on 2021-12-26 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.IntegerField(max_length=13)),
                ('content', models.TextField()),
                ('email', models.CharField(max_length=500)),
            ],
        ),
    ]
