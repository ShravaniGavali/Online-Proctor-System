# Generated by Django 3.2.12 on 2022-12-12 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersite', '0027_alter_admission_details_year_admission'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='current_semester',
            name='current_sem_num',
        ),
        migrations.AddField(
            model_name='current_semester',
            name='current_year',
            field=models.IntegerField(default=2020),
        ),
        migrations.AddField(
            model_name='personal_details',
            name='address',
            field=models.CharField(default='NULL', max_length=100),
        ),
        migrations.AddField(
            model_name='personal_details',
            name='email',
            field=models.CharField(default='NULL', max_length=30),
        ),
        migrations.AlterField(
            model_name='current_semester',
            name='current_sem',
            field=models.CharField(max_length=50),
        ),
    ]
