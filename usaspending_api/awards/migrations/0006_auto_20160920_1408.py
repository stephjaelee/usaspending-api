# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-20 14:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


def drop_award_data(apps, schema_editor):
    awards = apps.get_model('awards', 'Award')
    awards.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('references', '0002_auto_20160920_1408'),
        ('submissions', '0001_initial'),
        ('awards', '0005_merge_20160912_2032'),
    ]

    operations = [
        migrations.RunPython(drop_award_data),
        migrations.CreateModel(
            name='FinancialAssistanceAward',
            fields=[
                ('action_date', models.CharField(max_length=8)),
                ('action_type', models.CharField(blank=True, max_length=1, null=True)),
                ('federal_action_obligation', models.DecimalField(blank=True, decimal_places=0, max_digits=20, null=True)),
                ('award_modification_amendme', models.CharField(blank=True, max_length=50, null=True)),
                ('financial_assistance_award_id', models.AutoField(primary_key=True, serialize=False)),
                ('fain', models.CharField(blank=True, max_length=30, null=True)),
                ('uri', models.CharField(blank=True, max_length=70, null=True)),
                ('cfda_number', models.CharField(blank=True, max_length=7, null=True)),
                ('cfda_title', models.CharField(blank=True, max_length=100, null=True)),
                ('business_funds_indicator', models.CharField(max_length=3)),
                ('non_federal_funding_amount', models.DecimalField(blank=True, decimal_places=0, max_digits=20, null=True)),
                ('total_funding_amount', models.DecimalField(blank=True, decimal_places=0, max_digits=20, null=True)),
                ('face_value_loan_guarantee', models.DecimalField(blank=True, decimal_places=0, max_digits=20, null=True)),
                ('original_loan_subsidy_cost', models.DecimalField(blank=True, decimal_places=0, max_digits=20, null=True)),
                ('federal_funding_amount', models.DecimalField(blank=True, decimal_places=0, max_digits=20, null=True)),
                ('assistance_type', models.CharField(max_length=2)),
                ('record_type', models.IntegerField()),
                ('correction_late_delete_ind', models.CharField(blank=True, max_length=1, null=True)),
                ('fiscal_year_and_quarter_co', models.CharField(blank=True, max_length=5, null=True)),
                ('sai_number', models.CharField(blank=True, max_length=50, null=True)),
                ('drv_awd_fin_assist_type_label', models.CharField(blank=True, max_length=50, null=True)),
                ('reporting_period_start', models.DateField(blank=True, null=True)),
                ('reporting_period_end', models.DateField(blank=True, null=True)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('create_user_id', models.CharField(blank=True, max_length=50, null=True)),
                ('update_user_id', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'financial_assistance_award',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Procurement',
            fields=[
                ('action_date', models.CharField(max_length=8)),
                ('action_type', models.CharField(blank=True, max_length=1, null=True)),
                ('federal_action_obligation', models.DecimalField(blank=True, decimal_places=0, max_digits=20, null=True)),
                ('award_modification_amendme', models.CharField(blank=True, max_length=50, null=True)),
                ('procurement_id', models.AutoField(primary_key=True, serialize=False)),
                ('piid', models.CharField(blank=True, max_length=50)),
                ('parent_award_id', models.CharField(blank=True, max_length=50, null=True)),
                ('cost_or_pricing_data', models.CharField(blank=True, max_length=1, null=True)),
                ('type_of_contract_pricing', models.CharField(blank=True, max_length=2, null=True)),
                ('contract_award_type', models.CharField(blank=True, max_length=1, null=True)),
                ('naics', models.CharField(blank=True, max_length=6, null=True)),
                ('naics_description', models.CharField(blank=True, max_length=150, null=True)),
                ('period_of_perf_potential_e', models.CharField(blank=True, max_length=8, null=True)),
                ('ordering_period_end_date', models.CharField(blank=True, max_length=8, null=True)),
                ('current_total_value_award', models.DecimalField(blank=True, decimal_places=0, max_digits=20, null=True)),
                ('potential_total_value_awar', models.DecimalField(blank=True, decimal_places=0, max_digits=20, null=True)),
                ('referenced_idv_agency_iden', models.CharField(blank=True, max_length=4, null=True)),
                ('idv_type', models.CharField(blank=True, max_length=1, null=True)),
                ('multiple_or_single_award_i', models.CharField(blank=True, max_length=1, null=True)),
                ('type_of_idc', models.CharField(blank=True, max_length=1, null=True)),
                ('a_76_fair_act_action', models.CharField(blank=True, max_length=1, null=True)),
                ('dod_claimant_program_code', models.CharField(blank=True, max_length=3, null=True)),
                ('clinger_cohen_act_planning', models.CharField(blank=True, max_length=1, null=True)),
                ('commercial_item_acquisitio', models.CharField(blank=True, max_length=1, null=True)),
                ('commercial_item_test_progr', models.CharField(blank=True, max_length=1, null=True)),
                ('consolidated_contract', models.CharField(blank=True, max_length=1, null=True)),
                ('contingency_humanitarian_o', models.CharField(blank=True, max_length=1, null=True)),
                ('contract_bundling', models.CharField(blank=True, max_length=1, null=True)),
                ('contract_financing', models.CharField(blank=True, max_length=1, null=True)),
                ('contracting_officers_deter', models.CharField(blank=True, max_length=1, null=True)),
                ('cost_accounting_standards', models.CharField(blank=True, max_length=1, null=True)),
                ('country_of_product_or_serv', models.CharField(blank=True, max_length=3, null=True)),
                ('davis_bacon_act', models.CharField(blank=True, max_length=1, null=True)),
                ('evaluated_preference', models.CharField(blank=True, max_length=6, null=True)),
                ('extent_competed', models.CharField(blank=True, max_length=3, null=True)),
                ('fed_biz_opps', models.CharField(blank=True, max_length=1, null=True)),
                ('foreign_funding', models.CharField(blank=True, max_length=1, null=True)),
                ('government_furnished_equip', models.CharField(blank=True, max_length=1, null=True)),
                ('information_technology_com', models.CharField(blank=True, max_length=1, null=True)),
                ('interagency_contracting_au', models.CharField(blank=True, max_length=1, null=True)),
                ('local_area_set_aside', models.CharField(blank=True, max_length=1, null=True)),
                ('major_program', models.CharField(blank=True, max_length=100, null=True)),
                ('purchase_card_as_payment_m', models.CharField(blank=True, max_length=1, null=True)),
                ('multi_year_contract', models.CharField(blank=True, max_length=1, null=True)),
                ('national_interest_action', models.CharField(blank=True, max_length=4, null=True)),
                ('number_of_actions', models.CharField(blank=True, max_length=3, null=True)),
                ('number_of_offers_received', models.CharField(blank=True, max_length=3, null=True)),
                ('other_statutory_authority', models.CharField(blank=True, max_length=1, null=True)),
                ('performance_based_service', models.CharField(blank=True, max_length=1, null=True)),
                ('place_of_manufacture', models.CharField(blank=True, max_length=1, null=True)),
                ('price_evaluation_adjustmen', models.CharField(blank=True, max_length=2, null=True)),
                ('product_or_service_code', models.CharField(blank=True, max_length=4, null=True)),
                ('program_acronym', models.CharField(blank=True, max_length=25, null=True)),
                ('other_than_full_and_open_c', models.CharField(blank=True, max_length=3, null=True)),
                ('recovered_materials_sustai', models.CharField(blank=True, max_length=1, null=True)),
                ('research', models.CharField(blank=True, max_length=3, null=True)),
                ('sea_transportation', models.CharField(blank=True, max_length=1, null=True)),
                ('service_contract_act', models.CharField(blank=True, max_length=1, null=True)),
                ('small_business_competitive', models.CharField(blank=True, max_length=1, null=True)),
                ('solicitation_identifier', models.CharField(blank=True, max_length=25, null=True)),
                ('solicitation_procedures', models.CharField(blank=True, max_length=5, null=True)),
                ('fair_opportunity_limited_s', models.CharField(blank=True, max_length=50, null=True)),
                ('subcontracting_plan', models.CharField(blank=True, max_length=1, null=True)),
                ('program_system_or_equipmen', models.CharField(blank=True, max_length=4, null=True)),
                ('type_set_aside', models.CharField(blank=True, max_length=10, null=True)),
                ('epa_designated_product', models.CharField(blank=True, max_length=1, null=True)),
                ('walsh_healey_act', models.CharField(blank=True, max_length=1, null=True)),
                ('transaction_number', models.CharField(blank=True, max_length=6, null=True)),
                ('referenced_idv_modificatio', models.CharField(blank=True, max_length=1, null=True)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('reporting_period_start', models.DateField(blank=True, null=True)),
                ('reporting_period_end', models.DateField(blank=True, null=True)),
                ('create_user_id', models.CharField(blank=True, max_length=50, null=True)),
                ('update_user_id', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RenameField(
            model_name='award',
            old_name='obligated_amount',
            new_name='total_obligation',
        ),
        migrations.RemoveField(
            model_name='award',
            name='recipient_name',
        ),
        migrations.AddField(
            model_name='award',
            name='description',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='award',
            name='funding_agency',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='references.Agency'),
        ),
        migrations.AddField(
            model_name='award',
            name='latest_submission',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='submissions.SubmissionAttributes'),
        ),
        migrations.AddField(
            model_name='award',
            name='period_of_performance_star',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='award',
            name='recipient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='references.LegalEntity'),
        ),
        migrations.AddField(
            model_name='award',
            name='total_outlay',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='award',
            name='awarding_agency',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='references.Agency'),
        ),
        migrations.AddField(
            model_name='procurement',
            name='award',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='awards.Award'),
        ),
        migrations.AddField(
            model_name='financialassistanceaward',
            name='award',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='awards.Award'),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyawards',
            name='appropriation_account_balances',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.AppropriationAccountBalances'),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyawardstransactionobligations',
            name='financial_accounts_by_awards',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='awards.FinancialAccountsByAwards'),
        ),
    ]
