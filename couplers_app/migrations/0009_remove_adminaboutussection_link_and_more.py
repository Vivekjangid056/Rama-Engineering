# Generated by Django 5.0.1 on 2025-03-22 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('couplers_app', '0008_delete_adminbannerslider_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adminaboutussection',
            name='link',
        ),
        migrations.RemoveField(
            model_name='adminaboutussection',
            name='main_content',
        ),
        migrations.RemoveField(
            model_name='adminaboutussection',
            name='media_type',
        ),
        migrations.AddField(
            model_name='adminaboutussection',
            name='service1',
            field=models.CharField(blank=True, max_length=26, null=True),
        ),
        migrations.AddField(
            model_name='adminaboutussection',
            name='service2',
            field=models.CharField(blank=True, max_length=26, null=True),
        ),
        migrations.AddField(
            model_name='adminaboutussection',
            name='service3',
            field=models.CharField(blank=True, max_length=26, null=True),
        ),
        migrations.AddField(
            model_name='adminaboutussection',
            name='service4',
            field=models.CharField(blank=True, max_length=26, null=True),
        ),
        migrations.AlterField(
            model_name='adminaboutussection',
            name='about_us_media',
            field=models.ImageField(blank=True, null=True, upload_to='about_us_section/'),
        ),
    ]
