# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0007_fruit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ox',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('horn_length', models.IntegerField()),
            ],
            options={
                'ordering': ['horn_length'],
                'db_table': 'awesome_ox',
                'verbose_name_plural': 'oxen',
            },
            bases=(models.Model,),
        ),
    ]
