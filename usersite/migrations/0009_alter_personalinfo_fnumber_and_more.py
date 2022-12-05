# Generated by Django 4.0.1 on 2022-05-09 15:42

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('usersite', '0008_academic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalinfo',
            name='Fnumber',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='Mnumber',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='S1number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='S2number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='S3number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='income',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='mobnumber',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
    ]
