# Generated by Django 3.1.4 on 2021-02-05 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0008_fix_fidus_3_3_table_header'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='path',
            field=models.TextField(blank=True, default=''),
        ),
    ]
