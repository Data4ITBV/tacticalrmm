# Generated by Django 3.0.3 on 2020-02-29 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0003_agent_wmi_detail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agent',
            name='cpu_info',
        ),
    ]
