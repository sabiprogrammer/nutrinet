# Generated by Django 3.1.7 on 2021-05-07 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210507_0753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='additives_tags',
            field=models.CharField(blank=True, default=0, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='traces',
            field=models.CharField(blank=True, default=0, max_length=200, null=True),
        ),
    ]
