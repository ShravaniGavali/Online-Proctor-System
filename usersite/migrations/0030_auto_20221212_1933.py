# Generated by Django 3.2.12 on 2022-12-12 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersite', '0029_personal_details_guardian_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personal_details',
            name='stud_image',
        ),
        migrations.AddField(
            model_name='personal_details',
            name='birth_date',
            field=models.DateField(default=8),
        ),
    ]
