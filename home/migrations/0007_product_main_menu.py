# Generated by Django 5.0.7 on 2024-07-20 08:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_comment_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='main_menu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='main_menu', to='home.mainmenu'),
        ),
    ]