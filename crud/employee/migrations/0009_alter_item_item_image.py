# Generated by Django 4.0.3 on 2022-03-17 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0008_alter_item_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.FileField(default='images/default.jpg', upload_to='images/'),
        ),
    ]
