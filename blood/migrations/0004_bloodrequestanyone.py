# Generated by Django 3.2.8 on 2021-10-30 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0002_alter_donor_profile_pic'),
        ('blood', '0003_bloodrequest_hospital_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='BloodRequestAnyone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=30)),
                ('patient_age', models.PositiveIntegerField()),
                ('reason', models.CharField(max_length=500)),
                ('bloodgroup', models.CharField(max_length=10)),
                ('unit', models.PositiveIntegerField(default=0)),
                ('status', models.CharField(default='Pending', max_length=20)),
                ('hospital_name', models.CharField(default=None, max_length=50)),
                ('date', models.DateField(auto_now=True)),
                ('donor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='donor.donor')),
            ],
        ),
    ]
