# Generated by Django 4.1.4 on 2023-01-02 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_category_slug_alter_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
