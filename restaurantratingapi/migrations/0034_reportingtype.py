# Generated by Django 3.0.7 on 2020-07-06 01:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restaurantratingapi', '0033_reply'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportingType',
            fields=[
                ('reporting_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('reporting_type_name', models.CharField(max_length=50)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True, null=True)),
                ('created_by', models.ForeignKey(db_column='created_by', on_delete=django.db.models.deletion.DO_NOTHING, related_name='report_type_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, db_column='updated_by', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='report_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'reporting_type',
                'managed': True,
            },
        ),
    ]
