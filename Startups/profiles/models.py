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

class company_ent(models.Model):
    cid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    company_category_list = models.CharField(max_length=100, blank=True)
    market = models.CharField(max_length=30, blank=True)
    funding_total_usd = models.IntegerField(blank=True, null=True)
    funding_rounds = models.CharField(max_length=30, blank=True)
    status = models.CharField(max_length=10, blank=True)
    country_code = models.CharField(max_length=3, blank=True)
    state_code = models.CharField(max_length=2, blank=True)
    region = models.CharField(max_length=30, blank=True)
    city = models.CharField(max_length=30, blank=True)
    founded_at = models.DateField(blank=True, null=True)
    first_funding_at = models.DateField(blank=True, null=True)
    last_funding_at = models.DateField(blank=True, null=True)
    homepage = models.CharField(max_length=100, blank=True)
    company_permalink = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = False
        db_table = 'cb_company'
        
class round_ent(models.Model):
    cid = models.ForeignKey(company_ent, db_column='cid')
    round_id = models.IntegerField(primary_key=True)
    funding_round_type = models.CharField(max_length=30, blank=True)
    funding_round_code = models.CharField(max_length=5, blank=True)
    raised_amount_usd = models.IntegerField(blank=True, null=True)
    funded_at = models.DateField(blank=True, null=True)
    funding_round_permalink = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = False
        db_table = 'cb_round'


class investment_ent(models.Model):
    round_id = models.ForeignKey(round_ent, db_column='round_id')
    in_cid = models.IntegerField(primary_key=True)
    investor_cid = models.ForeignKey(company_ent, db_column='investor_cid')

    class Meta:
        managed = False
        db_table = 'cb_investment'


class acquisition_ent(models.Model):
    acq_id = models.IntegerField(primary_key=True)
    target_cid = models.ForeignKey(company_ent, related_name='target_cid')
    acquirer_cid = models.ForeignKey(company_ent, related_name='acquirer_cid')
    acquired_at = models.DateField(blank=True, null=True)
    price_amount = models.IntegerField(blank=True, null=True)
    price_currency_code = models.CharField(max_length=3, blank=True)

    class Meta:
        managed = False
        db_table = 'cb_acquisition'
