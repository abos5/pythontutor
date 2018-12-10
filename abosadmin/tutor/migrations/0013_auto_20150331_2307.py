# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0012_auto_20150331_2042'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zoo',
            fields=[
                ('place_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='tutor.Place')),
                ('with_dog', models.BooleanField(default=False)),
                ('with_dragon', models.BooleanField(default=False)),
                ('with_money', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=('tutor.place',),
        ),
        migrations.AlterField(
            model_name='female2',
            name='m2m',
            field=models.ManyToManyField(related_name=b'tutor_female2_related', verbose_name=b'monkeys', to=b'tutor.Monkey'),
        ),
        migrations.AlterField(
            model_name='male2',
            name='m2m',
            field=models.ManyToManyField(related_name=b'tutor_male2_related', verbose_name=b'monkeys', to=b'tutor.Monkey'),
        ),
    ]
