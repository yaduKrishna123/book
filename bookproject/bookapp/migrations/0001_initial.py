# Generated by Django 3.2.13 on 2022-09-20 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('dec', models.TextField()),
                ('year', models.IntegerField()),
                ('img', models.ImageField(upload_to='images')),
            ],
        ),
    ]