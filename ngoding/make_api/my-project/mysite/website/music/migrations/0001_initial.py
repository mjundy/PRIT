# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=50)),
                ('genre', models.CharField(max_length=25, default='Pop', choices=[('Pop', 'Pop'), ('Reggae', 'Reggae'), ('Country', 'Country'), ('Jazz', 'Jazz'), ('Hip Hop', 'Hip Hop'), ('Rock', 'Rock'), ('R&B and Souls', 'R&B and Souls'), ('Dangdut', 'Dangdut')])),
                ('singer', models.CharField(max_length=50)),
                ('rating', models.PositiveIntegerField(default=1)),
            ],
        ),
    ]
