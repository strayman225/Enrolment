# Generated by Django 3.2.3 on 2021-05-19 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0003_auto_20210519_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='fathername',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='fatheroccu',
            field=models.CharField(blank=True, max_length=125, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='mothername',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='motheroccu',
            field=models.CharField(blank=True, max_length=125, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='phonenumber',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='prevschool',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]