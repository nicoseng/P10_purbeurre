# Generated by Django 4.1.1 on 2022-12-29 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purbeurre_website', '0006_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='rating',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
