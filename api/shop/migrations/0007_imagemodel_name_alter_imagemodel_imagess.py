# Generated by Django 4.1.1 on 2022-10-28 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_imagemodel_remove_product_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagemodel',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='imagemodel',
            name='imagess',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
