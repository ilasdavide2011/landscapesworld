# Generated by Django 3.2.3 on 2021-08-15 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='landscape',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('immagine', models.ImageField(upload_to='')),
                ('nome', models.CharField(max_length=20)),
                ('descrizione', models.CharField(max_length=40)),
            ],
        ),
    ]
