# Generated by Django 2.1.5 on 2021-02-27 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.EmailField(default='user@gmail.com', max_length=20),
        ),
        migrations.AddField(
            model_name='employee',
            name='emp_code',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='mobile',
            field=models.CharField(default=1, max_length=14),
            preserve_default=False,
        ),
    ]
