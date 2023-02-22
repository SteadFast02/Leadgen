# Generated by Django 4.0.5 on 2023-01-13 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LeadGenerationApp', '0007_administrator'),
    ]

    operations = [
        migrations.CreateModel(
            name='CallDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerid', models.CharField(default='', max_length=45)),
                ('customername', models.CharField(default='', max_length=45)),
                ('callerid', models.CharField(default='', max_length=45)),
                ('status', models.CharField(default='', max_length=45)),
                ('callername', models.CharField(default='', max_length=45)),
                ('currentdate', models.DateField()),
                ('phonestatus', models.CharField(default='', max_length=45)),
                ('conversation', models.CharField(default='', max_length=200)),
                ('leadstatus', models.CharField(default='', max_length=45)),
                ('mobileno', models.CharField(default='', max_length=12)),
            ],
        ),
    ]