# Generated by Django 2.1.4 on 2019-01-15 21:11

from django.db import migrations, models
from django.conf import settings
import django.db.models.deletion
import document.models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0004_documenttemplate'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='template',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='document.DocumentTemplate'),
        ),
    ]
