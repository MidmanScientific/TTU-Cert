# Generated by Django 5.0.1 on 2024-07-13 04:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SubCert', '0003_automaticlogin'),
    ]

    operations = [
        migrations.AddField(
            model_name='automaticlogin',
            name='request',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SubCert.companyrequest'),
        ),
    ]
