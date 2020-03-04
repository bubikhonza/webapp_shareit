# Generated by Django 2.1.7 on 2019-06-10 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shr_io', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='media/files/'),
        ),
        migrations.AlterField(
            model_name='shareplace',
            name='code',
            field=models.CharField(max_length=12, unique=True),
        ),
    ]