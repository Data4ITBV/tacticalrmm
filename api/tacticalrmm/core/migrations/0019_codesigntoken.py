# Generated by Django 3.2 on 2021-04-13 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20210329_1709'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodeSignToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]