# Generated by Django 4.1.1 on 2022-12-16 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('purbeurre_website', '0004_rename_review_reviewrate_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ReviewRate',
        ),
    ]
