# Generated by Django 5.0.7 on 2024-07-31 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_mainmenu_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainmenu',
            name='slug',
            field=models.SlugField(allow_unicode=True, max_length=255, null=True, unique=True),
        ),
    ]
