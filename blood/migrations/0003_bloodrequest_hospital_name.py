# Generated by Django 3.2.8 on 2021-10-29 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0002_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloodrequest',
            name='hospital_name',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
