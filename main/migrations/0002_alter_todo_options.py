# Generated by Django 4.2.6 on 2023-10-30 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'verbose_name': 'Todo', 'verbose_name_plural': 'Todos'},
        ),
    ]
