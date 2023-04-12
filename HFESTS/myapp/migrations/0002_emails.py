# Generated by Django 4.2 on 2023-04-12 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emails',
            fields=[
                ('emailid', models.AutoField(db_column='emailID', primary_key=True, serialize=False)),
                ('emailto', models.CharField(blank=True, db_column='emailTo', max_length=40, null=True)),
                ('emailfrom', models.CharField(blank=True, db_column='emailFrom', max_length=40, null=True)),
                ('emaildate', models.DateField(blank=True, db_column='emailDate', null=True)),
                ('emailsubject', models.CharField(blank=True, db_column='emailSubject', max_length=100, null=True)),
                ('emailbody', models.CharField(blank=True, db_column='emailBody', max_length=1000, null=True)),
            ],
            options={
                'db_table': 'Emails',
                'managed': False,
            },
        ),
    ]
