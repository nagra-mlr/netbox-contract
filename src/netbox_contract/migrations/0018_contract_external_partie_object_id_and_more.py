# Generated by Django 4.2.5 on 2023-09-18 21:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('netbox_contract', '0017_alter_contract_accounting_dimensions'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='external_partie_object_id',
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='external_partie_object_type',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to='contenttypes.contenttype',
            ),
        ),
        migrations.AddIndex(
            model_name='contract',
            index=models.Index(
                fields=['external_partie_object_type', 'external_partie_object_id'],
                name='netbox_cont_externa_6343fb_idx',
            ),
        ),
        migrations.AddIndex(
            model_name='contractassignement',
            index=models.Index(
                fields=['content_type', 'object_id'],
                name='netbox_cont_content_ff787b_idx',
            ),
        ),
    ]
