# Generated by Django 4.2.7 on 2023-11-16 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_joblist_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=20)),
                ('LastName', models.CharField(max_length=20)),
                ('Gender', models.IntegerField()),
                ('BOD', models.DateField()),
                ('Email', models.CharField(max_length=100)),
                ('Mobile', models.CharField(max_length=20)),
                ('Skill', models.CharField(max_length=200)),
            ],
        ),
    ]
