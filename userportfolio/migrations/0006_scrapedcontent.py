# Generated by Django 4.2.6 on 2023-10-28 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userportfolio', '0005_useraccount'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScrapedContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
            ],
        ),
    ]
