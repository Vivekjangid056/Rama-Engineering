# Generated by Django 5.0.1 on 2025-01-09 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('couplers_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnquiryEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=200)),
            ],
        ),
    ]
