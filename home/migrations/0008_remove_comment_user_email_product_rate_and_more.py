# Generated by Django 5.0.7 on 2024-07-20 09:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_product_main_menu'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user_email',
        ),
        migrations.AddField(
            model_name='product',
            name='rate',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_comment', to=settings.AUTH_USER_MODEL),
        ),
    ]
