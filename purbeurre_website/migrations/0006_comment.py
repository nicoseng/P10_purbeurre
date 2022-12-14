# Generated by Django 4.1.1 on 2022-12-16 21:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('purbeurre_website', '0005_delete_reviewrate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=500)),
                ('rating', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('product_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='purbeurre_website.product')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
