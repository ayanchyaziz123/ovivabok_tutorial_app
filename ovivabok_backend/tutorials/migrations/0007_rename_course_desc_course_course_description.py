# Generated by Django 5.1 on 2024-08-18 05:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0006_remove_course_department_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='course_desc',
            new_name='course_description',
        ),
    ]
