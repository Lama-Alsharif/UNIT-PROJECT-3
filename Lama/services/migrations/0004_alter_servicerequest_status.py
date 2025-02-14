# Generated by Django 4.2.4 on 2023-09-04 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_alter_servicerequest_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicerequest',
            name='status',
            field=models.IntegerField(choices=[(1, 'pending'), (2, 'in_progress'), (3, 'done'), (4, 'canceled')], default='pending'),
        ),
    ]
