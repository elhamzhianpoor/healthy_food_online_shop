# Generated by Django 5.0.7 on 2024-08-05 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_alter_mainmenu_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('-created',)},
        ),
    ]
