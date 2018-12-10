# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0008_ox'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Ox',
        ),
    ]
