# Generated by Django 4.2.20 on 2025-03-26 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('couplers_app', '0005_alter_projects_place'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProdustSectionText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=50)),
                ('subheading', models.CharField(max_length=150)),
            ],
        ),
    ]
