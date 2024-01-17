# Generated by Django 5.0.1 on 2024-01-17 09:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0004_alter_newspaper_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspaper',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='topic_newspapers', to='agency.topic'),
        ),
    ]