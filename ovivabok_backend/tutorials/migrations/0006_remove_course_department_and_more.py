# Generated by Django 5.1 on 2024-08-18 05:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0005_department_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='department',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='course_description',
            new_name='course_desc',
        ),
        migrations.DeleteModel(
            name='Department',
        ),
    ]
