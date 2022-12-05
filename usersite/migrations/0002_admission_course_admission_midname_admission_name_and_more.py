# Generated by Django 4.0.1 on 2022-05-05 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='admission',
            name='course',
            field=models.CharField(choices=[('Select your branch', 'Select your branch'), ('Computer Science Engineering', 'Computer Science Engineering'), ('Information Technology Engineering', 'Information Technology Engineering'), ('Electronics and Telecommunication Engineering', 'Electronics and Telecommunication Engineering'), ('Electronics Engineering', 'Electronics Engineering')], default='Select your branch', max_length=100),
        ),
        migrations.AddField(
            model_name='admission',
            name='midname',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='admission',
            name='name',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='admission',
            name='procname',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='admission',
            name='rollsem1',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='admission',
            name='rollsem2',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='admission',
            name='rollsem3',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='admission',
            name='rollsem4',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='admission',
            name='rollsem5',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='admission',
            name='rollsem6',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='admission',
            name='rollsem7',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='admission',
            name='rollsem8',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='admission',
            name='surname',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
    ]
