# Generated by Django 3.2.3 on 2021-05-19 07:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0005_auto_20210519_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrolmentrecord',
            name='date_enrolled',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='student',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
