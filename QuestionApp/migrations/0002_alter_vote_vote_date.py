# Generated by Django 3.2.8 on 2021-10-28 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuestionApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='vote_date',
            field=models.DateTimeField(verbose_name='Date voted'),
        ),
    ]
