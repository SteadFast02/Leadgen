# Generated by Django 4.0.5 on 2022-12-29 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LeadGenerationApp', '0002_states'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stateid', models.IntegerField()),
                ('cityid', models.IntegerField()),
                ('cityname', models.CharField(default='', max_length=45)),
            ],
        ),
    ]