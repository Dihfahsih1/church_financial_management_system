# Generated by Django 2.1.7 on 2019-03-12 11:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0023_auto_20190312_1418'),
    ]

    operations = [
        migrations.AddField(
            model_name='salaryreportarchive',
            name='Month',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='expensesreportarchive',
            name='Date',
            field=models.DateField(default=datetime.datetime(2019, 3, 12, 11, 32, 57, 990378, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='salary',
            name='Date',
            field=models.DateField(default=datetime.datetime(2019, 3, 12, 11, 32, 57, 989403, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='salaryreportarchive',
            name='Date',
            field=models.DateField(default=datetime.datetime(2019, 3, 12, 11, 32, 57, 991354, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='spend',
            name='Date',
            field=models.DateField(default=datetime.datetime(2019, 3, 12, 11, 32, 57, 990378, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='sundry',
            name='Date',
            field=models.DateField(default=datetime.datetime(2019, 3, 12, 11, 32, 57, 990378, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='sundryreportarchive',
            name='Date',
            field=models.DateField(default=datetime.datetime(2019, 3, 12, 11, 32, 57, 991354, tzinfo=utc)),
        ),
    ]