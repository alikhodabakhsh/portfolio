# Generated by Django 4.0.6 on 2022-07-14 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='title_education',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='title_experience',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]