# Generated by Django 5.1 on 2024-12-20 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('company_name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('employment_type', models.CharField(max_length=50)),
                ('salary', models.CharField(blank=True, max_length=100, null=True)),
                ('details_url', models.URLField()),
                ('posted_date', models.DateField()),
            ],
        ),
    ]
