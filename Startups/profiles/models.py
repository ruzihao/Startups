# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models


class Company_ent(models.Model):
    cid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    company_category_list = models.CharField(max_length=300, blank=True, null=True)
    market = models.CharField(max_length=100, blank=True, null=True)
    funding_total_usd = models.IntegerField(blank=True, null=True)
    funding_rounds = models.CharField(max_length=30, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    country_code = models.CharField(max_length=3, blank=True, null=True)
    state_code = models.CharField(max_length=2, blank=True, null=True)
    region = models.CharField(max_length=80, blank=True, null=True)
    city = models.CharField(max_length=80, blank=True, null=True)
    founded_at = models.DateField(blank=True, null=True)
    first_funding_at = models.DateField(blank=True, null=True)
    last_funding_at = models.DateField(blank=True, null=True)
    homepage = models.CharField(max_length=300, blank=True, null=True)
    company_permalink = models.CharField(max_length=100, blank=True, null=True)
    stock_market = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cb_company'

class Funding_round_ent(models.Model):
    cid = models.ForeignKey('company_ent', related_name='round_company', db_column='cid')
    round_id = models.AutoField(primary_key=True)
    funding_round_type = models.CharField(max_length=30, blank=True, null=True)
    funding_round_code = models.CharField(max_length=5, blank=True, null=True)
    raised_amount_usd = models.IntegerField(blank=True, null=True)
    funded_at = models.DateField(blank=True, null=True)
    funding_round_permalink = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cb_round'

class Funding_ent(models.Model):
    round_id = models.ForeignKey('funding_round_ent', related_name='funding_round', db_column='round_id')
    in_cid = models.AutoField(primary_key=True)
    investor_cid = models.ForeignKey('company_ent', related_name='investor_company', db_column='investor_cid')

    class Meta:
        managed = False
        db_table = 'cb_investment'
		
class Acquisition_ent(models.Model):
    acq_id = models.AutoField(primary_key=True)
    target_cid = models.ForeignKey('company_ent', related_name='target_company', db_column='target_cid')
    acquirer_cid = models.ForeignKey('company_ent', related_name='acquirer_company', db_column='acquirer_cid')
    acquired_at = models.DateField(blank=True, null=True)
    price_amount = models.IntegerField(blank=True, null=True)
    price_currency_code = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cb_acquisition'
		
class Similar_objects_ent(models.Model):
	cid = models.ForeignKey('company_ent', related_name='similarSeed_company')
	score = models.FloatField(blank=True, null=True)
	counterpart = models.ForeignKey('company_ent', related_name='similarObj_company')

class Recommended_objects_ent(models.Model):
	cid = models.ForeignKey('company_ent', related_name='recSeed_company')
	score = models.FloatField(blank=True, null=True)
	counterpart = models.ForeignKey('company_ent', related_name='recObj_company')