# Generated by Django 3.2.3 on 2021-05-19 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='extname',
            field=models.CharField(max_length=25, null=True),
        ),
    ]