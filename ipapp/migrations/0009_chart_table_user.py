# Generated by Django 4.0.4 on 2022-06-01 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipapp', '0008_searched_data_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='chart_table',
            name='user',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
