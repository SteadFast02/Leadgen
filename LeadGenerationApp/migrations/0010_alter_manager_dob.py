# Generated by Django 4.0.5 on 2023-01-17 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LeadGenerationApp', '0009_administrator_profilepic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='dob',
            field=models.DateField(default=''),
        ),
    ]