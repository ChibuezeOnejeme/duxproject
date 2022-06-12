# Generated by Django 4.0.4 on 2022-05-31 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipapp', '0005_delete_chart_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chart_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=200, null=True)),
                ('data', models.IntegerField(max_length=100, null=True)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
