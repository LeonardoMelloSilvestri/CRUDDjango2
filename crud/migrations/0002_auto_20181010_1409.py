# Generated by Django 2.1.2 on 2018-10-10 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=8)),
                ('level', models.IntegerField()),
                ('positionX', models.IntegerField()),
                ('positionY', models.IntegerField()),
                ('highestScorePong', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
    ]
