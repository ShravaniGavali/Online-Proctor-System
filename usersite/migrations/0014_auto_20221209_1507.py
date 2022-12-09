# Generated by Django 3.2.12 on 2022-12-09 09:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usersite', '0013_alter_personalinfo_mobnumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='admission_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ssc_marks', models.DecimalField(decimal_places=2, max_digits=5)),
                ('hsc_marks', models.DecimalField(decimal_places=2, max_digits=5)),
                ('diploma_marks', models.DecimalField(decimal_places=2, max_digits=5)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('default_list_num', models.IntegerField()),
                ('is_defaulter', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='current_semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_sem', models.IntegerField()),
                ('current_sem_num', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='family_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('femail', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('contact_num', models.CharField(max_length=30)),
                ('qualification', models.CharField(max_length=30)),
                ('occupation', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='family_relation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relation_type', models.CharField(max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='personal_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('middle_name', models.CharField(max_length=30)),
                ('birth_place', models.CharField(max_length=30)),
                ('mother_tongue', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=30)),
                ('religion', models.CharField(max_length=30)),
                ('blood_group', models.CharField(max_length=30)),
                ('stud_image', models.ImageField(upload_to='')),
                ('stud_sign_image', models.ImageField(upload_to='')),
                ('family_income', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='semester_sub_ia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_1', models.CharField(max_length=30)),
                ('sub_2', models.CharField(max_length=30)),
                ('sub_3', models.CharField(max_length=30)),
                ('sub_4', models.CharField(max_length=30)),
                ('sub_5', models.CharField(max_length=30)),
                ('sub_6', models.CharField(max_length=30)),
                ('current_semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usersite.current_semester')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='admission',
            name='user',
        ),
        migrations.RemoveField(
            model_name='personalinfo',
            name='user',
        ),
        migrations.DeleteModel(
            name='academic',
        ),
        migrations.DeleteModel(
            name='admission',
        ),
        migrations.DeleteModel(
            name='personalinfo',
        ),
        migrations.AddField(
            model_name='family_info',
            name='relation_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usersite.family_relation'),
        ),
        migrations.AddField(
            model_name='family_info',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='attendance',
            name='current_sem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usersite.current_semester'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
