# Generated by Django 4.2.2 on 2023-08-03 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pucApp', '0010_alter_puccertificate_date_uploaded'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
    ]
