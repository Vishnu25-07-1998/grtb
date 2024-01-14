# Generated by Django 4.2.7 on 2023-12-20 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lifeapp', '0004_delete_patient'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientLedger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_id', models.CharField(max_length=10, unique=True)),
                ('patient_name', models.CharField(max_length=50)),
                ('admission_date', models.DateField()),
                ('discharge_date', models.DateField()),
                ('total_charges', models.DecimalField(decimal_places=2, max_digits=10)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
