# Generated by Django 5.0.7 on 2024-07-23 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_remove_product_rate_comment_rate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='verified',
        ),
    ]
