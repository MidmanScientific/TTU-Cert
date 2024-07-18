# Generated by Django 5.0.1 on 2024-07-15 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SubCert', '0005_remove_automaticlogin_request'),
    ]

    operations = [
        migrations.CreateModel(
            name='myVerification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_number', models.CharField(max_length=10)),
                ('student_name', models.CharField(max_length=50)),
                ('course', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50)),
                ('starting_year', models.IntegerField(max_length=10)),
                ('ending_year', models.IntegerField(max_length=10)),
                ('divisions', models.CharField(max_length=50)),
                ('cgpa', models.DecimalField(decimal_places=2, max_digits=5)),
                ('number_of_trails', models.IntegerField(max_length=5)),
            ],
        ),
    ]
