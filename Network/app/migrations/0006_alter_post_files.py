# Generated by Django 3.2.5 on 2021-09-19 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_post_files'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='files',
            field=models.FileField(default='C:\\Users\\admin\\Desktop\\D13\\Network\\media/uploads/sample.txt', upload_to='uploads/'),
        ),
    ]
