# Generated by Django 2.1.7 on 2019-03-05 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pdfbyte',
            fields=[
                ('name', models.CharField(max_length=1000, primary_key=True, serialize=False, unique=True)),
                ('bytedata', models.BinaryField()),
            ],
        ),
    ]
