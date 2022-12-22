# Generated by Django 4.0.8 on 2022-12-08 16:33

import django.core.serializers.json
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    replaces = [('contracts', '0001_initial'), ('contracts', '0002_remove_contract_content_type_and_more'), ('contracts', '0003_rename_contractinvoice_invoice_alter_invoice_options_and_more'), ('contracts', '0004_remove_contract_circuit_contract_circuit'), ('contracts', '0005_contract_initial_term_contract_invoice_frequency_and_more'), ('contracts', '0006_rename_periode_start_invoice_period_start'), ('contracts', '0007_alter_invoice_options'), ('contracts', '0008_contract_slug_contract_tenant_and_more'), ('contracts', '0009_remove_contract_slug')]

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('circuits', '0038_cabling_cleanup'),
        ('extras', '0077_customlink_extend_text_and_url'),
        ('tenancy', '0007_contact_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('name', models.CharField(max_length=100)),
                ('external_partie', models.CharField(max_length=30)),
                ('internal_partie', models.CharField(default='Active', max_length=50)),
                ('comments', models.TextField(blank=True)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='extras.TaggedItem', to='extras.Tag', verbose_name='Tags')),
                ('circuit', models.ManyToManyField(related_name='contract', to='circuits.circuit')),
                ('initial_term', models.IntegerField(default=12)),
                ('invoice_frequency', models.IntegerField(default=1)),
                ('mrc', models.DecimalField(decimal_places=2, default=1, max_digits=10)),
                ('nrc', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('renewal_term', models.IntegerField(default=12)),
                ('start_date', models.DateField(default='2022-01-01')),
                ('status', models.CharField(default='Active', max_length=50)),
                ('slug', models.SlugField(default='test', max_length=100, unique=True)),
                ('tenant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='contracts', to='tenancy.tenant')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('number', models.CharField(max_length=100)),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoice', to='contracts.contract')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='extras.TaggedItem', to='extras.Tag', verbose_name='Tags')),
                ('amount', models.DecimalField(decimal_places=2, default=1, max_digits=10)),
                ('period_end', models.DateField(default='2022-01-01')),
                ('period_start', models.DateField(default='2022-01-01')),
            ],
            options={
                'abstract': False,
                'ordering': ('-period_start',),
            },
        ),
        migrations.CreateModel(
            name='ServiceProvider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('portal_url', models.URLField(blank=True)),
                ('comments', models.TextField(blank=True)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='extras.TaggedItem', to='extras.Tag', verbose_name='Tags')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AlterField(
            model_name='contract',
            name='external_partie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contract', to='contracts.serviceprovider'),
        ),
        migrations.RemoveField(
            model_name='contract',
            name='slug',
        ),
    ]