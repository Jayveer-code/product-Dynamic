# Generated by Django 5.0 on 2024-03-04 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_blog_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='unique_id',
            field=models.CharField(auto_created=True, blank=True, max_length=200, null=True, unique=True),
        ),
    ]
