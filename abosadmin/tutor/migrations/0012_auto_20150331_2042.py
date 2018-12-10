# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0011_auto_20150331_2034'),
    ]

    operations = [
        migrations.CreateModel(
            name='Female2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('age', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('boobs', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Male2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('age', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('salary', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Monkey',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('age', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='male2',
            name='m2m',
            field=models.ManyToManyField(related_name=b'tutor_male2_related', to='tutor.Monkey'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='female2',
            name='m2m',
            field=models.ManyToManyField(related_name=b'tutor_female2_related', to='tutor.Monkey'),
            preserve_default=True,
        ),
    ]
