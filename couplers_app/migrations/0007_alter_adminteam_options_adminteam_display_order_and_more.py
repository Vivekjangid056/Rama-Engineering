# Generated by Django 4.2.20 on 2025-03-27 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('couplers_app', '0006_produstsectiontext'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adminteam',
            options={'ordering': ['-display_order', 'name'], 'verbose_name': 'Team Member', 'verbose_name_plural': 'Team Members'},
        ),
        migrations.AddField(
            model_name='adminteam',
            name='display_order',
            field=models.PositiveIntegerField(default=0, help_text='Higher numbers appear first'),
        ),
        migrations.AddField(
            model_name='adminteam',
            name='facebook',
            field=models.URLField(blank=True, help_text='Enter Facebook profile URL', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='adminteam',
            name='instagram',
            field=models.URLField(blank=True, help_text='Enter Instagram profile URL', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='adminteam',
            name='linkedin',
            field=models.URLField(blank=True, help_text='Enter LinkedIn profile URL', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='adminteam',
            name='twitter',
            field=models.URLField(blank=True, help_text='Enter Twitter/X profile URL', max_length=255, null=True),
        ),
    ]
