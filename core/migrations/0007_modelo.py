# Generated by Django 5.1.7 on 2025-04-15 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_cor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
                ('marca', models.CharField(max_length=80)),
                ('categoria', models.CharField(max_length=80)),
            ],
        ),
    ]
