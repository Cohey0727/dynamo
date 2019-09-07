# Generated by Django 2.2.4 on 2019-09-06 02:27
from django.db import migrations


def create_table(apps, schema_editor):
    from ..models import ToDoModel
    ToDoModel.create_table(wait=True)


class Migration(migrations.Migration):
    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_table),
    ]
