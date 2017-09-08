# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('invoice', '0002_auto_20170906_1546'),
    ]

    currencies = [
        ('USD', '', '$'),
        ('EUR', '€', ''),
    ]

    operations = [
        migrations.RunSQL(
            [("insert into invoice_currency (code, pre_symbol, post_symbol) values (%s, %s, %s);", values)]) for values
        in currencies
        ]
