# Generated by Django 5.0.7 on 2024-08-29 09:21

import taggit.managers
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_alter_pricechange_unit_price_and_more'),
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
