# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0013_auto_20150331_2307'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('place_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='tutor.Place')),
                ('customers', models.ManyToManyField(related_name=b'provider', to='tutor.Place')),
            ],
            options={
            },
            bases=('tutor.place',),
        ),
    ]
