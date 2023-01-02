# Generated by Django 4.1.4 on 2023-01-02 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_category_slug_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.CharField(db_index=True, default='product_name', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.CharField(db_index=True, default='product_name', max_length=255, null=True),
        ),
    ]
