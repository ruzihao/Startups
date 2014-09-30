# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class CbCompanies(models.Model):
    id = models.AutoField(primary_key=True)
    company_permalink = models.TextField(blank=True)
    company_name = models.TextField(blank=True)
    company_homepage_url = models.TextField(blank=True)
    company_category_code = models.TextField(blank=True)
    raised_amount_usd = models.TextField(blank=True)
    status = models.TextField(blank=True)
    company_country_code = models.TextField(blank=True)
    company_state_code = models.TextField(blank=True)
    company_region = models.TextField(blank=True)
    company_city = models.TextField(blank=True)
    funding_rounds = models.TextField(blank=True)
    founded_at = models.TextField(blank=True)
    founded_month = models.TextField(blank=True)
    founded_quarter = models.TextField(blank=True)
    founded_year = models.TextField(blank=True)
    first_funding_at = models.TextField(blank=True)
    last_funding_at = models.TextField(blank=True)
    last_milestone_at = models.TextField(blank=True)
    status_score = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'cb_companies'

class CbCompaniesBk(models.Model):
    permalink = models.TextField(blank=True)
    name = models.TextField(blank=True)
    homepage_url = models.TextField(blank=True)
    category_code = models.TextField(blank=True)
    funding_total_usd = models.TextField(blank=True)
    status = models.TextField(blank=True)
    country_code = models.TextField(blank=True)
    state_code = models.TextField(blank=True)
    region = models.TextField(blank=True)
    city = models.TextField(blank=True)
    funding_rounds = models.TextField(blank=True)
    founded_at = models.TextField(blank=True)
    founded_month = models.TextField(blank=True)
    founded_quarter = models.TextField(blank=True)
    founded_year = models.TextField(blank=True)
    first_funding_at = models.TextField(blank=True)
    last_funding_at = models.TextField(blank=True)
    last_milestone_at = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'cb_companies_bk'

class CbCompaniesInvestments(models.Model):
    company_name = models.TextField(blank=True)
    company_category_code = models.TextField(blank=True)
    company_country_code = models.TextField(blank=True)
    company_state_code = models.TextField(blank=True)
    company_region = models.TextField(blank=True)
    company_city = models.TextField(blank=True)
    investor_name = models.TextField(blank=True)
    investor_category_code = models.TextField(blank=True)
    investor_country_code = models.TextField(blank=True)
    investor_state_code = models.TextField(blank=True)
    investor_region = models.TextField(blank=True)
    investor_city = models.TextField(blank=True)
    funding_round_type = models.TextField(blank=True)
    funded_at = models.TextField(blank=True)
    funded_month = models.TextField(blank=True)
    funded_quarter = models.TextField(blank=True)
    funded_year = models.TextField(blank=True)
    raised_amount_usd = models.TextField(blank=True)
    funding_rounds = models.TextField(blank=True)
    founded_at = models.TextField(blank=True)
    founded_month = models.TextField(blank=True)
    founded_quarter = models.TextField(blank=True)
    founded_year = models.TextField(blank=True)
    first_funding_at = models.TextField(blank=True)
    last_funding_at = models.TextField(blank=True)
    last_milestone_at = models.TextField(blank=True)
    status_score = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'cb_companies_investments'

class CbCompaniesInvestments2009(models.Model):
    company_name = models.TextField(blank=True)
    company_category_code = models.TextField(blank=True)
    company_country_code = models.TextField(blank=True)
    company_state_code = models.TextField(blank=True)
    company_region = models.TextField(blank=True)
    company_city = models.TextField(blank=True)
    investor_name = models.TextField(blank=True)
    investor_category_code = models.TextField(blank=True)
    investor_country_code = models.TextField(blank=True)
    investor_state_code = models.TextField(blank=True)
    investor_region = models.TextField(blank=True)
    investor_city = models.TextField(blank=True)
    funding_round_type = models.TextField(blank=True)
    funded_at = models.TextField(blank=True)
    funded_month = models.TextField(blank=True)
    funded_quarter = models.TextField(blank=True)
    funded_year = models.TextField(blank=True)
    raised_amount_usd = models.TextField(blank=True)
    funding_rounds = models.TextField(blank=True)
    founded_at = models.TextField(blank=True)
    founded_month = models.TextField(blank=True)
    founded_quarter = models.TextField(blank=True)
    founded_year = models.TextField(blank=True)
    first_funding_at = models.TextField(blank=True)
    last_funding_at = models.TextField(blank=True)
    last_milestone_at = models.TextField(blank=True)
    cp = models.FloatField(blank=True, null=True)
    cr = models.FloatField(blank=True, null=True)
    actual_score = models.FloatField(blank=True, null=True)
    status_score = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'cb_companies_investments2009'

class CbCompaniesInvestmentsLess(models.Model):
    company_category_code = models.TextField(blank=True)
    company_state_code = models.TextField(blank=True)
    investor_country_code = models.TextField(blank=True)
    investor_state_code = models.TextField(blank=True)
    funding_round_type = models.TextField(blank=True)
    funded_month = models.TextField(blank=True)
    funded_quarter = models.TextField(blank=True)
    funded_year = models.TextField(blank=True)
    raised_amount_usd = models.BigIntegerField(blank=True, null=True)
    funding_rounds = models.IntegerField(blank=True, null=True)
    founded_month = models.TextField(blank=True)
    founded_quarter = models.TextField(blank=True)
    founded_year = models.TextField(blank=True)
    status_score = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'cb_companies_investments_less'

class CbInvestments(models.Model):
    id = models.AutoField(primary_key=True)
    company_permalink = models.TextField(blank=True)
    company_name = models.TextField(blank=True)
    company_category_code = models.TextField(blank=True)
    company_country_code = models.TextField(blank=True)
    company_state_code = models.TextField(blank=True)
    company_region = models.TextField(blank=True)
    company_city = models.TextField(blank=True)
    investor_permalink = models.TextField(blank=True)
    investor_name = models.TextField(blank=True)
    investor_category_code = models.TextField(blank=True)
    investor_country_code = models.TextField(blank=True)
    investor_state_code = models.TextField(blank=True)
    investor_region = models.TextField(blank=True)
    investor_city = models.TextField(blank=True)
    funding_round_type = models.TextField(blank=True)
    funded_at = models.TextField(blank=True)
    funded_month = models.TextField(blank=True)
    funded_quarter = models.TextField(blank=True)
    funded_year = models.TextField(blank=True)
    raised_amount_usd = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'cb_investments'

class CbInvestmentsBk(models.Model):
    company_permalink = models.TextField(blank=True)
    company_name = models.TextField(blank=True)
    company_category_code = models.TextField(blank=True)
    company_country_code = models.TextField(blank=True)
    company_state_code = models.TextField(blank=True)
    company_region = models.TextField(blank=True)
    company_city = models.TextField(blank=True)
    investor_permalink = models.TextField(blank=True)
    investor_name = models.TextField(blank=True)
    investor_category_code = models.TextField(blank=True)
    investor_country_code = models.TextField(blank=True)
    investor_state_code = models.TextField(blank=True)
    investor_region = models.TextField(blank=True)
    investor_city = models.TextField(blank=True)
    funding_round_type = models.TextField(blank=True)
    funded_at = models.TextField(blank=True)
    funded_month = models.TextField(blank=True)
    funded_quarter = models.TextField(blank=True)
    funded_year = models.TextField(blank=True)
    raised_amount_usd = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'cb_investments_bk'

class CbInvestorProfile(models.Model):
    investor_name = models.TextField(blank=True)
    history = models.BigIntegerField()
    performance = models.FloatField(blank=True, null=True)
    risk = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'cb_investor_profile'

class CbRounds(models.Model):
    id = models.AutoField(primary_key=True)
    company_permalink = models.TextField(blank=True)
    company_name = models.TextField(blank=True)
    company_category_code = models.TextField(blank=True)
    company_country_code = models.TextField(blank=True)
    company_state_code = models.TextField(blank=True)
    company_region = models.TextField(blank=True)
    company_city = models.TextField(blank=True)
    funding_round_type = models.TextField(blank=True)
    funded_at = models.TextField(blank=True)
    funded_month = models.TextField(blank=True)
    funded_quarter = models.TextField(blank=True)
    funded_year = models.TextField(blank=True)
    raised_amount_usd = models.TextField(blank=True)
    class Meta:
        managed = True
        db_table = 'cb_rounds'

class CbRoundsBk(models.Model):
    company_permalink = models.TextField(blank=True)
    company_name = models.TextField(blank=True)
    company_category_code = models.TextField(blank=True)
    company_country_code = models.TextField(blank=True)
    company_state_code = models.TextField(blank=True)
    company_region = models.TextField(blank=True)
    company_city = models.TextField(blank=True)
    funding_round_type = models.TextField(blank=True)
    funded_at = models.TextField(blank=True)
    funded_month = models.TextField(blank=True)
    funded_quarter = models.TextField(blank=True)
    funded_year = models.TextField(blank=True)
    raised_amount_usd = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'cb_rounds_bk'

class CbStartUps2007(models.Model):
    name = models.TextField(blank=True)
    cp = models.FloatField(blank=True, null=True)
    cr = models.FloatField(blank=True, null=True)
    actual_score = models.FloatField(blank=True, null=True)
    status_score = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'cb_start_ups2007'

class CbStartUps2008(models.Model):
    name = models.TextField(blank=True)
    cp = models.FloatField(blank=True, null=True)
    cr = models.FloatField(blank=True, null=True)
    actual_score = models.FloatField(blank=True, null=True)
    status_score = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'cb_start_ups2008'

class CbStartUps2009(models.Model):
    name = models.TextField(blank=True)
    cp = models.FloatField(blank=True, null=True)
    cr = models.FloatField(blank=True, null=True)
    actual_score = models.FloatField(blank=True, null=True)
    status_score = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'cb_start_ups2009'

class CbStartUps2010(models.Model):
    name = models.TextField(blank=True)
    cp = models.FloatField(blank=True, null=True)
    cr = models.FloatField(blank=True, null=True)
    estimated_score = models.FloatField(blank=True, null=True)
    status_score = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'cb_start_ups2010'

class CbStartUps2011(models.Model):
    name = models.TextField(blank=True)
    cp = models.FloatField(blank=True, null=True)
    cr = models.FloatField(blank=True, null=True)
    actual_score = models.FloatField(blank=True, null=True)
    status_score = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'cb_start_ups2011'

class CbStartUps2012(models.Model):
    name = models.TextField(blank=True)
    cp = models.FloatField(blank=True, null=True)
    cr = models.FloatField(blank=True, null=True)
    actual_score = models.FloatField(blank=True, null=True)
    status_score = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'cb_start_ups2012'

class EdgarCik(models.Model):
    name = models.TextField(blank=True)
    cik = models.IntegerField(blank=True, null=True)
    sic = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'edgar_cik'

class TmpAddSum(models.Model):
    company_name = models.TextField(blank=True)
    investor_name = models.TextField(blank=True)
    raised_amount_usd = models.TextField(blank=True)
    sum_amount = models.FloatField(blank=True, null=True)
    funded_year = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'tmp_add_sum'

class TmpCompInvest(models.Model):
    company_name = models.TextField(blank=True)
    investor_name = models.TextField(blank=True)
    raised_amount_usd = models.TextField(blank=True)
    status_score = models.IntegerField(blank=True, null=True)
    funded_year = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'tmp_comp_invest'

class TmpCompInvestNew(models.Model):
    company_name = models.TextField(blank=True)
    investor_name = models.TextField(blank=True)
    raised_amount_usd = models.TextField(blank=True)
    status_score = models.IntegerField(blank=True, null=True)
    funded_year = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'tmp_comp_invest_new'

class TmpCompInvestOld(models.Model):
    company_name = models.TextField(blank=True)
    investor_name = models.TextField(blank=True)
    raised_amount_usd = models.TextField(blank=True)
    status_score = models.IntegerField(blank=True, null=True)
    funded_year = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'tmp_comp_invest_old'

class TmpCompanyComp(models.Model):
    company_name = models.TextField(blank=True)
    investor_name = models.TextField(blank=True)
    lambda_field = models.FloatField(db_column='lambda', blank=True, null=True) # Field renamed because it was a Python reserved word.
    funded_year = models.TextField(blank=True)
    history = models.BigIntegerField()
    performance = models.FloatField(blank=True, null=True)
    risk = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'tmp_company_comp'

class TmpInvestor12(models.Model):
    company_name = models.TextField(blank=True)
    inv1 = models.TextField(blank=True)
    inv1_history = models.BigIntegerField()
    inv1_perfomance = models.FloatField(blank=True, null=True)
    inv1_risk = models.FloatField(blank=True, null=True)
    inv1_lambda = models.FloatField(blank=True, null=True)
    inv2 = models.TextField(blank=True)
    inv2_history = models.BigIntegerField()
    inv2_perfomance = models.FloatField(blank=True, null=True)
    inv2_risk = models.FloatField(blank=True, null=True)
    inv2_lambda = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'tmp_investor12'

class TmpInvestor12All(models.Model):
    company_name = models.TextField(blank=True)
    investor_name = models.TextField(blank=True)
    history = models.BigIntegerField()
    performance = models.FloatField(blank=True, null=True)
    risk = models.FloatField(blank=True, null=True)
    lambda_field = models.FloatField(db_column='lambda', blank=True, null=True) # Field renamed because it was a Python reserved word.
    sum_ij = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'tmp_investor12_all'

class TmpInvestor12Cr(models.Model):
    company_name = models.TextField(blank=True)
    cr = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'tmp_investor12_cr'

class TmpInvestor12J(models.Model):
    company_name = models.TextField(blank=True)
    inv1 = models.TextField(blank=True)
    inv1_history = models.BigIntegerField()
    inv1_perfomance = models.FloatField(blank=True, null=True)
    inv1_risk = models.FloatField(blank=True, null=True)
    inv1_lambda = models.FloatField(blank=True, null=True)
    inv2 = models.TextField(blank=True)
    inv2_history = models.BigIntegerField()
    inv2_perfomance = models.FloatField(blank=True, null=True)
    inv2_risk = models.FloatField(blank=True, null=True)
    inv2_lambda = models.FloatField(blank=True, null=True)
    common = models.BigIntegerField()
    j_ik = models.DecimalField(max_digits=24, decimal_places=4, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'tmp_investor12_j'

class TmpJ(models.Model):
    inv1 = models.TextField(blank=True)
    inv2 = models.TextField(blank=True)
    common = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'tmp_j'

class TmpRaised(models.Model):
    company_name = models.TextField(blank=True)
    investor_name = models.TextField(blank=True)
    raised_amount_usd = models.TextField(blank=True)
    status_score = models.IntegerField(blank=True, null=True)
    funded_year = models.TextField(blank=True)
    centered_score = models.DecimalField(max_digits=30, decimal_places=8, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'tmp_raised'

class VbCompetitors(models.Model):
    cid = models.IntegerField(db_column='CID', blank=True, null=True) # Field name made lowercase.
    company = models.CharField(db_column='Company', max_length=255, blank=True) # Field name made lowercase.
    competitors = models.CharField(db_column='Competitors', max_length=255, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'vb_competitors'

class VbFunding(models.Model):
    cid = models.IntegerField(db_column='CID', blank=True, null=True) # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True) # Field name made lowercase.
    fund_type = models.CharField(db_column='Fund_Type', max_length=255, blank=True) # Field name made lowercase.
    fund_date = models.CharField(db_column='Fund_Date', max_length=255, blank=True) # Field name made lowercase.
    investors = models.CharField(db_column='Investors', max_length=255, blank=True) # Field name made lowercase.
    capital_amount = models.CharField(db_column='Capital_Amount', max_length=255, blank=True) # Field name made lowercase.
    post_money = models.CharField(db_column='Post_Money', max_length=255, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'vb_funding'

class VbInfo(models.Model):
    cid = models.IntegerField(db_column='CID', blank=True, null=True) # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True) # Field name made lowercase.
    website = models.CharField(db_column='Website', max_length=255, blank=True) # Field name made lowercase.
    overview = models.TextField(db_column='Overview', blank=True) # Field name made lowercase.
    founded = models.CharField(db_column='Founded', max_length=255, blank=True) # Field name made lowercase.
    employees = models.IntegerField(db_column='Employees', blank=True, null=True) # Field name made lowercase.
    valuation = models.CharField(db_column='Valuation', max_length=255, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'vb_info'

class VbKeyPeople(models.Model):
    cid = models.IntegerField(db_column='CID', blank=True, null=True) # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True) # Field name made lowercase.
    last_name = models.CharField(db_column='Last_Name', max_length=255, blank=True) # Field name made lowercase.
    first_name = models.CharField(db_column='First_Name', max_length=255, blank=True) # Field name made lowercase.
    job_title = models.CharField(db_column='Job_Title', max_length=255, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'vb_key_people'

class WrdsCeos(models.Model):
    ceoage = models.TextField(db_column='CEOAGE', blank=True) # Field name made lowercase.
    ceoallothercomp = models.TextField(db_column='CEOALLOTHERCOMP', blank=True) # Field name made lowercase.
    ceoallothercompensation = models.TextField(db_column='CEOALLOTHERCOMPENSATION', blank=True) # Field name made lowercase.
    ceoalltotalcompensation = models.TextField(db_column='CEOALLTOTALCOMPENSATION', blank=True) # Field name made lowercase.
    ceoannbonusawardmaximumcash = models.TextField(db_column='CEOANNBONUSAWARDMAXIMUMCASH', blank=True) # Field name made lowercase.
    ceoannbonusawardmaximumothersca0 = models.TextField(db_column='CEOANNBONUSAWARDMAXIMUMOTHERSCA0', blank=True) # Field name made lowercase.
    ceoannbonusawardmaximumothersca1 = models.TextField(db_column='CEOANNBONUSAWARDMAXIMUMOTHERSCA1', blank=True) # Field name made lowercase.
    ceoannbonusawardmaximumothersca2 = models.TextField(db_column='CEOANNBONUSAWARDMAXIMUMOTHERSCA2', blank=True) # Field name made lowercase.
    ceoannbonusawardmaximumotherscas = models.TextField(db_column='CEOANNBONUSAWARDMAXIMUMOTHERSCAS', blank=True) # Field name made lowercase.
    ceoannbonusawardmaximumotherspe0 = models.TextField(db_column='CEOANNBONUSAWARDMAXIMUMOTHERSPE0', blank=True) # Field name made lowercase.
    ceoannbonusawardmaximumotherspe1 = models.TextField(db_column='CEOANNBONUSAWARDMAXIMUMOTHERSPE1', blank=True) # Field name made lowercase.
    ceoannbonusawardmaximumotherspe2 = models.TextField(db_column='CEOANNBONUSAWARDMAXIMUMOTHERSPE2', blank=True) # Field name made lowercase.
    ceoannbonusawardmaximumothersper = models.TextField(db_column='CEOANNBONUSAWARDMAXIMUMOTHERSPER', blank=True) # Field name made lowercase.
    ceoannbonusawardmaximumpercentag = models.TextField(db_column='CEOANNBONUSAWARDMAXIMUMPERCENTAG', blank=True) # Field name made lowercase.
    ceoannbonuscomments = models.TextField(db_column='CEOANNBONUSCOMMENTS', blank=True) # Field name made lowercase.
    ceoannbonusdeferredscheme = models.TextField(db_column='CEOANNBONUSDEFERREDSCHEME', blank=True) # Field name made lowercase.
    ceoannbonusdeferredschemedeferra = models.TextField(db_column='CEOANNBONUSDEFERREDSCHEMEDEFERRA', blank=True) # Field name made lowercase.
    ceoannbonusdeferredschememandato = models.TextField(db_column='CEOANNBONUSDEFERREDSCHEMEMANDATO', blank=True) # Field name made lowercase.
    ceoannbonusdeferredschemematchin = models.TextField(db_column='CEOANNBONUSDEFERREDSCHEMEMATCHIN', blank=True) # Field name made lowercase.
    ceoannbonusdeferredschememaximum = models.TextField(db_column='CEOANNBONUSDEFERREDSCHEMEMAXIMUM', blank=True) # Field name made lowercase.
    ceoannbonusdeferredschemesharepr = models.TextField(db_column='CEOANNBONUSDEFERREDSCHEMESHAREPR', blank=True) # Field name made lowercase.
    ceoannbonuspaymentform = models.TextField(db_column='CEOANNBONUSPAYMENTFORM', blank=True) # Field name made lowercase.
    ceoannbonuspaymentformconditions = models.TextField(db_column='CEOANNBONUSPAYMENTFORMCONDITIONS', blank=True) # Field name made lowercase.
    ceoannbonuspaymentformother = models.TextField(db_column='CEOANNBONUSPAYMENTFORMOTHER', blank=True) # Field name made lowercase.
    ceoannbonuspayments = models.TextField(db_column='CEOANNBONUSPAYMENTS', blank=True) # Field name made lowercase.
    ceoannbonusperfmeasuresdiscretio = models.TextField(db_column='CEOANNBONUSPERFMEASURESDISCRETIO', blank=True) # Field name made lowercase.
    ceoannbonusperfmeasuresgenericli = models.TextField(db_column='CEOANNBONUSPERFMEASURESGENERICLI', blank=True) # Field name made lowercase.
    ceoannbonusperfmeasuresusedinye0 = models.TextField(db_column='CEOANNBONUSPERFMEASURESUSEDINYE0', blank=True) # Field name made lowercase.
    ceoannbonusperfmeasuresusedinye1 = models.TextField(db_column='CEOANNBONUSPERFMEASURESUSEDINYE1', blank=True) # Field name made lowercase.
    ceoannbonusperfmeasuresusedinye2 = models.TextField(db_column='CEOANNBONUSPERFMEASURESUSEDINYE2', blank=True) # Field name made lowercase.
    ceoannbonusperfmeasuresusedinye3 = models.TextField(db_column='CEOANNBONUSPERFMEASURESUSEDINYE3', blank=True) # Field name made lowercase.
    ceoannbonusperfmeasuresusedinyea = models.TextField(db_column='CEOANNBONUSPERFMEASURESUSEDINYEA', blank=True) # Field name made lowercase.
    ceoannbonustargetcash = models.TextField(db_column='CEOANNBONUSTARGETCASH', blank=True) # Field name made lowercase.
    ceoannbonustargetotherscash1 = models.TextField(db_column='CEOANNBONUSTARGETOTHERSCASH1', blank=True) # Field name made lowercase.
    ceoannbonustargetotherscash2 = models.TextField(db_column='CEOANNBONUSTARGETOTHERSCASH2', blank=True) # Field name made lowercase.
    ceoannbonustargetotherscash3 = models.TextField(db_column='CEOANNBONUSTARGETOTHERSCASH3', blank=True) # Field name made lowercase.
    ceoannbonustargetotherspercenta0 = models.TextField(db_column='CEOANNBONUSTARGETOTHERSPERCENTA0', blank=True) # Field name made lowercase.
    ceoannbonustargetotherspercenta1 = models.TextField(db_column='CEOANNBONUSTARGETOTHERSPERCENTA1', blank=True) # Field name made lowercase.
    ceoannbonustargetotherspercenta2 = models.TextField(db_column='CEOANNBONUSTARGETOTHERSPERCENTA2', blank=True) # Field name made lowercase.
    ceoannbonustargetotherspercentag = models.TextField(db_column='CEOANNBONUSTARGETOTHERSPERCENTAG', blank=True) # Field name made lowercase.
    ceoannbonustargetpercentage = models.TextField(db_column='CEOANNBONUSTARGETPERCENTAGE', blank=True) # Field name made lowercase.
    ceoannbonusyrachievements = models.TextField(db_column='CEOANNBONUSYRACHIEVEMENTS', blank=True) # Field name made lowercase.
    ceoannualbonus = models.TextField(db_column='CEOANNUALBONUS', blank=True) # Field name made lowercase.
    ceoannualoptiongrant1 = models.TextField(db_column='CEOANNUALOPTIONGRANT1', blank=True) # Field name made lowercase.
    ceoannualoptiongrant2 = models.TextField(db_column='CEOANNUALOPTIONGRANT2', blank=True) # Field name made lowercase.
    ceoannualoptiongrant3 = models.TextField(db_column='CEOANNUALOPTIONGRANT3', blank=True) # Field name made lowercase.
    ceoannualoptiongrant4 = models.TextField(db_column='CEOANNUALOPTIONGRANT4', blank=True) # Field name made lowercase.
    ceoannualoptiongrant5 = models.TextField(db_column='CEOANNUALOPTIONGRANT5', blank=True) # Field name made lowercase.
    ceoannualoptiongrant6 = models.TextField(db_column='CEOANNUALOPTIONGRANT6', blank=True) # Field name made lowercase.
    ceoannualoptiongrantblackschole0 = models.TextField(db_column='CEOANNUALOPTIONGRANTBLACKSCHOLE0', blank=True) # Field name made lowercase.
    ceoannualoptiongrantblackschole1 = models.TextField(db_column='CEOANNUALOPTIONGRANTBLACKSCHOLE1', blank=True) # Field name made lowercase.
    ceoannualoptiongrantblackschole2 = models.TextField(db_column='CEOANNUALOPTIONGRANTBLACKSCHOLE2', blank=True) # Field name made lowercase.
    ceoannualoptiongrantblackschole3 = models.TextField(db_column='CEOANNUALOPTIONGRANTBLACKSCHOLE3', blank=True) # Field name made lowercase.
    ceoannualoptiongrantblackschole4 = models.TextField(db_column='CEOANNUALOPTIONGRANTBLACKSCHOLE4', blank=True) # Field name made lowercase.
    ceoannualoptiongrantblackscholes = models.TextField(db_column='CEOANNUALOPTIONGRANTBLACKSCHOLES', blank=True) # Field name made lowercase.
    ceoannualoptiongrantexercisepri0 = models.TextField(db_column='CEOANNUALOPTIONGRANTEXERCISEPRI0', blank=True) # Field name made lowercase.
    ceoannualoptiongrantexercisepri1 = models.TextField(db_column='CEOANNUALOPTIONGRANTEXERCISEPRI1', blank=True) # Field name made lowercase.
    ceoannualoptiongrantexercisepri2 = models.TextField(db_column='CEOANNUALOPTIONGRANTEXERCISEPRI2', blank=True) # Field name made lowercase.
    ceoannualoptiongrantexercisepri3 = models.TextField(db_column='CEOANNUALOPTIONGRANTEXERCISEPRI3', blank=True) # Field name made lowercase.
    ceoannualoptiongrantexercisepri4 = models.TextField(db_column='CEOANNUALOPTIONGRANTEXERCISEPRI4', blank=True) # Field name made lowercase.
    ceoannualoptiongrantexercisepric = models.TextField(db_column='CEOANNUALOPTIONGRANTEXERCISEPRIC', blank=True) # Field name made lowercase.
    ceoannualoptiongrantpctgoftotal0 = models.TextField(db_column='CEOANNUALOPTIONGRANTPCTGOFTOTAL0', blank=True) # Field name made lowercase.
    ceoannualoptiongrantpctgoftotal1 = models.TextField(db_column='CEOANNUALOPTIONGRANTPCTGOFTOTAL1', blank=True) # Field name made lowercase.
    ceoannualoptiongrantpctgoftotal2 = models.TextField(db_column='CEOANNUALOPTIONGRANTPCTGOFTOTAL2', blank=True) # Field name made lowercase.
    ceoannualoptiongrantpctgoftotal3 = models.TextField(db_column='CEOANNUALOPTIONGRANTPCTGOFTOTAL3', blank=True) # Field name made lowercase.
    ceoannualoptiongrantpctgoftotal4 = models.TextField(db_column='CEOANNUALOPTIONGRANTPCTGOFTOTAL4', blank=True) # Field name made lowercase.
    ceoannualoptiongrantpctgoftotalg = models.TextField(db_column='CEOANNUALOPTIONGRANTPCTGOFTOTALG', blank=True) # Field name made lowercase.
    ceobasesalary = models.TextField(db_column='CEOBASESALARY', blank=True) # Field name made lowercase.
    ceobonus = models.TextField(db_column='CEOBONUS', blank=True) # Field name made lowercase.
    ceocompensationreviewcompensatio = models.TextField(db_column='CEOCOMPENSATIONREVIEWCOMPENSATIO', blank=True) # Field name made lowercase.
    ceocompensationreviewsalaryincre = models.TextField(db_column='CEOCOMPENSATIONREVIEWSALARYINCRE', blank=True) # Field name made lowercase.
    ceocompensationreviewsalarysetti = models.TextField(db_column='CEOCOMPENSATIONREVIEWSALARYSETTI', blank=True) # Field name made lowercase.
    ceocompensationreviewtotalcompen = models.TextField(db_column='CEOCOMPENSATIONREVIEWTOTALCOMPEN', blank=True) # Field name made lowercase.
    ceocompensationyear = models.TextField(db_column='CEOCOMPENSATIONYEAR', blank=True) # Field name made lowercase.
    ceocomphighlights = models.TextField(db_column='CEOCOMPHIGHLIGHTS', blank=True) # Field name made lowercase.
    ceocontractincentivelatestyeara0 = models.TextField(db_column='CEOCONTRACTINCENTIVELATESTYEARA0', blank=True) # Field name made lowercase.
    ceocontractincentivelatestyeara1 = models.TextField(db_column='CEOCONTRACTINCENTIVELATESTYEARA1', blank=True) # Field name made lowercase.
    ceocontractincentivelatestyeara2 = models.TextField(db_column='CEOCONTRACTINCENTIVELATESTYEARA2', blank=True) # Field name made lowercase.
    ceocontractincentivelatestyeara3 = models.TextField(db_column='CEOCONTRACTINCENTIVELATESTYEARA3', blank=True) # Field name made lowercase.
    ceocontractincentivelatestyearac = models.TextField(db_column='CEOCONTRACTINCENTIVELATESTYEARAC', blank=True) # Field name made lowercase.
    ceocontractincentivelatestyearaw = models.TextField(db_column='CEOCONTRACTINCENTIVELATESTYEARAW', blank=True) # Field name made lowercase.
    ceocontractincentivenotes = models.TextField(db_column='CEOCONTRACTINCENTIVENOTES', blank=True) # Field name made lowercase.
    ceocontractincentivespecialawar0 = models.TextField(db_column='CEOCONTRACTINCENTIVESPECIALAWAR0', blank=True) # Field name made lowercase.
    ceocontractincentivespecialawar1 = models.TextField(db_column='CEOCONTRACTINCENTIVESPECIALAWAR1', blank=True) # Field name made lowercase.
    ceocontractincentivespecialawar2 = models.TextField(db_column='CEOCONTRACTINCENTIVESPECIALAWAR2', blank=True) # Field name made lowercase.
    ceocontractincentivespecialaward = models.TextField(db_column='CEOCONTRACTINCENTIVESPECIALAWARD', blank=True) # Field name made lowercase.
    ceocontractminimumbasicsalary = models.TextField(db_column='CEOCONTRACTMINIMUMBASICSALARY', blank=True) # Field name made lowercase.
    ceocontractsalaryformerceo_chair = models.TextField(db_column='CEOCONTRACTSALARYFORMERCEO_CHAIR', blank=True) # Field name made lowercase.
    ceocontractsalarylatestincrease = models.TextField(db_column='CEOCONTRACTSALARYLATESTINCREASE', blank=True) # Field name made lowercase.
    ceocontractsalarynotes = models.TextField(db_column='CEOCONTRACTSALARYNOTES', blank=True) # Field name made lowercase.
    ceocontractsalaryratelastyear = models.TextField(db_column='CEOCONTRACTSALARYRATELASTYEAR', blank=True) # Field name made lowercase.
    ceocontractsalaryratethisyear = models.TextField(db_column='CEOCONTRACTSALARYRATETHISYEAR', blank=True) # Field name made lowercase.
    ceocontractsalarysetting = models.TextField(db_column='CEOCONTRACTSALARYSETTING', blank=True) # Field name made lowercase.
    ceocontractseverancebenefitconti = models.TextField(db_column='CEOCONTRACTSEVERANCEBENEFITCONTI', blank=True) # Field name made lowercase.
    ceocontractseverancebonuscontinu = models.TextField(db_column='CEOCONTRACTSEVERANCEBONUSCONTINU', blank=True) # Field name made lowercase.
    ceocontractseverancechangeofcon0 = models.TextField(db_column='CEOCONTRACTSEVERANCECHANGEOFCON0', blank=True) # Field name made lowercase.
    ceocontractseverancechangeofcon1 = models.TextField(db_column='CEOCONTRACTSEVERANCECHANGEOFCON1', blank=True) # Field name made lowercase.
    ceocontractseverancechangeofcon2 = models.TextField(db_column='CEOCONTRACTSEVERANCECHANGEOFCON2', blank=True) # Field name made lowercase.
    ceocontractseverancechangeofcon3 = models.TextField(db_column='CEOCONTRACTSEVERANCECHANGEOFCON3', blank=True) # Field name made lowercase.
    ceocontractseverancechangeofcon4 = models.TextField(db_column='CEOCONTRACTSEVERANCECHANGEOFCON4', blank=True) # Field name made lowercase.
    ceocontractseverancechangeofcon5 = models.TextField(db_column='CEOCONTRACTSEVERANCECHANGEOFCON5', blank=True) # Field name made lowercase.
    ceocontractseverancechangeofcon6 = models.TextField(db_column='CEOCONTRACTSEVERANCECHANGEOFCON6', blank=True) # Field name made lowercase.
    ceocontractseverancechangeofcon7 = models.TextField(db_column='CEOCONTRACTSEVERANCECHANGEOFCON7', blank=True) # Field name made lowercase.
    ceocontractseverancechangeofcont = models.TextField(db_column='CEOCONTRACTSEVERANCECHANGEOFCONT', blank=True) # Field name made lowercase.
    ceocontractseveranceequityaward0 = models.TextField(db_column='CEOCONTRACTSEVERANCEEQUITYAWARD0', blank=True) # Field name made lowercase.
    ceocontractseveranceequityaward1 = models.TextField(db_column='CEOCONTRACTSEVERANCEEQUITYAWARD1', blank=True) # Field name made lowercase.
    ceocontractseveranceequityawards = models.TextField(db_column='CEOCONTRACTSEVERANCEEQUITYAWARDS', blank=True) # Field name made lowercase.
    ceocontractseverancenotes = models.TextField(db_column='CEOCONTRACTSEVERANCENOTES', blank=True) # Field name made lowercase.
    ceocontractseveranceother = models.TextField(db_column='CEOCONTRACTSEVERANCEOTHER', blank=True) # Field name made lowercase.
    ceocontractseverancesalarycontin = models.TextField(db_column='CEOCONTRACTSEVERANCESALARYCONTIN', blank=True) # Field name made lowercase.
    ceoexercisableoptions = models.TextField(db_column='CEOEXERCISABLEOPTIONS', blank=True) # Field name made lowercase.
    ceofname = models.TextField(db_column='CEOFNAME', blank=True) # Field name made lowercase.
    ceofnameco = models.TextField(db_column='CEOFNAMECO', blank=True) # Field name made lowercase.
    ceohascontract = models.TextField(db_column='CEOHASCONTRACT', blank=True) # Field name made lowercase.
    ceohireyr = models.TextField(db_column='CEOHIREYR', blank=True) # Field name made lowercase.
    ceoischairman = models.TextField(db_column='CEOISCHAIRMAN', blank=True) # Field name made lowercase.
    ceolname = models.TextField(db_column='CEOLNAME', blank=True) # Field name made lowercase.
    ceolnameco = models.TextField(db_column='CEOLNAMECO', blank=True) # Field name made lowercase.
    ceoltipawardedinyear = models.TextField(db_column='CEOLTIPAWARDEDINYEAR', blank=True) # Field name made lowercase.
    ceoltipawardedinyearoptionexchan = models.TextField(db_column='CEOLTIPAWARDEDINYEAROPTIONEXCHAN', blank=True) # Field name made lowercase.
    ceoltipawardedinyearoptionrepric = models.TextField(db_column='CEOLTIPAWARDEDINYEAROPTIONREPRIC', blank=True) # Field name made lowercase.
    ceoltipawardedinyearoptionshave0 = models.TextField(db_column='CEOLTIPAWARDEDINYEAROPTIONSHAVE0', blank=True) # Field name made lowercase.
    ceoltipawardedinyearoptionshave1 = models.TextField(db_column='CEOLTIPAWARDEDINYEAROPTIONSHAVE1', blank=True) # Field name made lowercase.
    ceoltipawardedinyearoptionshave2 = models.TextField(db_column='CEOLTIPAWARDEDINYEAROPTIONSHAVE2', blank=True) # Field name made lowercase.
    ceoltipawardedinyearoptionshave3 = models.TextField(db_column='CEOLTIPAWARDEDINYEAROPTIONSHAVE3', blank=True) # Field name made lowercase.
    ceoltipawardedinyearoptionshave4 = models.TextField(db_column='CEOLTIPAWARDEDINYEAROPTIONSHAVE4', blank=True) # Field name made lowercase.
    ceoltipawardedinyearoptionshave5 = models.TextField(db_column='CEOLTIPAWARDEDINYEAROPTIONSHAVE5', blank=True) # Field name made lowercase.
    ceoltipawardedinyearoptionshaveb = models.TextField(db_column='CEOLTIPAWARDEDINYEAROPTIONSHAVEB', blank=True) # Field name made lowercase.
    ceoltipcomments = models.TextField(db_column='CEOLTIPCOMMENTS', blank=True) # Field name made lowercase.
    ceoltipdividends = models.TextField(db_column='CEOLTIPDIVIDENDS', blank=True) # Field name made lowercase.
    ceoltipmaximumperf = models.TextField(db_column='CEOLTIPMAXIMUMPERF', blank=True) # Field name made lowercase.
    ceoltipmaxpayablecash = models.TextField(db_column='CEOLTIPMAXPAYABLECASH', blank=True) # Field name made lowercase.
    ceoltipmaxpayableother = models.TextField(db_column='CEOLTIPMAXPAYABLEOTHER', blank=True) # Field name made lowercase.
    ceoltipmaxpayablerestrictedstock = models.TextField(db_column='CEOLTIPMAXPAYABLERESTRICTEDSTOCK', blank=True) # Field name made lowercase.
    ceoltipmaxpayablestockoptions = models.TextField(db_column='CEOLTIPMAXPAYABLESTOCKOPTIONS', blank=True) # Field name made lowercase.
    ceoltipoptiondeferredvestingper0 = models.TextField(db_column='CEOLTIPOPTIONDEFERREDVESTINGPER0', blank=True) # Field name made lowercase.
    ceoltipoptiondeferredvestingper1 = models.TextField(db_column='CEOLTIPOPTIONDEFERREDVESTINGPER1', blank=True) # Field name made lowercase.
    ceoltipoptiondeferredvestingperi = models.TextField(db_column='CEOLTIPOPTIONDEFERREDVESTINGPERI', blank=True) # Field name made lowercase.
    ceoltipoptionexpirationperiod1 = models.TextField(db_column='CEOLTIPOPTIONEXPIRATIONPERIOD1', blank=True) # Field name made lowercase.
    ceoltipoptionexpirationperiod2 = models.TextField(db_column='CEOLTIPOPTIONEXPIRATIONPERIOD2', blank=True) # Field name made lowercase.
    ceoltipoptionmeasures1 = models.TextField(db_column='CEOLTIPOPTIONMEASURES1', blank=True) # Field name made lowercase.
    ceoltipoptionmeasures2 = models.TextField(db_column='CEOLTIPOPTIONMEASURES2', blank=True) # Field name made lowercase.
    ceoltipoptionvestingfrequency1 = models.TextField(db_column='CEOLTIPOPTIONVESTINGFREQUENCY1', blank=True) # Field name made lowercase.
    ceoltipoptionvestingfrequency2 = models.TextField(db_column='CEOLTIPOPTIONVESTINGFREQUENCY2', blank=True) # Field name made lowercase.
    ceoltipoptionvestingperiod1 = models.TextField(db_column='CEOLTIPOPTIONVESTINGPERIOD1', blank=True) # Field name made lowercase.
    ceoltipoptionvestingperiod2 = models.TextField(db_column='CEOLTIPOPTIONVESTINGPERIOD2', blank=True) # Field name made lowercase.
    ceoltipoptionvestingrate1 = models.TextField(db_column='CEOLTIPOPTIONVESTINGRATE1', blank=True) # Field name made lowercase.
    ceoltipoptionvestingrate2 = models.TextField(db_column='CEOLTIPOPTIONVESTINGRATE2', blank=True) # Field name made lowercase.
    ceoltipownershipguidelinesceo = models.TextField(db_column='CEOLTIPOWNERSHIPGUIDELINESCEO', blank=True) # Field name made lowercase.
    ceoltipownershipguidelinesceonum = models.TextField(db_column='CEOLTIPOWNERSHIPGUIDELINESCEONUM', blank=True) # Field name made lowercase.
    ceoltipownershipguidelineschair0 = models.TextField(db_column='CEOLTIPOWNERSHIPGUIDELINESCHAIR0', blank=True) # Field name made lowercase.
    ceoltipownershipguidelineschair1 = models.TextField(db_column='CEOLTIPOWNERSHIPGUIDELINESCHAIR1', blank=True) # Field name made lowercase.
    ceoltipownershipguidelineschairm = models.TextField(db_column='CEOLTIPOWNERSHIPGUIDELINESCHAIRM', blank=True) # Field name made lowercase.
    ceoltipownershipguidelinescoo_c0 = models.TextField(db_column='CEOLTIPOWNERSHIPGUIDELINESCOO_C0', blank=True) # Field name made lowercase.
    ceoltipownershipguidelinescoo_c1 = models.TextField(db_column='CEOLTIPOWNERSHIPGUIDELINESCOO_C1', blank=True) # Field name made lowercase.
    ceoltipownershipguidelinescoo_cf = models.TextField(db_column='CEOLTIPOWNERSHIPGUIDELINESCOO_CF', blank=True) # Field name made lowercase.
    ceoltipownershipguidelinesnotes = models.TextField(db_column='CEOLTIPOWNERSHIPGUIDELINESNOTES', blank=True) # Field name made lowercase.
    ceoltipownershipguidelinesother1 = models.TextField(db_column='CEOLTIPOWNERSHIPGUIDELINESOTHER1', blank=True) # Field name made lowercase.
    ceoltipownershipguidelinesother2 = models.TextField(db_column='CEOLTIPOWNERSHIPGUIDELINESOTHER2', blank=True) # Field name made lowercase.
    ceoltipownershipguidelinesother3 = models.TextField(db_column='CEOLTIPOWNERSHIPGUIDELINESOTHER3', blank=True) # Field name made lowercase.
    ceoltippaymentform = models.TextField(db_column='CEOLTIPPAYMENTFORM', blank=True) # Field name made lowercase.
    ceoltippaymentformother = models.TextField(db_column='CEOLTIPPAYMENTFORMOTHER', blank=True) # Field name made lowercase.
    ceoltippayout = models.TextField(db_column='CEOLTIPPAYOUT', blank=True) # Field name made lowercase.
    ceoltipperfmeasurescorporate1 = models.TextField(db_column='CEOLTIPPERFMEASURESCORPORATE1', blank=True) # Field name made lowercase.
    ceoltipperfmeasurescorporate2 = models.TextField(db_column='CEOLTIPPERFMEASURESCORPORATE2', blank=True) # Field name made lowercase.
    ceoltipperfmeasurescorporate3 = models.TextField(db_column='CEOLTIPPERFMEASURESCORPORATE3', blank=True) # Field name made lowercase.
    ceoltipperfmeasuresgenericlist = models.TextField(db_column='CEOLTIPPERFMEASURESGENERICLIST', blank=True) # Field name made lowercase.
    ceoltipperfmeasuresother = models.TextField(db_column='CEOLTIPPERFMEASURESOTHER', blank=True) # Field name made lowercase.
    ceoltipperfmeasuresperformancepe = models.TextField(db_column='CEOLTIPPERFMEASURESPERFORMANCEPE', blank=True) # Field name made lowercase.
    ceoltiprestrictionperiod = models.TextField(db_column='CEOLTIPRESTRICTIONPERIOD', blank=True) # Field name made lowercase.
    ceoltipretentionperiod = models.TextField(db_column='CEOLTIPRETENTIONPERIOD', blank=True) # Field name made lowercase.
    ceoltiptargetpayable = models.TextField(db_column='CEOLTIPTARGETPAYABLE', blank=True) # Field name made lowercase.
    ceoltiptargetperf = models.TextField(db_column='CEOLTIPTARGETPERF', blank=True) # Field name made lowercase.
    ceoltipthresholdperf = models.TextField(db_column='CEOLTIPTHRESHOLDPERF', blank=True) # Field name made lowercase.
    ceoltiptotsharesreservedaddition = models.TextField(db_column='CEOLTIPTOTSHARESRESERVEDADDITION', blank=True) # Field name made lowercase.
    ceoltiptotsharesreserveddilution = models.TextField(db_column='CEOLTIPTOTSHARESRESERVEDDILUTION', blank=True) # Field name made lowercase.
    ceoltiptotsharesreservedscheme1 = models.TextField(db_column='CEOLTIPTOTSHARESRESERVEDSCHEME1', blank=True) # Field name made lowercase.
    ceoltiptotsharesreservedscheme2 = models.TextField(db_column='CEOLTIPTOTSHARESRESERVEDSCHEME2', blank=True) # Field name made lowercase.
    ceoltiptotsharesreservedscheme3 = models.TextField(db_column='CEOLTIPTOTSHARESRESERVEDSCHEME3', blank=True) # Field name made lowercase.
    ceoltiptotsharesreservedscheme4 = models.TextField(db_column='CEOLTIPTOTSHARESRESERVEDSCHEME4', blank=True) # Field name made lowercase.
    ceoltiptotsharesreservedtotal = models.TextField(db_column='CEOLTIPTOTSHARESRESERVEDTOTAL', blank=True) # Field name made lowercase.
    ceoltiptotsharesreservedyearofla = models.TextField(db_column='CEOLTIPTOTSHARESRESERVEDYEAROFLA', blank=True) # Field name made lowercase.
    ceoltipvestedinyear = models.TextField(db_column='CEOLTIPVESTEDINYEAR', blank=True) # Field name made lowercase.
    ceoltipyrachievements = models.TextField(db_column='CEOLTIPYRACHIEVEMENTS', blank=True) # Field name made lowercase.
    ceononeqincentcomp = models.TextField(db_column='CEONONEQINCENTCOMP', blank=True) # Field name made lowercase.
    ceonumberofoptionsexercised = models.TextField(db_column='CEONUMBEROFOPTIONSEXERCISED', blank=True) # Field name made lowercase.
    ceooptionawards = models.TextField(db_column='CEOOPTIONAWARDS', blank=True) # Field name made lowercase.
    ceooptionawards_gdv = models.TextField(db_column='CEOOPTIONAWARDS_GDV', blank=True) # Field name made lowercase.
    ceooptionvaluerealized = models.TextField(db_column='CEOOPTIONVALUEREALIZED', blank=True) # Field name made lowercase.
    ceootherannualcomp = models.TextField(db_column='CEOOTHERANNUALCOMP', blank=True) # Field name made lowercase.
    ceopeerpaycompanydescription = models.TextField(db_column='CEOPEERPAYCOMPANYDESCRIPTION', blank=True) # Field name made lowercase.
    ceopeerpaycompanylist = models.TextField(db_column='CEOPEERPAYCOMPANYLIST', blank=True) # Field name made lowercase.
    ceopeerpayindex = models.TextField(db_column='CEOPEERPAYINDEX', blank=True) # Field name made lowercase.
    ceopeerpaysurveys_consultants = models.TextField(db_column='CEOPEERPAYSURVEYS_CONSULTANTS', blank=True) # Field name made lowercase.
    ceopeerperfincentiveschemecompan = models.TextField(db_column='CEOPEERPERFINCENTIVESCHEMECOMPAN', blank=True) # Field name made lowercase.
    ceopeerperfincentiveschemeindex = models.TextField(db_column='CEOPEERPERFINCENTIVESCHEMEINDEX', blank=True) # Field name made lowercase.
    ceopeerperftsrgraphcompanylist = models.TextField(db_column='CEOPEERPERFTSRGRAPHCOMPANYLIST', blank=True) # Field name made lowercase.
    ceopeerperftsrgraphindex = models.TextField(db_column='CEOPEERPERFTSRGRAPHINDEX', blank=True) # Field name made lowercase.
    ceopensionnqdc = models.TextField(db_column='CEOPENSIONNQDC', blank=True) # Field name made lowercase.
    ceorestrictedstock = models.TextField(db_column='CEORESTRICTEDSTOCK', blank=True) # Field name made lowercase.
    ceosharesheld = models.TextField(db_column='CEOSHARESHELD', blank=True) # Field name made lowercase.
    ceosharesheld1yrincrpct = models.TextField(db_column='CEOSHARESHELD1YRINCRPCT', blank=True) # Field name made lowercase.
    ceosharesheldlastyear = models.TextField(db_column='CEOSHARESHELDLASTYEAR', blank=True) # Field name made lowercase.
    ceosharesheldvtpwrpct = models.TextField(db_column='CEOSHARESHELDVTPWRPCT', blank=True) # Field name made lowercase.
    ceosharestopaymultiple = models.TextField(db_column='CEOSHARESTOPAYMULTIPLE', blank=True) # Field name made lowercase.
    ceostockawards = models.TextField(db_column='CEOSTOCKAWARDS', blank=True) # Field name made lowercase.
    ceostockawards_gdv = models.TextField(db_column='CEOSTOCKAWARDS_GDV', blank=True) # Field name made lowercase.
    ceosummaryblackscholesvalue = models.TextField(db_column='CEOSUMMARYBLACKSCHOLESVALUE', blank=True) # Field name made lowercase.
    ceosummarytclblackscholesvalue = models.TextField(db_column='CEOSUMMARYTCLBLACKSCHOLESVALUE', blank=True) # Field name made lowercase.
    ceotenure = models.TextField(db_column='CEOTENURE', blank=True) # Field name made lowercase.
    ceototactcomp = models.TextField(db_column='CEOTOTACTCOMP', blank=True) # Field name made lowercase.
    ceototalannualcomp = models.TextField(db_column='CEOTOTALANNUALCOMP', blank=True) # Field name made lowercase.
    ceototaltargetcomp = models.TextField(db_column='CEOTOTALTARGETCOMP', blank=True) # Field name made lowercase.
    ceototanncomp = models.TextField(db_column='CEOTOTANNCOMP', blank=True) # Field name made lowercase.
    ceototsumcomp = models.TextField(db_column='CEOTOTSUMCOMP', blank=True) # Field name made lowercase.
    ceounexercisableoptions = models.TextField(db_column='CEOUNEXERCISABLEOPTIONS', blank=True) # Field name made lowercase.
    ceovalueofexercisableoptions = models.TextField(db_column='CEOVALUEOFEXERCISABLEOPTIONS', blank=True) # Field name made lowercase.
    ceovalueofunexercisableoptions = models.TextField(db_column='CEOVALUEOFUNEXERCISABLEOPTIONS', blank=True) # Field name made lowercase.
    ceovariablepayasstock = models.TextField(db_column='CEOVARIABLEPAYASSTOCK', blank=True) # Field name made lowercase.
    ceovariabletototalpaymultiple = models.TextField(db_column='CEOVARIABLETOTOTALPAYMULTIPLE', blank=True) # Field name made lowercase.
    ceovariabletpm = models.TextField(db_column='CEOVARIABLETPM', blank=True) # Field name made lowercase.
    companyname = models.TextField(db_column='COMPANYNAME', blank=True) # Field name made lowercase.
    dirage = models.TextField(db_column='DIRAGE', blank=True) # Field name made lowercase.
    dirfname = models.TextField(db_column='DIRFNAME', blank=True) # Field name made lowercase.
    dirlname = models.TextField(db_column='DIRLNAME', blank=True) # Field name made lowercase.
    dirtenure = models.TextField(db_column='DIRTENURE', blank=True) # Field name made lowercase.
    notesceocontract = models.TextField(db_column='NOTESCEOCONTRACT', blank=True) # Field name made lowercase.
    notesceocontractcorporateaircraf = models.TextField(db_column='NOTESCEOCONTRACTCORPORATEAIRCRAF', blank=True) # Field name made lowercase.
    notesceocontractexpirationdate = models.TextField(db_column='NOTESCEOCONTRACTEXPIRATIONDATE', blank=True) # Field name made lowercase.
    notesceocontractfixedterm = models.TextField(db_column='NOTESCEOCONTRACTFIXEDTERM', blank=True) # Field name made lowercase.
    notesceocontractgoldenhellos = models.TextField(db_column='NOTESCEOCONTRACTGOLDENHELLOS', blank=True) # Field name made lowercase.
    notesceocontractlifeinsurance = models.TextField(db_column='NOTESCEOCONTRACTLIFEINSURANCE', blank=True) # Field name made lowercase.
    notesceocontractnotes = models.TextField(db_column='NOTESCEOCONTRACTNOTES', blank=True) # Field name made lowercase.
    notesceocontractpensionguarantee = models.TextField(db_column='NOTESCEOCONTRACTPENSIONGUARANTEE', blank=True) # Field name made lowercase.
    notesceocontractpostceochairman0 = models.TextField(db_column='NOTESCEOCONTRACTPOSTCEOCHAIRMAN0', blank=True) # Field name made lowercase.
    notesceocontractpostceochairman1 = models.TextField(db_column='NOTESCEOCONTRACTPOSTCEOCHAIRMAN1', blank=True) # Field name made lowercase.
    notesceocontractpostceochairmans = models.TextField(db_column='NOTESCEOCONTRACTPOSTCEOCHAIRMANS', blank=True) # Field name made lowercase.
    notesceocontractpostretirementbe = models.TextField(db_column='NOTESCEOCONTRACTPOSTRETIREMENTBE', blank=True) # Field name made lowercase.
    notesceocontractpostretirementc0 = models.TextField(db_column='NOTESCEOCONTRACTPOSTRETIREMENTC0', blank=True) # Field name made lowercase.
    notesceocontractpostretirementc1 = models.TextField(db_column='NOTESCEOCONTRACTPOSTRETIREMENTC1', blank=True) # Field name made lowercase.
    notesceocontractpostretirementco = models.TextField(db_column='NOTESCEOCONTRACTPOSTRETIREMENTCO', blank=True) # Field name made lowercase.
    notesceocontractrenewal = models.TextField(db_column='NOTESCEOCONTRACTRENEWAL', blank=True) # Field name made lowercase.
    notesceocontractretentionawards = models.TextField(db_column='NOTESCEOCONTRACTRETENTIONAWARDS', blank=True) # Field name made lowercase.
    notesceocontractrolling = models.TextField(db_column='NOTESCEOCONTRACTROLLING', blank=True) # Field name made lowercase.
    notesceocontractsigningdate = models.TextField(db_column='NOTESCEOCONTRACTSIGNINGDATE', blank=True) # Field name made lowercase.
    notesceocontracttermlength = models.TextField(db_column='NOTESCEOCONTRACTTERMLENGTH', blank=True) # Field name made lowercase.
    prevceofname = models.TextField(db_column='PREVCEOFNAME', blank=True) # Field name made lowercase.
    prevceolname = models.TextField(db_column='PREVCEOLNAME', blank=True) # Field name made lowercase.
    prevceotenure = models.TextField(db_column='PREVCEOTENURE', blank=True) # Field name made lowercase.
    tenure = models.TextField(db_column='TENURE', blank=True) # Field name made lowercase.
    ticker = models.TextField(db_column='TICKER', blank=True) # Field name made lowercase.
    year = models.TextField(db_column='YEAR', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'wrds_ceos'

class WrdsCeos20042007(models.Model):
    ticker = models.TextField(db_column='TICKER', blank=True) # Field name made lowercase.
    companyname = models.TextField(db_column='COMPANYNAME', blank=True) # Field name made lowercase.
    year = models.TextField(db_column='YEAR', blank=True) # Field name made lowercase.
    ceoannbonuscomments = models.TextField(db_column='CEOANNBONUSCOMMENTS', blank=True) # Field name made lowercase.
    ceoannbonusdeferredschemematchin = models.TextField(db_column='CEOANNBONUSDEFERREDSCHEMEMATCHIN', blank=True) # Field name made lowercase.
    ceoannbonuspaymentformconditions = models.TextField(db_column='CEOANNBONUSPAYMENTFORMCONDITIONS', blank=True) # Field name made lowercase.
    ceoannbonuspaymentformother = models.TextField(db_column='CEOANNBONUSPAYMENTFORMOTHER', blank=True) # Field name made lowercase.
    ceoannbonusperfmeasuresdiscretio = models.TextField(db_column='CEOANNBONUSPERFMEASURESDISCRETIO', blank=True) # Field name made lowercase.
    ceoannbonusperfmeasuresgenericli = models.TextField(db_column='CEOANNBONUSPERFMEASURESGENERICLI', blank=True) # Field name made lowercase.
    ceoannbonusperfmeasuresusedinye0 = models.TextField(db_column='CEOANNBONUSPERFMEASURESUSEDINYE0', blank=True) # Field name made lowercase.
    ceoannbonusperfmeasuresusedinye1 = models.TextField(db_column='CEOANNBONUSPERFMEASURESUSEDINYE1', blank=True) # Field name made lowercase.
    ceoannbonusperfmeasuresusedinyea = models.TextField(db_column='CEOANNBONUSPERFMEASURESUSEDINYEA', blank=True) # Field name made lowercase.
    ceoannbonustargetcash = models.TextField(db_column='CEOANNBONUSTARGETCASH', blank=True) # Field name made lowercase.
    ceoannbonusyrachievements = models.TextField(db_column='CEOANNBONUSYRACHIEVEMENTS', blank=True) # Field name made lowercase.
    ceocompensationreviewcompensatio = models.TextField(db_column='CEOCOMPENSATIONREVIEWCOMPENSATIO', blank=True) # Field name made lowercase.
    ceocompensationreviewsalaryincre = models.TextField(db_column='CEOCOMPENSATIONREVIEWSALARYINCRE', blank=True) # Field name made lowercase.
    ceocontractincentivelatestyearac = models.TextField(db_column='CEOCONTRACTINCENTIVELATESTYEARAC', blank=True) # Field name made lowercase.
    ceocontractincentivenotes = models.TextField(db_column='CEOCONTRACTINCENTIVENOTES', blank=True) # Field name made lowercase.
    ceocontractsalarynotes = models.TextField(db_column='CEOCONTRACTSALARYNOTES', blank=True) # Field name made lowercase.
    ceocontractsalarysetting = models.TextField(db_column='CEOCONTRACTSALARYSETTING', blank=True) # Field name made lowercase.
    ceocontractseverancebenefitconti = models.TextField(db_column='CEOCONTRACTSEVERANCEBENEFITCONTI', blank=True) # Field name made lowercase.
    ceocontractseverancechangeofcon1 = models.TextField(db_column='CEOCONTRACTSEVERANCECHANGEOFCON1', blank=True) # Field name made lowercase.
    ceocontractseverancechangeofcon2 = models.TextField(db_column='CEOCONTRACTSEVERANCECHANGEOFCON2', blank=True) # Field name made lowercase.
    ceocontractseverancechangeofcon4 = models.TextField(db_column='CEOCONTRACTSEVERANCECHANGEOFCON4', blank=True) # Field name made lowercase.
    ceocontractseveranceequityaward0 = models.TextField(db_column='CEOCONTRACTSEVERANCEEQUITYAWARD0', blank=True) # Field name made lowercase.
    ceocontractseverancenotes = models.TextField(db_column='CEOCONTRACTSEVERANCENOTES', blank=True) # Field name made lowercase.
    ceocontractseveranceother = models.TextField(db_column='CEOCONTRACTSEVERANCEOTHER', blank=True) # Field name made lowercase.
    ceoltipcomments = models.TextField(db_column='CEOLTIPCOMMENTS', blank=True) # Field name made lowercase.
    ceoltipdividends = models.TextField(db_column='CEOLTIPDIVIDENDS', blank=True) # Field name made lowercase.
    ceoltipmaximumperf = models.TextField(db_column='CEOLTIPMAXIMUMPERF', blank=True) # Field name made lowercase.
    ceoltipmaxpayableother = models.TextField(db_column='CEOLTIPMAXPAYABLEOTHER', blank=True) # Field name made lowercase.
    ceoltipoptionmeasures1 = models.TextField(db_column='CEOLTIPOPTIONMEASURES1', blank=True) # Field name made lowercase.
    ceoltipoptionmeasures2 = models.TextField(db_column='CEOLTIPOPTIONMEASURES2', blank=True) # Field name made lowercase.
    ceoltipownershipguidelinesceo = models.TextField(db_column='CEOLTIPOWNERSHIPGUIDELINESCEO', blank=True) # Field name made lowercase.
    ceoltippaymentform = models.TextField(db_column='CEOLTIPPAYMENTFORM', blank=True) # Field name made lowercase.
    ceoltippaymentformother = models.TextField(db_column='CEOLTIPPAYMENTFORMOTHER', blank=True) # Field name made lowercase.
    ceoltipperfmeasurescorporate1 = models.TextField(db_column='CEOLTIPPERFMEASURESCORPORATE1', blank=True) # Field name made lowercase.
    ceoltipperfmeasurescorporate2 = models.TextField(db_column='CEOLTIPPERFMEASURESCORPORATE2', blank=True) # Field name made lowercase.
    ceoltipperfmeasuresgenericlist = models.TextField(db_column='CEOLTIPPERFMEASURESGENERICLIST', blank=True) # Field name made lowercase.
    ceoltipperfmeasuresother = models.TextField(db_column='CEOLTIPPERFMEASURESOTHER', blank=True) # Field name made lowercase.
    ceoltipperfmeasuresperformancepe = models.TextField(db_column='CEOLTIPPERFMEASURESPERFORMANCEPE', blank=True) # Field name made lowercase.
    ceoltiprestrictionperiod = models.TextField(db_column='CEOLTIPRESTRICTIONPERIOD', blank=True) # Field name made lowercase.
    ceoltipretentionperiod = models.TextField(db_column='CEOLTIPRETENTIONPERIOD', blank=True) # Field name made lowercase.
    ceoltiptargetperf = models.TextField(db_column='CEOLTIPTARGETPERF', blank=True) # Field name made lowercase.
    ceoltipthresholdperf = models.TextField(db_column='CEOLTIPTHRESHOLDPERF', blank=True) # Field name made lowercase.
    ceoltipyrachievements = models.TextField(db_column='CEOLTIPYRACHIEVEMENTS', blank=True) # Field name made lowercase.
    ceopeerpaycompanydescription = models.TextField(db_column='CEOPEERPAYCOMPANYDESCRIPTION', blank=True) # Field name made lowercase.
    ceopeerpaycompanylist = models.TextField(db_column='CEOPEERPAYCOMPANYLIST', blank=True) # Field name made lowercase.
    ceopeerpaysurveys_consultants = models.TextField(db_column='CEOPEERPAYSURVEYS_CONSULTANTS', blank=True) # Field name made lowercase.
    ceopeerperftsrgraphcompanylist = models.TextField(db_column='CEOPEERPERFTSRGRAPHCOMPANYLIST', blank=True) # Field name made lowercase.
    ceopeerperftsrgraphindex = models.TextField(db_column='CEOPEERPERFTSRGRAPHINDEX', blank=True) # Field name made lowercase.
    notesceocontractgoldenhellos = models.TextField(db_column='NOTESCEOCONTRACTGOLDENHELLOS', blank=True) # Field name made lowercase.
    notesceocontractnotes = models.TextField(db_column='NOTESCEOCONTRACTNOTES', blank=True) # Field name made lowercase.
    notesceocontractpensionguarantee = models.TextField(db_column='NOTESCEOCONTRACTPENSIONGUARANTEE', blank=True) # Field name made lowercase.
    notesceocontractpostretirementbe = models.TextField(db_column='NOTESCEOCONTRACTPOSTRETIREMENTBE', blank=True) # Field name made lowercase.
    notesceocontractpostretirementc0 = models.TextField(db_column='NOTESCEOCONTRACTPOSTRETIREMENTC0', blank=True) # Field name made lowercase.
    ceocontractincentivespecialawar1 = models.TextField(db_column='CEOCONTRACTINCENTIVESPECIALAWAR1', blank=True) # Field name made lowercase.
    ceoage = models.TextField(db_column='CEOAGE', blank=True) # Field name made lowercase.
    ceoallothercomp = models.TextField(db_column='CEOALLOTHERCOMP', blank=True) # Field name made lowercase.
    ceoalltotalcompensation = models.TextField(db_column='CEOALLTOTALCOMPENSATION', blank=True) # Field name made lowercase.
    ceoannualbonus = models.TextField(db_column='CEOANNUALBONUS', blank=True) # Field name made lowercase.
    ceoannualoptiongrant1 = models.TextField(db_column='CEOANNUALOPTIONGRANT1', blank=True) # Field name made lowercase.
    ceoannualoptiongrant2 = models.TextField(db_column='CEOANNUALOPTIONGRANT2', blank=True) # Field name made lowercase.
    ceoannualoptiongrant3 = models.TextField(db_column='CEOANNUALOPTIONGRANT3', blank=True) # Field name made lowercase.
    ceoannualoptiongrantblackscholes = models.TextField(db_column='CEOANNUALOPTIONGRANTBLACKSCHOLES', blank=True) # Field name made lowercase.
    ceoannualoptiongrantexercisepri0 = models.TextField(db_column='CEOANNUALOPTIONGRANTEXERCISEPRI0', blank=True) # Field name made lowercase.
    ceoannualoptiongrantexercisepri1 = models.TextField(db_column='CEOANNUALOPTIONGRANTEXERCISEPRI1', blank=True) # Field name made lowercase.
    ceoannualoptiongrantexercisepric = models.TextField(db_column='CEOANNUALOPTIONGRANTEXERCISEPRIC', blank=True) # Field name made lowercase.
    ceoannualoptiongrantpctgoftotal0 = models.TextField(db_column='CEOANNUALOPTIONGRANTPCTGOFTOTAL0', blank=True) # Field name made lowercase.
    ceoannualoptiongrantpctgoftotal1 = models.TextField(db_column='CEOANNUALOPTIONGRANTPCTGOFTOTAL1', blank=True) # Field name made lowercase.
    ceoannualoptiongrantpctgoftotalg = models.TextField(db_column='CEOANNUALOPTIONGRANTPCTGOFTOTALG', blank=True) # Field name made lowercase.
    ceobasesalary = models.TextField(db_column='CEOBASESALARY', blank=True) # Field name made lowercase.
    ceocomphighlights = models.TextField(db_column='CEOCOMPHIGHLIGHTS', blank=True) # Field name made lowercase.
    ceoexercisableoptions = models.TextField(db_column='CEOEXERCISABLEOPTIONS', blank=True) # Field name made lowercase.
    ceofname = models.TextField(db_column='CEOFNAME', blank=True) # Field name made lowercase.
    ceofnameco = models.TextField(db_column='CEOFNAMECO', blank=True) # Field name made lowercase.
    ceohascontract = models.TextField(db_column='CEOHASCONTRACT', blank=True) # Field name made lowercase.
    ceohireyr = models.TextField(db_column='CEOHIREYR', blank=True) # Field name made lowercase.
    ceoischairman = models.TextField(db_column='CEOISCHAIRMAN', blank=True) # Field name made lowercase.
    ceolname = models.TextField(db_column='CEOLNAME', blank=True) # Field name made lowercase.
    ceolnameco = models.TextField(db_column='CEOLNAMECO', blank=True) # Field name made lowercase.
    ceoltipawardedinyear = models.TextField(db_column='CEOLTIPAWARDEDINYEAR', blank=True) # Field name made lowercase.
    ceoltippayout = models.TextField(db_column='CEOLTIPPAYOUT', blank=True) # Field name made lowercase.
    ceoltiptotsharesreservedaddition = models.TextField(db_column='CEOLTIPTOTSHARESRESERVEDADDITION', blank=True) # Field name made lowercase.
    ceoltiptotsharesreserveddilution = models.TextField(db_column='CEOLTIPTOTSHARESRESERVEDDILUTION', blank=True) # Field name made lowercase.
    ceoltiptotsharesreservedscheme1 = models.TextField(db_column='CEOLTIPTOTSHARESRESERVEDSCHEME1', blank=True) # Field name made lowercase.
    ceoltiptotsharesreservedtotal = models.TextField(db_column='CEOLTIPTOTSHARESRESERVEDTOTAL', blank=True) # Field name made lowercase.
    ceoltiptotsharesreservedyearofla = models.TextField(db_column='CEOLTIPTOTSHARESRESERVEDYEAROFLA', blank=True) # Field name made lowercase.
    ceoltipvestedinyear = models.TextField(db_column='CEOLTIPVESTEDINYEAR', blank=True) # Field name made lowercase.
    ceonumberofoptionsexercised = models.TextField(db_column='CEONUMBEROFOPTIONSEXERCISED', blank=True) # Field name made lowercase.
    ceooptionvaluerealized = models.TextField(db_column='CEOOPTIONVALUEREALIZED', blank=True) # Field name made lowercase.
    ceootherannualcomp = models.TextField(db_column='CEOOTHERANNUALCOMP', blank=True) # Field name made lowercase.
    ceorestrictedstock = models.TextField(db_column='CEORESTRICTEDSTOCK', blank=True) # Field name made lowercase.
    ceosharesheld = models.TextField(db_column='CEOSHARESHELD', blank=True) # Field name made lowercase.
    ceosharesheldlastyear = models.TextField(db_column='CEOSHARESHELDLASTYEAR', blank=True) # Field name made lowercase.
    ceosharestopaymultiple = models.TextField(db_column='CEOSHARESTOPAYMULTIPLE', blank=True) # Field name made lowercase.
    ceosummaryblackscholesvalue = models.TextField(db_column='CEOSUMMARYBLACKSCHOLESVALUE', blank=True) # Field name made lowercase.
    ceosummarytclblackscholesvalue = models.TextField(db_column='CEOSUMMARYTCLBLACKSCHOLESVALUE', blank=True) # Field name made lowercase.
    ceotenure = models.TextField(db_column='CEOTENURE', blank=True) # Field name made lowercase.
    ceototalannualcomp = models.TextField(db_column='CEOTOTALANNUALCOMP', blank=True) # Field name made lowercase.
    ceototaltargetcomp = models.TextField(db_column='CEOTOTALTARGETCOMP', blank=True) # Field name made lowercase.
    ceounexercisableoptions = models.TextField(db_column='CEOUNEXERCISABLEOPTIONS', blank=True) # Field name made lowercase.
    ceovalueofexercisableoptions = models.TextField(db_column='CEOVALUEOFEXERCISABLEOPTIONS', blank=True) # Field name made lowercase.
    ceovalueofunexercisableoptions = models.TextField(db_column='CEOVALUEOFUNEXERCISABLEOPTIONS', blank=True) # Field name made lowercase.
    ceovariablepayasstock = models.TextField(db_column='CEOVARIABLEPAYASSTOCK', blank=True) # Field name made lowercase.
    ceovariabletototalpaymultiple = models.TextField(db_column='CEOVARIABLETOTOTALPAYMULTIPLE', blank=True) # Field name made lowercase.
    prevceofname = models.TextField(db_column='PREVCEOFNAME', blank=True) # Field name made lowercase.
    prevceolname = models.TextField(db_column='PREVCEOLNAME', blank=True) # Field name made lowercase.
    prevceotenure = models.TextField(db_column='PREVCEOTENURE', blank=True) # Field name made lowercase.
    ceoannbonusawardmaximumcash = models.TextField(db_column='CEOANNBONUSAWARDMAXIMUMCASH', blank=True) # Field name made lowercase.
    ceoannbonusawardmaximumothersca0 = models.TextField(db_column='CEOANNBONUSAWARDMAXIMUMOTHERSCA0', blank=True) # Field name made lowercase.
    ceoannbonusawardmaximumothersca1 = models.TextField(db_column='CEOANNBONUSAWARDMAXIMUMOTHERSCA1', blank=True) # Field name made lowercase.
    ceoannbonusawardmaximumotherscas = models.TextField(db_column='CEOANNBONUSAWARDMAXIMUMOTHERSCAS', blank=True) # Field name made lowercase.
    ceoannbonusawardmaximumotherspe0 = models.TextField(db_column='CEOANNBONUSAWARDMAXIMUMOTHERSPE0', blank=True) # Field name made lowercase.
    ceoannbonusawardmaximumotherspe1 = models.TextField(db_column='CEOANNBONUSAWARDMAXIMUMOTHERSPE1', blank=True) # Field name made lowercase.
    ceoannbonusawardmaximumothersper = models.TextField(db_column='CEOANNBONUSAWARDMAXIMUMOTHERSPER', blank=True) # Field name made lowercase.
    ceoannbonusdeferredscheme = models.TextField(db_column='CEOANNBONUSDEFERREDSCHEME', blank=True) # Field name made lowercase.
    ceoannbonusdeferredschemedeferra = models.TextField(db_column='CEOANNBONUSDEFERREDSCHEMEDEFERRA', blank=True) # Field name made lowercase.
    ceoannbonusdeferredschememandato = models.TextField(db_column='CEOANNBONUSDEFERREDSCHEMEMANDATO', blank=True) # Field name made lowercase.
    ceoannbonusdeferredschememaximum = models.TextField(db_column='CEOANNBONUSDEFERREDSCHEMEMAXIMUM', blank=True) # Field name made lowercase.
    ceoannbonusdeferredschemesharepr = models.TextField(db_column='CEOANNBONUSDEFERREDSCHEMESHAREPR', blank=True) # Field name made lowercase.
    ceoannbonuspaymentform = models.TextField(db_column='CEOANNBONUSPAYMENTFORM', blank=True) # Field name made lowercase.
    ceoannbonuspayments = models.TextField(db_column='CEOANNBONUSPAYMENTS', blank=True) # Field name made lowercase.
    ceoannbonusperfmeasuresusedinye2 = models.TextField(db_column='CEOANNBONUSPERFMEASURESUSEDINYE2', blank=True) # Field name made lowercase.
    ceoannbonustargetotherscash1 = models.TextField(db_column='CEOANNBONUSTARGETOTHERSCASH1', blank=True) # Field name made lowercase.
    ceoannbonustargetotherscash2 = models.TextField(db_column='CEOANNBONUSTARGETOTHERSCASH2', blank=True) # Field name made lowercase.
    ceoannbonustargetotherscash3 = models.TextField(db_column='CEOANNBONUSTARGETOTHERSCASH3', blank=True) # Field name made lowercase.
    ceoannbonustargetotherspercenta0 = models.TextField(db_column='CEOANNBONUSTARGETOTHERSPERCENTA0', blank=True) # Field name made lowercase.
    ceoannbonustargetotherspercenta1 = models.TextField(db_column='CEOANNBONUSTARGETOTHERSPERCENTA1', blank=True) # Field name made lowercase.
    ceoannbonustargetotherspercentag = models.TextField(db_column='CEOANNBONUSTARGETOTHERSPERCENTAG', blank=True) # Field name made lowercase.
    ceoannualoptiongrantblackschole4 = models.TextField(db_column='CEOANNUALOPTIONGRANTBLACKSCHOLE4', blank=True) # Field name made lowercase.
    ceocompensationreviewsalarysetti = models.TextField(db_column='CEOCOMPENSATIONREVIEWSALARYSETTI', blank=True) # Field name made lowercase.
    ceocompensationreviewtotalcompen = models.TextField(db_column='CEOCOMPENSATIONREVIEWTOTALCOMPEN', blank=True) # Field name made lowercase.
    ceocontractincentivelatestyeara0 = models.TextField(db_column='CEOCONTRACTINCENTIVELATESTYEARA0', blank=True) # Field name made lowercase.
    ceocontractincentivelatestyeara1 = models.TextField(db_column='CEOCONTRACTINCENTIVELATESTYEARA1', blank=True) # Field name made lowercase.
    ceocontractincentivelatestyeara2 = models.TextField(db_column='CEOCONTRACTINCENTIVELATESTYEARA2', blank=True) # Field name made lowercase.
    ceocontractincentivelatestyearaw = models.TextField(db_column='CEOCONTRACTINCENTIVELATESTYEARAW', blank=True) # Field name made lowercase.
    ceocontractincentivespecialawar0 = models.TextField(db_column='CEOCONTRACTINCENTIVESPECIALAWAR0', blank=True) # Field name made lowercase.
    ceocontractincentivespecialaward = models.TextField(db_column='CEOCONTRACTINCENTIVESPECIALAWARD', blank=True) # Field name made lowercase.
    ceocontractseverancebonuscontinu = models.TextField(db_column='CEOCONTRACTSEVERANCEBONUSCONTINU', blank=True) # Field name made lowercase.
    ceocontractseverancechangeofcon0 = models.TextField(db_column='CEOCONTRACTSEVERANCECHANGEOFCON0', blank=True) # Field name made lowercase.
    ceocontractseverancechangeofcon3 = models.TextField(db_column='CEOCONTRACTSEVERANCECHANGEOFCON3', blank=True) # Field name made lowercase.
    ceocontractseverancechangeofcon5 = models.TextField(db_column='CEOCONTRACTSEVERANCECHANGEOFCON5', blank=True) # Field name made lowercase.
    ceocontractseverancechangeofcon6 = models.TextField(db_column='CEOCONTRACTSEVERANCECHANGEOFCON6', blank=True) # Field name made lowercase.
    ceocontractseverancechangeofcont = models.TextField(db_column='CEOCONTRACTSEVERANCECHANGEOFCONT', blank=True) # Field name made lowercase.
    ceocontractseveranceequityawards = models.TextField(db_column='CEOCONTRACTSEVERANCEEQUITYAWARDS', blank=True) # Field name made lowercase.
    ceocontractseverancesalarycontin = models.TextField(db_column='CEOCONTRACTSEVERANCESALARYCONTIN', blank=True) # Field name made lowercase.
    ceoltipawardedinyearoptionexchan = models.TextField(db_column='CEOLTIPAWARDEDINYEAROPTIONEXCHAN', blank=True) # Field name made lowercase.
    ceoltipawardedinyearoptionrepric = models.TextField(db_column='CEOLTIPAWARDEDINYEAROPTIONREPRIC', blank=True) # Field name made lowercase.
    ceoltipawardedinyearoptionshave0 = models.TextField(db_column='CEOLTIPAWARDEDINYEAROPTIONSHAVE0', blank=True) # Field name made lowercase.
    ceoltipawardedinyearoptionshave1 = models.TextField(db_column='CEOLTIPAWARDEDINYEAROPTIONSHAVE1', blank=True) # Field name made lowercase.
    ceoltipawardedinyearoptionshave2 = models.TextField(db_column='CEOLTIPAWARDEDINYEAROPTIONSHAVE2', blank=True) # Field name made lowercase.
    ceoltipawardedinyearoptionshave3 = models.TextField(db_column='CEOLTIPAWARDEDINYEAROPTIONSHAVE3', blank=True) # Field name made lowercase.
    ceoltipawardedinyearoptionshaveb = models.TextField(db_column='CEOLTIPAWARDEDINYEAROPTIONSHAVEB', blank=True) # Field name made lowercase.
    ceoltipmaxpayablecash = models.TextField(db_column='CEOLTIPMAXPAYABLECASH', blank=True) # Field name made lowercase.
    ceoltipoptiondeferredvestingper0 = models.TextField(db_column='CEOLTIPOPTIONDEFERREDVESTINGPER0', blank=True) # Field name made lowercase.
    ceoltipoptiondeferredvestingperi = models.TextField(db_column='CEOLTIPOPTIONDEFERREDVESTINGPERI', blank=True) # Field name made lowercase.
    ceoltipoptionexpirationperiod1 = models.TextField(db_column='CEOLTIPOPTIONEXPIRATIONPERIOD1', blank=True) # Field name made lowercase.
    ceoltipoptionexpirationperiod2 = models.TextField(db_column='CEOLTIPOPTIONEXPIRATIONPERIOD2', blank=True) # Field name made lowercase.
    ceoltipoptionvestingfrequency1 = models.TextField(db_column='CEOLTIPOPTIONVESTINGFREQUENCY1', blank=True) # Field name made lowercase.
    ceoltipoptionvestingfrequency2 = models.TextField(db_column='CEOLTIPOPTIONVESTINGFREQUENCY2', blank=True) # Field name made lowercase.
    ceoltipoptionvestingperiod1 = models.TextField(db_column='CEOLTIPOPTIONVESTINGPERIOD1', blank=True) # Field name made lowercase.
    ceoltipoptionvestingperiod2 = models.TextField(db_column='CEOLTIPOPTIONVESTINGPERIOD2', blank=True) # Field name made lowercase.
    ceoltipoptionvestingrate1 = models.TextField(db_column='CEOLTIPOPTIONVESTINGRATE1', blank=True) # Field name made lowercase.
    ceoltipoptionvestingrate2 = models.TextField(db_column='CEOLTIPOPTIONVESTINGRATE2', blank=True) # Field name made lowercase.
    ceoltipownershipguidelineschair0 = models.TextField(db_column='CEOLTIPOWNERSHIPGUIDELINESCHAIR0', blank=True) # Field name made lowercase.
    ceoltipownershipguidelinescoo_c0 = models.TextField(db_column='CEOLTIPOWNERSHIPGUIDELINESCOO_C0', blank=True) # Field name made lowercase.
    ceoltipownershipguidelinesnotes = models.TextField(db_column='CEOLTIPOWNERSHIPGUIDELINESNOTES', blank=True) # Field name made lowercase.
    ceoltipperfmeasurescorporate3 = models.TextField(db_column='CEOLTIPPERFMEASURESCORPORATE3', blank=True) # Field name made lowercase.
    ceoltiptargetpayable = models.TextField(db_column='CEOLTIPTARGETPAYABLE', blank=True) # Field name made lowercase.
    ceopeerpayindex = models.TextField(db_column='CEOPEERPAYINDEX', blank=True) # Field name made lowercase.
    ceopeerperfincentiveschemecompan = models.TextField(db_column='CEOPEERPERFINCENTIVESCHEMECOMPAN', blank=True) # Field name made lowercase.
    ceopeerperfincentiveschemeindex = models.TextField(db_column='CEOPEERPERFINCENTIVESCHEMEINDEX', blank=True) # Field name made lowercase.
    dirfname = models.TextField(db_column='DIRFNAME', blank=True) # Field name made lowercase.
    dirlname = models.TextField(db_column='DIRLNAME', blank=True) # Field name made lowercase.
    notesceocontract = models.TextField(db_column='NOTESCEOCONTRACT', blank=True) # Field name made lowercase.
    notesceocontractcorporateaircraf = models.TextField(db_column='NOTESCEOCONTRACTCORPORATEAIRCRAF', blank=True) # Field name made lowercase.
    notesceocontractfixedterm = models.TextField(db_column='NOTESCEOCONTRACTFIXEDTERM', blank=True) # Field name made lowercase.
    notesceocontractlifeinsurance = models.TextField(db_column='NOTESCEOCONTRACTLIFEINSURANCE', blank=True) # Field name made lowercase.
    notesceocontractpostceochairman0 = models.TextField(db_column='NOTESCEOCONTRACTPOSTCEOCHAIRMAN0', blank=True) # Field name made lowercase.
    notesceocontractpostceochairmans = models.TextField(db_column='NOTESCEOCONTRACTPOSTCEOCHAIRMANS', blank=True) # Field name made lowercase.
    notesceocontractpostretirementco = models.TextField(db_column='NOTESCEOCONTRACTPOSTRETIREMENTCO', blank=True) # Field name made lowercase.
    notesceocontractrenewal = models.TextField(db_column='NOTESCEOCONTRACTRENEWAL', blank=True) # Field name made lowercase.
    notesceocontractretentionawards = models.TextField(db_column='NOTESCEOCONTRACTRETENTIONAWARDS', blank=True) # Field name made lowercase.
    notesceocontractrolling = models.TextField(db_column='NOTESCEOCONTRACTROLLING', blank=True) # Field name made lowercase.
    notesceocontracttermlength = models.TextField(db_column='NOTESCEOCONTRACTTERMLENGTH', blank=True) # Field name made lowercase.
    dirage = models.TextField(db_column='DIRAGE', blank=True) # Field name made lowercase.
    dirtenure = models.TextField(db_column='DIRTENURE', blank=True) # Field name made lowercase.
    ceoannualoptiongrant4 = models.TextField(db_column='CEOANNUALOPTIONGRANT4', blank=True) # Field name made lowercase.
    ceoannualoptiongrant5 = models.TextField(db_column='CEOANNUALOPTIONGRANT5', blank=True) # Field name made lowercase.
    ceoannualoptiongrantexercisepri2 = models.TextField(db_column='CEOANNUALOPTIONGRANTEXERCISEPRI2', blank=True) # Field name made lowercase.
    ceoannualoptiongrantexercisepri3 = models.TextField(db_column='CEOANNUALOPTIONGRANTEXERCISEPRI3', blank=True) # Field name made lowercase.
    ceoannualoptiongrantpctgoftotal2 = models.TextField(db_column='CEOANNUALOPTIONGRANTPCTGOFTOTAL2', blank=True) # Field name made lowercase.
    ceoannualoptiongrantpctgoftotal3 = models.TextField(db_column='CEOANNUALOPTIONGRANTPCTGOFTOTAL3', blank=True) # Field name made lowercase.
    ceoltipownershipguidelinesceonum = models.TextField(db_column='CEOLTIPOWNERSHIPGUIDELINESCEONUM', blank=True) # Field name made lowercase.
    ceoltipownershipguidelinesother2 = models.TextField(db_column='CEOLTIPOWNERSHIPGUIDELINESOTHER2', blank=True) # Field name made lowercase.
    ceosharesheld1yrincrpct = models.TextField(db_column='CEOSHARESHELD1YRINCRPCT', blank=True) # Field name made lowercase.
    ceosharesheldvtpwrpct = models.TextField(db_column='CEOSHARESHELDVTPWRPCT', blank=True) # Field name made lowercase.
    ceoannbonustargetpercentage = models.TextField(db_column='CEOANNBONUSTARGETPERCENTAGE', blank=True) # Field name made lowercase.
    notesceocontractsigningdate = models.TextField(db_column='NOTESCEOCONTRACTSIGNINGDATE', blank=True) # Field name made lowercase.
    ceocontractsalarylatestincrease = models.TextField(db_column='CEOCONTRACTSALARYLATESTINCREASE', blank=True) # Field name made lowercase.
    ceoannbonusawardmaximumpercentag = models.TextField(db_column='CEOANNBONUSAWARDMAXIMUMPERCENTAG', blank=True) # Field name made lowercase.
    ceoannualoptiongrant6 = models.TextField(db_column='CEOANNUALOPTIONGRANT6', blank=True) # Field name made lowercase.
    ceoannualoptiongrantblackschole0 = models.TextField(db_column='CEOANNUALOPTIONGRANTBLACKSCHOLE0', blank=True) # Field name made lowercase.
    ceoannualoptiongrantblackschole1 = models.TextField(db_column='CEOANNUALOPTIONGRANTBLACKSCHOLE1', blank=True) # Field name made lowercase.
    ceoannualoptiongrantblackschole2 = models.TextField(db_column='CEOANNUALOPTIONGRANTBLACKSCHOLE2', blank=True) # Field name made lowercase.
    ceoannualoptiongrantblackschole3 = models.TextField(db_column='CEOANNUALOPTIONGRANTBLACKSCHOLE3', blank=True) # Field name made lowercase.
    ceoannualoptiongrantexercisepri4 = models.TextField(db_column='CEOANNUALOPTIONGRANTEXERCISEPRI4', blank=True) # Field name made lowercase.
    ceoannualoptiongrantpctgoftotal4 = models.TextField(db_column='CEOANNUALOPTIONGRANTPCTGOFTOTAL4', blank=True) # Field name made lowercase.
    ceocontractminimumbasicsalary = models.TextField(db_column='CEOCONTRACTMINIMUMBASICSALARY', blank=True) # Field name made lowercase.
    ceocontractsalaryformerceo_chair = models.TextField(db_column='CEOCONTRACTSALARYFORMERCEO_CHAIR', blank=True) # Field name made lowercase.
    ceocontractsalaryratelastyear = models.TextField(db_column='CEOCONTRACTSALARYRATELASTYEAR', blank=True) # Field name made lowercase.
    ceocontractsalaryratethisyear = models.TextField(db_column='CEOCONTRACTSALARYRATETHISYEAR', blank=True) # Field name made lowercase.
    ceoltipawardedinyearoptionshave4 = models.TextField(db_column='CEOLTIPAWARDEDINYEAROPTIONSHAVE4', blank=True) # Field name made lowercase.
    ceoltipmaxpayablerestrictedstock = models.TextField(db_column='CEOLTIPMAXPAYABLERESTRICTEDSTOCK', blank=True) # Field name made lowercase.
    ceoltipmaxpayablestockoptions = models.TextField(db_column='CEOLTIPMAXPAYABLESTOCKOPTIONS', blank=True) # Field name made lowercase.
    ceoltipownershipguidelineschairm = models.TextField(db_column='CEOLTIPOWNERSHIPGUIDELINESCHAIRM', blank=True) # Field name made lowercase.
    ceoltipownershipguidelinescoo_cf = models.TextField(db_column='CEOLTIPOWNERSHIPGUIDELINESCOO_CF', blank=True) # Field name made lowercase.
    ceoltipownershipguidelinesother1 = models.TextField(db_column='CEOLTIPOWNERSHIPGUIDELINESOTHER1', blank=True) # Field name made lowercase.
    ceoltipownershipguidelinesother3 = models.TextField(db_column='CEOLTIPOWNERSHIPGUIDELINESOTHER3', blank=True) # Field name made lowercase.
    notesceocontractexpirationdate = models.TextField(db_column='NOTESCEOCONTRACTEXPIRATIONDATE', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'wrds_ceos_2004_2007'

class WrdsCeos2008(models.Model):
    ceoannbonusawardmaximumcash = models.TextField(db_column='CEOAnnBonusAwardMaximumCash', blank=True) # Field name made lowercase.
    ceoannbonusawardmaximumothersca0 = models.TextField(db_column='CEOAnnBonusAwardMaximumOthersCa0', blank=True) # Field name made lowercase.
    ceoannbonusawardmaximumothersca1 = models.TextField(db_column='CEOAnnBonusAwardMaximumOthersCa1', blank=True) # Field name made lowercase.
    ceoannbonusawardmaximumotherscas = models.TextField(db_column='CEOAnnBonusAwardMaximumOthersCas', blank=True) # Field name made lowercase.
    ceoannbonusawardmaximumotherspe0 = models.TextField(db_column='CEOAnnBonusAwardMaximumOthersPe0', blank=True) # Field name made lowercase.
    ceoannbonusawardmaximumotherspe1 = models.TextField(db_column='CEOAnnBonusAwardMaximumOthersPe1', blank=True) # Field name made lowercase.
    ceoannbonusawardmaximumothersper = models.TextField(db_column='CEOAnnBonusAwardMaximumOthersPer', blank=True) # Field name made lowercase.
    ceoannbonuscomments = models.TextField(db_column='CEOAnnBonusComments', blank=True) # Field name made lowercase.
    ceoannbonusdeferredscheme = models.TextField(db_column='CEOAnnBonusDeferredScheme', blank=True) # Field name made lowercase.
    ceoannbonusdeferredschemedeferra = models.TextField(db_column='CEOAnnBonusDeferredSchemeDeferra', blank=True) # Field name made lowercase.
    ceoannbonusdeferredschememandato = models.TextField(db_column='CEOAnnBonusDeferredSchemeMandato', blank=True) # Field name made lowercase.
    ceoannbonusdeferredschemematchin = models.TextField(db_column='CEOAnnBonusDeferredSchemeMatchin', blank=True) # Field name made lowercase.
    ceoannbonusdeferredschememaximum = models.TextField(db_column='CEOAnnBonusDeferredSchemeMaximum', blank=True) # Field name made lowercase.
    ceoannbonusdeferredschemesharepr = models.TextField(db_column='CEOAnnBonusDeferredSchemeSharePr', blank=True) # Field name made lowercase.
    ceoannbonuspaymentform = models.TextField(db_column='CEOAnnBonusPaymentForm', blank=True) # Field name made lowercase.
    ceoannbonuspaymentformconditions = models.TextField(db_column='CEOAnnBonusPaymentFormConditions', blank=True) # Field name made lowercase.
    ceoannbonuspaymentformother = models.TextField(db_column='CEOAnnBonusPaymentFormOther', blank=True) # Field name made lowercase.
    ceoannbonuspayments = models.TextField(db_column='CEOAnnBonusPayments', blank=True) # Field name made lowercase.
    ceoannbonusperfmeasuresdiscretio = models.TextField(db_column='CEOAnnBonusPerfMeasuresDiscretio', blank=True) # Field name made lowercase.
    ceoannbonusperfmeasuresgenericli = models.TextField(db_column='CEOAnnBonusPerfMeasuresGenericLi', blank=True) # Field name made lowercase.
    ceoannbonusperfmeasuresusedinye0 = models.TextField(db_column='CEOAnnBonusPerfMeasuresUsedInYe0', blank=True) # Field name made lowercase.
    ceoannbonusperfmeasuresusedinye1 = models.TextField(db_column='CEOAnnBonusPerfMeasuresUsedInYe1', blank=True) # Field name made lowercase.
    ceoannbonusperfmeasuresusedinye2 = models.TextField(db_column='CEOAnnBonusPerfMeasuresUsedInYe2', blank=True) # Field name made lowercase.
    ceoannbonusperfmeasuresusedinyea = models.TextField(db_column='CEOAnnBonusPerfMeasuresUsedInYea', blank=True) # Field name made lowercase.
    ceoannbonustargetcash = models.TextField(db_column='CEOAnnBonusTargetCash', blank=True) # Field name made lowercase.
    ceoannbonustargetotherscash1 = models.TextField(db_column='CEOAnnBonusTargetOthersCash1', blank=True) # Field name made lowercase.
    ceoannbonustargetotherscash2 = models.TextField(db_column='CEOAnnBonusTargetOthersCash2', blank=True) # Field name made lowercase.
    ceoannbonustargetotherscash3 = models.TextField(db_column='CEOAnnBonusTargetOthersCash3', blank=True) # Field name made lowercase.
    ceoannbonustargetotherspercenta0 = models.TextField(db_column='CEOAnnBonusTargetOthersPercenta0', blank=True) # Field name made lowercase.
    ceoannbonustargetotherspercenta1 = models.TextField(db_column='CEOAnnBonusTargetOthersPercenta1', blank=True) # Field name made lowercase.
    ceoannbonustargetotherspercentag = models.TextField(db_column='CEOAnnBonusTargetOthersPercentag', blank=True) # Field name made lowercase.
    ceoannbonusyrachievements = models.TextField(db_column='CEOAnnBonusYrAchievements', blank=True) # Field name made lowercase.
    ceoannualoptiongrantblackschole1 = models.TextField(db_column='CEOAnnualOptionGrantBlackSchole1', blank=True) # Field name made lowercase.
    ceoannualoptiongrantblackschole2 = models.TextField(db_column='CEOAnnualOptionGrantBlackSchole2', blank=True) # Field name made lowercase.
    ceoannualoptiongrantblackschole3 = models.TextField(db_column='CEOAnnualOptionGrantBlackSchole3', blank=True) # Field name made lowercase.
    ceoannualoptiongrantblackschole4 = models.TextField(db_column='CEOAnnualOptionGrantBlackSchole4', blank=True) # Field name made lowercase.
    ceocomphighlights = models.TextField(db_column='CEOCompHighlights', blank=True) # Field name made lowercase.
    ceocompensationreviewcompensatio = models.TextField(db_column='CEOCompensationReviewCompensatio', blank=True) # Field name made lowercase.
    ceocompensationreviewsalaryincre = models.TextField(db_column='CEOCompensationReviewSalaryIncre', blank=True) # Field name made lowercase.
    ceocompensationreviewsalarysetti = models.TextField(db_column='CEOCompensationReviewSalarySetti', blank=True) # Field name made lowercase.
    ceocompensationreviewtotalcompen = models.TextField(db_column='CEOCompensationReviewTotalCompen', blank=True) # Field name made lowercase.
    ceocontractincentivelatestyeara0 = models.TextField(db_column='CEOContractIncentiveLatestYearA0', blank=True) # Field name made lowercase.
    ceocontractincentivelatestyeara1 = models.TextField(db_column='CEOContractIncentiveLatestYearA1', blank=True) # Field name made lowercase.
    ceocontractincentivelatestyeara2 = models.TextField(db_column='CEOContractIncentiveLatestYearA2', blank=True) # Field name made lowercase.
    ceocontractincentivelatestyearac = models.TextField(db_column='CEOContractIncentiveLatestYearAc', blank=True) # Field name made lowercase.
    ceocontractincentivelatestyearaw = models.TextField(db_column='CEOContractIncentiveLatestYearAw', blank=True) # Field name made lowercase.
    ceocontractincentivenotes = models.TextField(db_column='CEOContractIncentiveNotes', blank=True) # Field name made lowercase.
    ceocontractincentivespecialaward = models.TextField(db_column='CEOContractIncentiveSpecialAward', blank=True) # Field name made lowercase.
    ceocontractsalarynotes = models.TextField(db_column='CEOContractSalaryNotes', blank=True) # Field name made lowercase.
    ceocontractsalarysetting = models.TextField(db_column='CEOContractSalarySetting', blank=True) # Field name made lowercase.
    ceocontractseverancebenefitconti = models.TextField(db_column='CEOContractSeveranceBenefitConti', blank=True) # Field name made lowercase.
    ceocontractseverancebonuscontinu = models.TextField(db_column='CEOContractSeveranceBonusContinu', blank=True) # Field name made lowercase.
    ceocontractseverancechangeofcon0 = models.TextField(db_column='CEOContractSeveranceChangeOfCon0', blank=True) # Field name made lowercase.
    ceocontractseverancechangeofcon1 = models.TextField(db_column='CEOContractSeveranceChangeOfCon1', blank=True) # Field name made lowercase.
    ceocontractseverancechangeofcon2 = models.TextField(db_column='CEOContractSeveranceChangeOfCon2', blank=True) # Field name made lowercase.
    ceocontractseverancechangeofcon3 = models.TextField(db_column='CEOContractSeveranceChangeOfCon3', blank=True) # Field name made lowercase.
    ceocontractseverancechangeofcon4 = models.TextField(db_column='CEOContractSeveranceChangeOfCon4', blank=True) # Field name made lowercase.
    ceocontractseverancechangeofcon5 = models.TextField(db_column='CEOContractSeveranceChangeOfCon5', blank=True) # Field name made lowercase.
    ceocontractseverancechangeofcon6 = models.TextField(db_column='CEOContractSeveranceChangeOfCon6', blank=True) # Field name made lowercase.
    ceocontractseverancechangeofcont = models.TextField(db_column='CEOContractSeveranceChangeOfCont', blank=True) # Field name made lowercase.
    ceocontractseveranceequityaward0 = models.TextField(db_column='CEOContractSeveranceEquityAward0', blank=True) # Field name made lowercase.
    ceocontractseveranceequityawards = models.TextField(db_column='CEOContractSeveranceEquityAwards', blank=True) # Field name made lowercase.
    ceocontractseverancenotes = models.TextField(db_column='CEOContractSeveranceNotes', blank=True) # Field name made lowercase.
    ceocontractseveranceother = models.TextField(db_column='CEOContractSeveranceOther', blank=True) # Field name made lowercase.
    ceocontractseverancesalarycontin = models.TextField(db_column='CEOContractSeveranceSalaryContin', blank=True) # Field name made lowercase.
    ceoltipawardedinyear = models.TextField(db_column='CEOLTIPAwardedinYear', blank=True) # Field name made lowercase.
    ceoltipawardedinyearoptionexchan = models.TextField(db_column='CEOLTIPAwardedinYearOptionExchan', blank=True) # Field name made lowercase.
    ceoltipawardedinyearoptionrepric = models.TextField(db_column='CEOLTIPAwardedinYearOptionRepric', blank=True) # Field name made lowercase.
    ceoltipawardedinyearoptionshave0 = models.TextField(db_column='CEOLTIPAwardedinYearOptionsHave0', blank=True) # Field name made lowercase.
    ceoltipawardedinyearoptionshave2 = models.TextField(db_column='CEOLTIPAwardedinYearOptionsHave2', blank=True) # Field name made lowercase.
    ceoltipawardedinyearoptionshave3 = models.TextField(db_column='CEOLTIPAwardedinYearOptionsHave3', blank=True) # Field name made lowercase.
    ceoltipawardedinyearoptionshaveb = models.TextField(db_column='CEOLTIPAwardedinYearOptionsHaveB', blank=True) # Field name made lowercase.
    ceoltipcomments = models.TextField(db_column='CEOLTIPComments', blank=True) # Field name made lowercase.
    ceoltipdividends = models.TextField(db_column='CEOLTIPDividends', blank=True) # Field name made lowercase.
    ceoltipmaxpayablecash = models.TextField(db_column='CEOLTIPMaxPayableCash', blank=True) # Field name made lowercase.
    ceoltipmaxpayableother = models.TextField(db_column='CEOLTIPMaxPayableOther', blank=True) # Field name made lowercase.
    ceoltipmaximumperf = models.TextField(db_column='CEOLTIPMaximumPerf', blank=True) # Field name made lowercase.
    ceoltipoptiondeferredvestingper0 = models.TextField(db_column='CEOLTIPOptionDeferredVestingPer0', blank=True) # Field name made lowercase.
    ceoltipoptiondeferredvestingperi = models.TextField(db_column='CEOLTIPOptionDeferredVestingPeri', blank=True) # Field name made lowercase.
    ceoltipoptionexpirationperiod1 = models.TextField(db_column='CEOLTIPOptionExpirationPeriod1', blank=True) # Field name made lowercase.
    ceoltipoptionexpirationperiod2 = models.TextField(db_column='CEOLTIPOptionExpirationPeriod2', blank=True) # Field name made lowercase.
    ceoltipoptionmeasures1 = models.TextField(db_column='CEOLTIPOptionMeasures1', blank=True) # Field name made lowercase.
    ceoltipoptionmeasures2 = models.TextField(db_column='CEOLTIPOptionMeasures2', blank=True) # Field name made lowercase.
    ceoltipoptionvestingfrequency1 = models.TextField(db_column='CEOLTIPOptionVestingFrequency1', blank=True) # Field name made lowercase.
    ceoltipoptionvestingfrequency2 = models.TextField(db_column='CEOLTIPOptionVestingFrequency2', blank=True) # Field name made lowercase.
    ceoltipoptionvestingperiod1 = models.TextField(db_column='CEOLTIPOptionVestingPeriod1', blank=True) # Field name made lowercase.
    ceoltipoptionvestingperiod2 = models.TextField(db_column='CEOLTIPOptionVestingPeriod2', blank=True) # Field name made lowercase.
    ceoltipoptionvestingrate1 = models.TextField(db_column='CEOLTIPOptionVestingRate1', blank=True) # Field name made lowercase.
    ceoltipoptionvestingrate2 = models.TextField(db_column='CEOLTIPOptionVestingRate2', blank=True) # Field name made lowercase.
    ceoltipownershipguidelinesceo = models.TextField(db_column='CEOLTIPOwnershipGuidelinesCEO', blank=True) # Field name made lowercase.
    ceoltipownershipguidelinesceonum = models.TextField(db_column='CEOLTIPOwnershipGuidelinesCEONum', blank=True) # Field name made lowercase.
    ceoltipownershipguidelinescoo_c0 = models.TextField(db_column='CEOLTIPOwnershipGuidelinesCOO_C0', blank=True) # Field name made lowercase.
    ceoltipownershipguidelineschair0 = models.TextField(db_column='CEOLTIPOwnershipGuidelinesChair0', blank=True) # Field name made lowercase.
    ceoltipownershipguidelinesnotes = models.TextField(db_column='CEOLTIPOwnershipGuidelinesNotes', blank=True) # Field name made lowercase.
    ceoltippaymentform = models.TextField(db_column='CEOLTIPPaymentForm', blank=True) # Field name made lowercase.
    ceoltippaymentformother = models.TextField(db_column='CEOLTIPPaymentFormOther', blank=True) # Field name made lowercase.
    ceoltipperfmeasurescorporate1 = models.TextField(db_column='CEOLTIPPerfMeasuresCorporate1', blank=True) # Field name made lowercase.
    ceoltipperfmeasurescorporate2 = models.TextField(db_column='CEOLTIPPerfMeasuresCorporate2', blank=True) # Field name made lowercase.
    ceoltipperfmeasurescorporate3 = models.TextField(db_column='CEOLTIPPerfMeasuresCorporate3', blank=True) # Field name made lowercase.
    ceoltipperfmeasuresgenericlist = models.TextField(db_column='CEOLTIPPerfMeasuresGenericList', blank=True) # Field name made lowercase.
    ceoltipperfmeasuresother = models.TextField(db_column='CEOLTIPPerfMeasuresOther', blank=True) # Field name made lowercase.
    ceoltipperfmeasuresperformancepe = models.TextField(db_column='CEOLTIPPerfMeasuresPerformancePe', blank=True) # Field name made lowercase.
    ceoltiprestrictionperiod = models.TextField(db_column='CEOLTIPRestrictionPeriod', blank=True) # Field name made lowercase.
    ceoltipretentionperiod = models.TextField(db_column='CEOLTIPRetentionPeriod', blank=True) # Field name made lowercase.
    ceoltiptargetpayable = models.TextField(db_column='CEOLTIPTargetPayable', blank=True) # Field name made lowercase.
    ceoltiptargetperf = models.TextField(db_column='CEOLTIPTargetPerf', blank=True) # Field name made lowercase.
    ceoltipthresholdperf = models.TextField(db_column='CEOLTIPThresholdPerf', blank=True) # Field name made lowercase.
    ceoltiptotsharesreservedtotal = models.TextField(db_column='CEOLTIPTotSharesReservedTotal', blank=True) # Field name made lowercase.
    ceoltipvestedinyear = models.TextField(db_column='CEOLTIPVestedinYear', blank=True) # Field name made lowercase.
    ceoltipyrachievements = models.TextField(db_column='CEOLTIPYrAchievements', blank=True) # Field name made lowercase.
    ceopeerpaycompanydescription = models.TextField(db_column='CEOPeerPayCompanyDescription', blank=True) # Field name made lowercase.
    ceopeerpaycompanylist = models.TextField(db_column='CEOPeerPayCompanyList', blank=True) # Field name made lowercase.
    ceopeerpayindex = models.TextField(db_column='CEOPeerPayIndex', blank=True) # Field name made lowercase.
    ceopeerpaysurveys_consultants = models.TextField(db_column='CEOPeerPaySurveys_Consultants', blank=True) # Field name made lowercase.
    ceopeerperfincentiveschemecompan = models.TextField(db_column='CEOPeerPerfIncentiveSchemeCompan', blank=True) # Field name made lowercase.
    ceopeerperfincentiveschemeindex = models.TextField(db_column='CEOPeerPerfIncentiveSchemeIndex', blank=True) # Field name made lowercase.
    ceopeerperftsrgraphcompanylist = models.TextField(db_column='CEOPeerPerfTSRGraphCompanyList', blank=True) # Field name made lowercase.
    ceopeerperftsrgraphindex = models.TextField(db_column='CEOPeerPerfTSRGraphIndex', blank=True) # Field name made lowercase.
    ceohascontract = models.TextField(db_column='CEOhasContract', blank=True) # Field name made lowercase.
    companyname = models.TextField(db_column='CompanyName', blank=True) # Field name made lowercase.
    dirfname = models.TextField(db_column='DirFName', blank=True) # Field name made lowercase.
    dirlname = models.TextField(db_column='DirLName', blank=True) # Field name made lowercase.
    notesceocontract = models.TextField(db_column='NotesCEOContract', blank=True) # Field name made lowercase.
    notesceocontractcorporateaircraf = models.TextField(db_column='NotesCEOContractCorporateAircraf', blank=True) # Field name made lowercase.
    notesceocontractfixedterm = models.TextField(db_column='NotesCEOContractFixedTerm', blank=True) # Field name made lowercase.
    notesceocontractgoldenhellos = models.TextField(db_column='NotesCEOContractGoldenHellos', blank=True) # Field name made lowercase.
    notesceocontractlifeinsurance = models.TextField(db_column='NotesCEOContractLifeInsurance', blank=True) # Field name made lowercase.
    notesceocontractnotes = models.TextField(db_column='NotesCEOContractNotes', blank=True) # Field name made lowercase.
    notesceocontractpensionguarantee = models.TextField(db_column='NotesCEOContractPensionGuarantee', blank=True) # Field name made lowercase.
    notesceocontractpostceochairman0 = models.TextField(db_column='NotesCEOContractPostCEOChairman0', blank=True) # Field name made lowercase.
    notesceocontractpostceochairmans = models.TextField(db_column='NotesCEOContractPostCEOChairmans', blank=True) # Field name made lowercase.
    notesceocontractpostretirementbe = models.TextField(db_column='NotesCEOContractPostRetirementBe', blank=True) # Field name made lowercase.
    notesceocontractpostretirementc0 = models.TextField(db_column='NotesCEOContractPostRetirementC0', blank=True) # Field name made lowercase.
    notesceocontractpostretirementco = models.TextField(db_column='NotesCEOContractPostRetirementCo', blank=True) # Field name made lowercase.
    notesceocontractrenewal = models.TextField(db_column='NotesCEOContractRenewal', blank=True) # Field name made lowercase.
    notesceocontractretentionawards = models.TextField(db_column='NotesCEOContractRetentionAwards', blank=True) # Field name made lowercase.
    notesceocontractrolling = models.TextField(db_column='NotesCEOContractRolling', blank=True) # Field name made lowercase.
    notesceocontracttermlength = models.TextField(db_column='NotesCEOContractTermLength', blank=True) # Field name made lowercase.
    ticker = models.TextField(db_column='Ticker', blank=True) # Field name made lowercase.
    dirage = models.TextField(db_column='DirAge', blank=True) # Field name made lowercase.
    dirtenure = models.TextField(db_column='DirTenure', blank=True) # Field name made lowercase.
    ceohireyr = models.TextField(db_column='CEOHireYr', blank=True) # Field name made lowercase.
    ceoallothercomp = models.TextField(db_column='CEOAllOtherComp', blank=True) # Field name made lowercase.
    ceoalltotalcompensation = models.TextField(db_column='CEOAllTotalCompensation', blank=True) # Field name made lowercase.
    ceoannualbonus = models.TextField(db_column='CEOAnnualBonus', blank=True) # Field name made lowercase.
    ceobasesalary = models.TextField(db_column='CEOBaseSalary', blank=True) # Field name made lowercase.
    ceoexercisableoptions = models.TextField(db_column='CEOExercisableOptions', blank=True) # Field name made lowercase.
    ceoltippayout = models.TextField(db_column='CEOLTIPPayout', blank=True) # Field name made lowercase.
    ceootherannualcomp = models.TextField(db_column='CEOOtherAnnualComp', blank=True) # Field name made lowercase.
    ceorestrictedstock = models.TextField(db_column='CEORestrictedStock', blank=True) # Field name made lowercase.
    ceototalannualcomp = models.TextField(db_column='CEOTotalAnnualComp', blank=True) # Field name made lowercase.
    ceovariabletototalpaymultiple = models.TextField(db_column='CEOVariableToTotalPayMultiple', blank=True) # Field name made lowercase.
    ceosharesheld = models.TextField(db_column='CEOSharesHeld', blank=True) # Field name made lowercase.
    ceosharesheldlastyear = models.TextField(db_column='CEOSharesHeldLastYear', blank=True) # Field name made lowercase.
    ceosharestopaymultiple = models.TextField(db_column='CEOSharesToPayMultiple', blank=True) # Field name made lowercase.
    ceoannualoptiongrant1 = models.TextField(db_column='CEOAnnualOptionGrant1', blank=True) # Field name made lowercase.
    ceoannualoptiongrant2 = models.TextField(db_column='CEOAnnualOptionGrant2', blank=True) # Field name made lowercase.
    ceoannualoptiongrant3 = models.TextField(db_column='CEOAnnualOptionGrant3', blank=True) # Field name made lowercase.
    ceoannualoptiongrant4 = models.TextField(db_column='CEOAnnualOptionGrant4', blank=True) # Field name made lowercase.
    ceoannualoptiongrant5 = models.TextField(db_column='CEOAnnualOptionGrant5', blank=True) # Field name made lowercase.
    ceoannualoptiongrant6 = models.TextField(db_column='CEOAnnualOptionGrant6', blank=True) # Field name made lowercase.
    ceoannualoptiongrantblackscholes = models.TextField(db_column='CEOAnnualOptionGrantBlackScholes', blank=True) # Field name made lowercase.
    ceoannualoptiongrantblackschole0 = models.TextField(db_column='CEOAnnualOptionGrantBlackSchole0', blank=True) # Field name made lowercase.
    ceoannualoptiongrantexercisepric = models.TextField(db_column='CEOAnnualOptionGrantExercisePric', blank=True) # Field name made lowercase.
    ceoannualoptiongrantexercisepri0 = models.TextField(db_column='CEOAnnualOptionGrantExercisePri0', blank=True) # Field name made lowercase.
    ceoannualoptiongrantexercisepri1 = models.TextField(db_column='CEOAnnualOptionGrantExercisePri1', blank=True) # Field name made lowercase.
    ceoannualoptiongrantexercisepri2 = models.TextField(db_column='CEOAnnualOptionGrantExercisePri2', blank=True) # Field name made lowercase.
    ceoannualoptiongrantexercisepri3 = models.TextField(db_column='CEOAnnualOptionGrantExercisePri3', blank=True) # Field name made lowercase.
    ceoannualoptiongrantexercisepri4 = models.TextField(db_column='CEOAnnualOptionGrantExercisePri4', blank=True) # Field name made lowercase.
    ceoannualoptiongrantpctgoftotalg = models.TextField(db_column='CEOAnnualOptionGrantPctgofTotalG', blank=True) # Field name made lowercase.
    ceoannualoptiongrantpctgoftotal0 = models.TextField(db_column='CEOAnnualOptionGrantPctgofTotal0', blank=True) # Field name made lowercase.
    ceoannualoptiongrantpctgoftotal1 = models.TextField(db_column='CEOAnnualOptionGrantPctgofTotal1', blank=True) # Field name made lowercase.
    ceoannualoptiongrantpctgoftotal2 = models.TextField(db_column='CEOAnnualOptionGrantPctgofTotal2', blank=True) # Field name made lowercase.
    ceoannualoptiongrantpctgoftotal3 = models.TextField(db_column='CEOAnnualOptionGrantPctgofTotal3', blank=True) # Field name made lowercase.
    ceoannualoptiongrantpctgoftotal4 = models.TextField(db_column='CEOAnnualOptionGrantPctgofTotal4', blank=True) # Field name made lowercase.
    ceonumberofoptionsexercised = models.TextField(db_column='CEONumberofOptionsExercised', blank=True) # Field name made lowercase.
    ceooptionvaluerealized = models.TextField(db_column='CEOOptionValueRealized', blank=True) # Field name made lowercase.
    ceosummaryblackscholesvalue = models.TextField(db_column='CEOSummaryBlackScholesValue', blank=True) # Field name made lowercase.
    ceosummarytclblackscholesvalue = models.TextField(db_column='CEOSummaryTCLBlackScholesValue', blank=True) # Field name made lowercase.
    ceototaltargetcomp = models.TextField(db_column='CEOTotalTargetComp', blank=True) # Field name made lowercase.
    ceounexercisableoptions = models.TextField(db_column='CEOUnexercisableOptions', blank=True) # Field name made lowercase.
    ceovalueofexercisableoptions = models.TextField(db_column='CEOValueofExercisableOptions', blank=True) # Field name made lowercase.
    ceovalueofunexercisableoptions = models.TextField(db_column='CEOValueOfUnexercisableOptions', blank=True) # Field name made lowercase.
    ceovariablepayasstock = models.TextField(db_column='CEOVariablePayAsStock', blank=True) # Field name made lowercase.
    ceoltipownershipguidelineschairm = models.TextField(db_column='CEOLTIPOwnershipGuidelinesChairm', blank=True) # Field name made lowercase.
    ceoltipownershipguidelinescoo_cf = models.TextField(db_column='CEOLTIPOwnershipGuidelinesCOO_CF', blank=True) # Field name made lowercase.
    ceoltipownershipguidelinesother1 = models.TextField(db_column='CEOLTIPOwnershipGuidelinesOther1', blank=True) # Field name made lowercase.
    ceoltipownershipguidelinesother2 = models.TextField(db_column='CEOLTIPOwnershipGuidelinesOther2', blank=True) # Field name made lowercase.
    ceoltipownershipguidelinesother3 = models.TextField(db_column='CEOLTIPOwnershipGuidelinesOther3', blank=True) # Field name made lowercase.
    ceosharesheld1yrincrpct = models.TextField(db_column='CEOSharesHeld1yrIncrPct', blank=True) # Field name made lowercase.
    ceosharesheldvtpwrpct = models.TextField(db_column='CEOSharesHeldVtPwrPct', blank=True) # Field name made lowercase.
    ceoannbonustargetpercentage = models.TextField(db_column='CEOAnnBonusTargetPercentage', blank=True) # Field name made lowercase.
    ceoannbonusawardmaximumpercentag = models.TextField(db_column='CEOAnnBonusAwardMaximumPercentag', blank=True) # Field name made lowercase.
    ceoltipmaxpayablestockoptions = models.TextField(db_column='CEOLTIPMaxPayableStockOptions', blank=True) # Field name made lowercase.
    ceoltipmaxpayablerestrictedstock = models.TextField(db_column='CEOLTIPMaxPayableRestrictedStock', blank=True) # Field name made lowercase.
    ceoltiptotsharesreservedscheme1 = models.TextField(db_column='CEOLTIPTotSharesReservedScheme1', blank=True) # Field name made lowercase.
    ceoltiptotsharesreserveddilution = models.TextField(db_column='CEOLTIPTotSharesReservedDilution', blank=True) # Field name made lowercase.
    ceoltiptotsharesreservedaddition = models.TextField(db_column='CEOLTIPTotSharesReservedAddition', blank=True) # Field name made lowercase.
    ceoltiptotsharesreservedyearofla = models.TextField(db_column='CEOLTIPTotSharesReservedYearOfLa', blank=True) # Field name made lowercase.
    ceoltipawardedinyearoptionshave1 = models.TextField(db_column='CEOLTIPAwardedinYearOptionsHave1', blank=True) # Field name made lowercase.
    ceoltipawardedinyearoptionshave4 = models.TextField(db_column='CEOLTIPAwardedinYearOptionsHave4', blank=True) # Field name made lowercase.
    notesceocontractsigningdate = models.TextField(db_column='NotesCEOContractSigningDate', blank=True) # Field name made lowercase.
    notesceocontractexpirationdate = models.TextField(db_column='NotesCEOContractExpirationDate', blank=True) # Field name made lowercase.
    ceocontractminimumbasicsalary = models.TextField(db_column='CEOContractMinimumBasicSalary', blank=True) # Field name made lowercase.
    ceocontractsalarylatestincrease = models.TextField(db_column='CEOContractSalaryLatestIncrease', blank=True) # Field name made lowercase.
    ceocontractsalaryratethisyear = models.TextField(db_column='CEOContractSalaryRateThisYear', blank=True) # Field name made lowercase.
    ceocontractsalaryratelastyear = models.TextField(db_column='CEOContractSalaryRateLastYear', blank=True) # Field name made lowercase.
    ceocontractsalaryformerceo_chair = models.TextField(db_column='CEOContractSalaryFormerCEO_Chair', blank=True) # Field name made lowercase.
    ceocontractincentivespecialawar0 = models.TextField(db_column='CEOContractIncentiveSpecialAwar0', blank=True) # Field name made lowercase.
    ceocontractincentivespecialawar1 = models.TextField(db_column='CEOContractIncentiveSpecialAwar1', blank=True) # Field name made lowercase.
    ceototsumcomp = models.TextField(db_column='CEOTotSumComp', blank=True) # Field name made lowercase.
    year = models.TextField(db_column='YEAR', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'wrds_ceos_2008'

class WrdsCeos2009(models.Model):
    ticker = models.TextField(db_column='Ticker', blank=True) # Field name made lowercase.
    companyname = models.TextField(db_column='CompanyName', blank=True) # Field name made lowercase.
    dirfname = models.TextField(db_column='DirFName', blank=True) # Field name made lowercase.
    dirlname = models.TextField(db_column='DirLName', blank=True) # Field name made lowercase.
    dirage = models.TextField(db_column='DirAge', blank=True) # Field name made lowercase.
    dirtenure = models.TextField(db_column='DirTenure', blank=True) # Field name made lowercase.
    ceohireyr = models.TextField(db_column='CEOHireYr', blank=True) # Field name made lowercase.
    ceohascontract = models.TextField(db_column='CEOhasContract', blank=True) # Field name made lowercase.
    ceobasesalary = models.TextField(db_column='CEOBaseSalary', blank=True) # Field name made lowercase.
    ceoexercisableoptions = models.TextField(db_column='CEOExercisableOptions', blank=True) # Field name made lowercase.
    ceoltipawardedinyear = models.TextField(db_column='CEOLTIPAwardedinYear', blank=True) # Field name made lowercase.
    ceoltipvestedinyear = models.TextField(db_column='CEOLTIPVestedinYear', blank=True) # Field name made lowercase.
    ceosharesheld = models.TextField(db_column='CEOSharesHeld', blank=True) # Field name made lowercase.
    ceosharesheldlastyear = models.TextField(db_column='CEOSharesHeldLastYear', blank=True) # Field name made lowercase.
    ceoannualoptiongrant1 = models.TextField(db_column='CEOAnnualOptionGrant1', blank=True) # Field name made lowercase.
    ceonumberofoptionsexercised = models.TextField(db_column='CEONumberofOptionsExercised', blank=True) # Field name made lowercase.
    ceooptionvaluerealized = models.TextField(db_column='CEOOptionValueRealized', blank=True) # Field name made lowercase.
    ceosummaryblackscholesvalue = models.TextField(db_column='CEOSummaryBlackScholesValue', blank=True) # Field name made lowercase.
    ceosummarytclblackscholesvalue = models.TextField(db_column='CEOSummaryTCLBlackScholesValue', blank=True) # Field name made lowercase.
    ceototaltargetcomp = models.TextField(db_column='CEOTotalTargetComp', blank=True) # Field name made lowercase.
    ceounexercisableoptions = models.TextField(db_column='CEOUnexercisableOptions', blank=True) # Field name made lowercase.
    ceovalueofexercisableoptions = models.TextField(db_column='CEOValueofExercisableOptions', blank=True) # Field name made lowercase.
    ceovalueofunexercisableoptions = models.TextField(db_column='CEOValueOfUnexercisableOptions', blank=True) # Field name made lowercase.
    ceovariablepayasstock = models.TextField(db_column='CEOVariablePayAsStock', blank=True) # Field name made lowercase.
    ceoltipdividends = models.TextField(db_column='CEOLTIPDividends', blank=True) # Field name made lowercase.
    ceoltipmaximumperf = models.TextField(db_column='CEOLTIPMaximumPerf', blank=True) # Field name made lowercase.
    ceoltipoptionvestingfrequency2 = models.TextField(db_column='CEOLTIPOptionVestingFrequency2', blank=True) # Field name made lowercase.
    ceoltipownershipguidelinesceonum = models.TextField(db_column='CEOLTIPOwnershipGuidelinesCEONum', blank=True) # Field name made lowercase.
    ceoltipownershipguidelineschairm = models.TextField(db_column='CEOLTIPOwnershipGuidelinesChairm', blank=True) # Field name made lowercase.
    ceoltipownershipguidelinescoo_cf = models.TextField(db_column='CEOLTIPOwnershipGuidelinesCOO_CF', blank=True) # Field name made lowercase.
    ceoltipownershipguidelinesother1 = models.TextField(db_column='CEOLTIPOwnershipGuidelinesOther1', blank=True) # Field name made lowercase.
    ceoltipownershipguidelinesother2 = models.TextField(db_column='CEOLTIPOwnershipGuidelinesOther2', blank=True) # Field name made lowercase.
    ceoltipownershipguidelinesother3 = models.TextField(db_column='CEOLTIPOwnershipGuidelinesOther3', blank=True) # Field name made lowercase.
    ceoltiptargetperf = models.TextField(db_column='CEOLTIPTargetPerf', blank=True) # Field name made lowercase.
    ceoltipthresholdperf = models.TextField(db_column='CEOLTIPThresholdPerf', blank=True) # Field name made lowercase.
    ceosharesheld1yrincrpct = models.TextField(db_column='CEOSharesHeld1yrIncrPct', blank=True) # Field name made lowercase.
    ceosharesheldvtpwrpct = models.TextField(db_column='CEOSharesHeldVtPwrPct', blank=True) # Field name made lowercase.
    ceopeerpaycompanydescription = models.TextField(db_column='CEOPeerPayCompanyDescription', blank=True) # Field name made lowercase.
    ceopeerpaycompanylist = models.TextField(db_column='CEOPeerPayCompanyList', blank=True) # Field name made lowercase.
    ceopeerpayindex = models.TextField(db_column='CEOPeerPayIndex', blank=True) # Field name made lowercase.
    ceopeerpaysurveys_consultants = models.TextField(db_column='CEOPeerPaySurveys_Consultants', blank=True) # Field name made lowercase.
    ceopeerperfincentiveschemecompan = models.TextField(db_column='CEOPeerPerfIncentiveSchemeCompan', blank=True) # Field name made lowercase.
    ceopeerperfincentiveschemeindex = models.TextField(db_column='CEOPeerPerfIncentiveSchemeIndex', blank=True) # Field name made lowercase.
    ceopeerperftsrgraphcompanylist = models.TextField(db_column='CEOPeerPerfTSRGraphCompanyList', blank=True) # Field name made lowercase.
    ceopeerperftsrgraphindex = models.TextField(db_column='CEOPeerPerfTSRGraphIndex', blank=True) # Field name made lowercase.
    ceocompensationreviewsalaryincre = models.TextField(db_column='CEOCompensationReviewSalaryIncre', blank=True) # Field name made lowercase.
    ceocompensationreviewsalarysetti = models.TextField(db_column='CEOCompensationReviewSalarySetti', blank=True) # Field name made lowercase.
    ceocompensationreviewtotalcompen = models.TextField(db_column='CEOCompensationReviewTotalCompen', blank=True) # Field name made lowercase.
    ceocompensationreviewcompensatio = models.TextField(db_column='CEOCompensationReviewCompensatio', blank=True) # Field name made lowercase.
    ceocomphighlights = models.TextField(db_column='CEOCompHighlights', blank=True) # Field name made lowercase.
    ceoannbonustargetpercentage = models.TextField(db_column='CEOAnnBonusTargetPercentage', blank=True) # Field name made lowercase.
    ceoannbonustargetcash = models.TextField(db_column='CEOAnnBonusTargetCash', blank=True) # Field name made lowercase.
    ceoannbonustargetotherspercentag = models.TextField(db_column='CEOAnnBonusTargetOthersPercentag', blank=True) # Field name made lowercase.
    ceoannbonustargetotherscash1 = models.TextField(db_column='CEOAnnBonusTargetOthersCash1', blank=True) # Field name made lowercase.
    ceoannbonustargetotherspercenta1 = models.TextField(db_column='CEOAnnBonusTargetOthersPercenta1', blank=True) # Field name made lowercase.
    ceoannbonustargetotherscash2 = models.TextField(db_column='CEOAnnBonusTargetOthersCash2', blank=True) # Field name made lowercase.
    ceoannbonustargetotherspercenta2 = models.TextField(db_column='CEOAnnBonusTargetOthersPercenta2', blank=True) # Field name made lowercase.
    ceoannbonustargetotherscash3 = models.TextField(db_column='CEOAnnBonusTargetOthersCash3', blank=True) # Field name made lowercase.
    ceoannbonusawardmaximumpercentag = models.TextField(db_column='CEOAnnBonusAwardMaximumPercentag', blank=True) # Field name made lowercase.
    ceoannbonusawardmaximumcash = models.TextField(db_column='CEOAnnBonusAwardMaximumCash', blank=True) # Field name made lowercase.
    ceoannbonusawardmaximumothersper = models.TextField(db_column='CEOAnnBonusAwardMaximumOthersPer', blank=True) # Field name made lowercase.
    ceoannbonusawardmaximumotherscas = models.TextField(db_column='CEOAnnBonusAwardMaximumOthersCas', blank=True) # Field name made lowercase.
    ceoannbonusawardmaximumotherspe1 = models.TextField(db_column='CEOAnnBonusAwardMaximumOthersPe1', blank=True) # Field name made lowercase.
    ceoannbonusawardmaximumothersca1 = models.TextField(db_column='CEOAnnBonusAwardMaximumOthersCa1', blank=True) # Field name made lowercase.
    ceoannbonusawardmaximumotherspe2 = models.TextField(db_column='CEOAnnBonusAwardMaximumOthersPe2', blank=True) # Field name made lowercase.
    ceoannbonusawardmaximumothersca2 = models.TextField(db_column='CEOAnnBonusAwardMaximumOthersCa2', blank=True) # Field name made lowercase.
    ceoannbonuspaymentform = models.TextField(db_column='CEOAnnBonusPaymentForm', blank=True) # Field name made lowercase.
    ceoannbonuspaymentformother = models.TextField(db_column='CEOAnnBonusPaymentFormOther', blank=True) # Field name made lowercase.
    ceoannbonuspaymentformconditions = models.TextField(db_column='CEOAnnBonusPaymentFormConditions', blank=True) # Field name made lowercase.
    ceoannbonusperfmeasuresusedinyea = models.TextField(db_column='CEOAnnBonusPerfMeasuresUsedInYea', blank=True) # Field name made lowercase.
    ceoannbonusperfmeasuresusedinye1 = models.TextField(db_column='CEOAnnBonusPerfMeasuresUsedInYe1', blank=True) # Field name made lowercase.
    ceoannbonusperfmeasuresusedinye2 = models.TextField(db_column='CEOAnnBonusPerfMeasuresUsedInYe2', blank=True) # Field name made lowercase.
    ceoannbonusperfmeasuresdiscretio = models.TextField(db_column='CEOAnnBonusPerfMeasuresDiscretio', blank=True) # Field name made lowercase.
    ceoannbonusperfmeasuresusedinye3 = models.TextField(db_column='CEOAnnBonusPerfMeasuresUsedInYe3', blank=True) # Field name made lowercase.
    ceoannbonusperfmeasuresgenericli = models.TextField(db_column='CEOAnnBonusPerfMeasuresGenericLi', blank=True) # Field name made lowercase.
    ceoannbonuspayments = models.TextField(db_column='CEOAnnBonusPayments', blank=True) # Field name made lowercase.
    ceoannbonusyrachievements = models.TextField(db_column='CEOAnnBonusYrAchievements', blank=True) # Field name made lowercase.
    ceoannbonusdeferredscheme = models.TextField(db_column='CEOAnnBonusDeferredScheme', blank=True) # Field name made lowercase.
    ceoannbonusdeferredschememaximum = models.TextField(db_column='CEOAnnBonusDeferredSchemeMaximum', blank=True) # Field name made lowercase.
    ceoannbonusdeferredschememandato = models.TextField(db_column='CEOAnnBonusDeferredSchemeMandato', blank=True) # Field name made lowercase.
    ceoannbonusdeferredschemedeferra = models.TextField(db_column='CEOAnnBonusDeferredSchemeDeferra', blank=True) # Field name made lowercase.
    ceoannbonusdeferredschemesharepr = models.TextField(db_column='CEOAnnBonusDeferredSchemeSharePr', blank=True) # Field name made lowercase.
    ceoannbonusdeferredschemematchin = models.TextField(db_column='CEOAnnBonusDeferredSchemeMatchin', blank=True) # Field name made lowercase.
    ceoannbonuscomments = models.TextField(db_column='CEOAnnBonusComments', blank=True) # Field name made lowercase.
    ceoltippaymentform = models.TextField(db_column='CEOLTIPPaymentForm', blank=True) # Field name made lowercase.
    ceoltippaymentformother = models.TextField(db_column='CEOLTIPPaymentFormOther', blank=True) # Field name made lowercase.
    ceoltipyrachievements = models.TextField(db_column='CEOLTIPYrAchievements', blank=True) # Field name made lowercase.
    ceoltipmaxpayablestockoptions = models.TextField(db_column='CEOLTIPMaxPayableStockOptions', blank=True) # Field name made lowercase.
    ceoltipmaxpayablerestrictedstock = models.TextField(db_column='CEOLTIPMaxPayableRestrictedStock', blank=True) # Field name made lowercase.
    ceoltipmaxpayablecash = models.TextField(db_column='CEOLTIPMaxPayableCash', blank=True) # Field name made lowercase.
    ceoltipmaxpayableother = models.TextField(db_column='CEOLTIPMaxPayableOther', blank=True) # Field name made lowercase.
    ceoltiptargetpayable = models.TextField(db_column='CEOLTIPTargetPayable', blank=True) # Field name made lowercase.
    ceoltipoptionvestingrate1 = models.TextField(db_column='CEOLTIPOptionVestingRate1', blank=True) # Field name made lowercase.
    ceoltipoptionvestingrate2 = models.TextField(db_column='CEOLTIPOptionVestingRate2', blank=True) # Field name made lowercase.
    ceoltipoptionvestingperiod1 = models.TextField(db_column='CEOLTIPOptionVestingPeriod1', blank=True) # Field name made lowercase.
    ceoltipoptionvestingperiod2 = models.TextField(db_column='CEOLTIPOptionVestingPeriod2', blank=True) # Field name made lowercase.
    ceoltipoptiondeferredvestingperi = models.TextField(db_column='CEOLTIPOptionDeferredVestingPeri', blank=True) # Field name made lowercase.
    ceoltipoptiondeferredvestingper1 = models.TextField(db_column='CEOLTIPOptionDeferredVestingPer1', blank=True) # Field name made lowercase.
    ceoltipoptionvestingfrequency1 = models.TextField(db_column='CEOLTIPOptionVestingFrequency1', blank=True) # Field name made lowercase.
    ceoltipoptionexpirationperiod1 = models.TextField(db_column='CEOLTIPOptionExpirationPeriod1', blank=True) # Field name made lowercase.
    ceoltipoptionexpirationperiod2 = models.TextField(db_column='CEOLTIPOptionExpirationPeriod2', blank=True) # Field name made lowercase.
    ceoltipoptionmeasures1 = models.TextField(db_column='CEOLTIPOptionMeasures1', blank=True) # Field name made lowercase.
    ceoltipoptionmeasures2 = models.TextField(db_column='CEOLTIPOptionMeasures2', blank=True) # Field name made lowercase.
    ceoltipperfmeasurescorporate1 = models.TextField(db_column='CEOLTIPPerfMeasuresCorporate1', blank=True) # Field name made lowercase.
    ceoltipperfmeasurescorporate2 = models.TextField(db_column='CEOLTIPPerfMeasuresCorporate2', blank=True) # Field name made lowercase.
    ceoltipperfmeasurescorporate3 = models.TextField(db_column='CEOLTIPPerfMeasuresCorporate3', blank=True) # Field name made lowercase.
    ceoltipperfmeasuresperformancepe = models.TextField(db_column='CEOLTIPPerfMeasuresPerformancePe', blank=True) # Field name made lowercase.
    ceoltipperfmeasuresother = models.TextField(db_column='CEOLTIPPerfMeasuresOther', blank=True) # Field name made lowercase.
    ceoltipperfmeasuresgenericlist = models.TextField(db_column='CEOLTIPPerfMeasuresGenericList', blank=True) # Field name made lowercase.
    ceoltiprestrictionperiod = models.TextField(db_column='CEOLTIPRestrictionPeriod', blank=True) # Field name made lowercase.
    ceoltipretentionperiod = models.TextField(db_column='CEOLTIPRetentionPeriod', blank=True) # Field name made lowercase.
    ceoltiptotsharesreservedscheme1 = models.TextField(db_column='CEOLTIPTotSharesReservedScheme1', blank=True) # Field name made lowercase.
    ceoltiptotsharesreservedscheme2 = models.TextField(db_column='CEOLTIPTotSharesReservedScheme2', blank=True) # Field name made lowercase.
    ceoltiptotsharesreservedscheme3 = models.TextField(db_column='CEOLTIPTotSharesReservedScheme3', blank=True) # Field name made lowercase.
    ceoltiptotsharesreservedscheme4 = models.TextField(db_column='CEOLTIPTotSharesReservedScheme4', blank=True) # Field name made lowercase.
    ceoltiptotsharesreservedtotal = models.TextField(db_column='CEOLTIPTotSharesReservedTotal', blank=True) # Field name made lowercase.
    ceoltiptotsharesreserveddilution = models.TextField(db_column='CEOLTIPTotSharesReservedDilution', blank=True) # Field name made lowercase.
    ceoltiptotsharesreservedaddition = models.TextField(db_column='CEOLTIPTotSharesReservedAddition', blank=True) # Field name made lowercase.
    ceoltiptotsharesreservedyearofla = models.TextField(db_column='CEOLTIPTotSharesReservedYearOfLa', blank=True) # Field name made lowercase.
    ceoltipawardedinyearoptionrepric = models.TextField(db_column='CEOLTIPAwardedinYearOptionRepric', blank=True) # Field name made lowercase.
    ceoltipawardedinyearoptionexchan = models.TextField(db_column='CEOLTIPAwardedinYearOptionExchan', blank=True) # Field name made lowercase.
    ceoltipawardedinyearoptionshaveb = models.TextField(db_column='CEOLTIPAwardedinYearOptionsHaveB', blank=True) # Field name made lowercase.
    ceoltipawardedinyearoptionshave1 = models.TextField(db_column='CEOLTIPAwardedinYearOptionsHave1', blank=True) # Field name made lowercase.
    ceoltipawardedinyearoptionshave2 = models.TextField(db_column='CEOLTIPAwardedinYearOptionsHave2', blank=True) # Field name made lowercase.
    ceoltipawardedinyearoptionshave3 = models.TextField(db_column='CEOLTIPAwardedinYearOptionsHave3', blank=True) # Field name made lowercase.
    ceoltipawardedinyearoptionshave4 = models.TextField(db_column='CEOLTIPAwardedinYearOptionsHave4', blank=True) # Field name made lowercase.
    ceoltipawardedinyearoptionshave5 = models.TextField(db_column='CEOLTIPAwardedinYearOptionsHave5', blank=True) # Field name made lowercase.
    ceoltipownershipguidelinesceo = models.TextField(db_column='CEOLTIPOwnershipGuidelinesCEO', blank=True) # Field name made lowercase.
    ceoltipownershipguidelineschair1 = models.TextField(db_column='CEOLTIPOwnershipGuidelinesChair1', blank=True) # Field name made lowercase.
    ceoltipownershipguidelinescoo_c1 = models.TextField(db_column='CEOLTIPOwnershipGuidelinesCOO_C1', blank=True) # Field name made lowercase.
    ceoltipownershipguidelinesnotes = models.TextField(db_column='CEOLTIPOwnershipGuidelinesNotes', blank=True) # Field name made lowercase.
    ceoltipcomments = models.TextField(db_column='CEOLTIPComments', blank=True) # Field name made lowercase.
    notesceocontract = models.TextField(db_column='NotesCEOContract', blank=True) # Field name made lowercase.
    notesceocontracttermlength = models.TextField(db_column='NotesCEOContractTermLength', blank=True) # Field name made lowercase.
    notesceocontractsigningdate = models.TextField(db_column='NotesCEOContractSigningDate', blank=True) # Field name made lowercase.
    notesceocontractexpirationdate = models.TextField(db_column='NotesCEOContractExpirationDate', blank=True) # Field name made lowercase.
    notesceocontractrenewal = models.TextField(db_column='NotesCEOContractRenewal', blank=True) # Field name made lowercase.
    notesceocontractrolling = models.TextField(db_column='NotesCEOContractRolling', blank=True) # Field name made lowercase.
    notesceocontractfixedterm = models.TextField(db_column='NotesCEOContractFixedTerm', blank=True) # Field name made lowercase.
    notesceocontractgoldenhellos = models.TextField(db_column='NotesCEOContractGoldenHellos', blank=True) # Field name made lowercase.
    notesceocontractretentionawards = models.TextField(db_column='NotesCEOContractRetentionAwards', blank=True) # Field name made lowercase.
    ceocontractminimumbasicsalary = models.TextField(db_column='CEOContractMinimumBasicSalary', blank=True) # Field name made lowercase.
    ceocontractsalarylatestincrease = models.TextField(db_column='CEOContractSalaryLatestIncrease', blank=True) # Field name made lowercase.
    ceocontractsalaryratethisyear = models.TextField(db_column='CEOContractSalaryRateThisYear', blank=True) # Field name made lowercase.
    ceocontractsalaryratelastyear = models.TextField(db_column='CEOContractSalaryRateLastYear', blank=True) # Field name made lowercase.
    ceocontractsalarysetting = models.TextField(db_column='CEOContractSalarySetting', blank=True) # Field name made lowercase.
    ceocontractsalaryformerceo_chair = models.TextField(db_column='CEOContractSalaryFormerCEO_Chair', blank=True) # Field name made lowercase.
    ceocontractsalarynotes = models.TextField(db_column='CEOContractSalaryNotes', blank=True) # Field name made lowercase.
    ceocontractincentivelatestyearaw = models.TextField(db_column='CEOContractIncentiveLatestYearAw', blank=True) # Field name made lowercase.
    ceocontractincentivelatestyeara1 = models.TextField(db_column='CEOContractIncentiveLatestYearA1', blank=True) # Field name made lowercase.
    ceocontractincentivelatestyeara2 = models.TextField(db_column='CEOContractIncentiveLatestYearA2', blank=True) # Field name made lowercase.
    ceocontractincentivelatestyeara3 = models.TextField(db_column='CEOContractIncentiveLatestYearA3', blank=True) # Field name made lowercase.
    ceocontractincentivelatestyearac = models.TextField(db_column='CEOContractIncentiveLatestYearAc', blank=True) # Field name made lowercase.
    ceocontractincentivespecialaward = models.TextField(db_column='CEOContractIncentiveSpecialAward', blank=True) # Field name made lowercase.
    ceocontractincentivespecialawar1 = models.TextField(db_column='CEOContractIncentiveSpecialAwar1', blank=True) # Field name made lowercase.
    ceocontractincentivespecialawar2 = models.TextField(db_column='CEOContractIncentiveSpecialAwar2', blank=True) # Field name made lowercase.
    ceocontractincentivenotes = models.TextField(db_column='CEOContractIncentiveNotes', blank=True) # Field name made lowercase.
    notesceocontractcorporateaircraf = models.TextField(db_column='NotesCEOContractCorporateAircraf', blank=True) # Field name made lowercase.
    notesceocontractlifeinsurance = models.TextField(db_column='NotesCEOContractLifeInsurance', blank=True) # Field name made lowercase.
    notesceocontractpensionguarantee = models.TextField(db_column='NotesCEOContractPensionGuarantee', blank=True) # Field name made lowercase.
    ceocontractseverancesalarycontin = models.TextField(db_column='CEOContractSeveranceSalaryContin', blank=True) # Field name made lowercase.
    ceocontractseverancebonuscontinu = models.TextField(db_column='CEOContractSeveranceBonusContinu', blank=True) # Field name made lowercase.
    ceocontractseverancebenefitconti = models.TextField(db_column='CEOContractSeveranceBenefitConti', blank=True) # Field name made lowercase.
    ceocontractseveranceother = models.TextField(db_column='CEOContractSeveranceOther', blank=True) # Field name made lowercase.
    ceocontractseveranceequityawards = models.TextField(db_column='CEOContractSeveranceEquityAwards', blank=True) # Field name made lowercase.
    ceocontractseveranceequityaward1 = models.TextField(db_column='CEOContractSeveranceEquityAward1', blank=True) # Field name made lowercase.
    ceocontractseverancenotes = models.TextField(db_column='CEOContractSeveranceNotes', blank=True) # Field name made lowercase.
    ceocontractseverancechangeofcont = models.TextField(db_column='CEOContractSeveranceChangeOfCont', blank=True) # Field name made lowercase.
    ceocontractseverancechangeofcon1 = models.TextField(db_column='CEOContractSeveranceChangeOfCon1', blank=True) # Field name made lowercase.
    ceocontractseverancechangeofcon2 = models.TextField(db_column='CEOContractSeveranceChangeOfCon2', blank=True) # Field name made lowercase.
    ceocontractseverancechangeofcon3 = models.TextField(db_column='CEOContractSeveranceChangeOfCon3', blank=True) # Field name made lowercase.
    ceocontractseverancechangeofcon4 = models.TextField(db_column='CEOContractSeveranceChangeOfCon4', blank=True) # Field name made lowercase.
    ceocontractseverancechangeofcon5 = models.TextField(db_column='CEOContractSeveranceChangeOfCon5', blank=True) # Field name made lowercase.
    ceocontractseverancechangeofcon6 = models.TextField(db_column='CEOContractSeveranceChangeOfCon6', blank=True) # Field name made lowercase.
    ceocontractseverancechangeofcon7 = models.TextField(db_column='CEOContractSeveranceChangeOfCon7', blank=True) # Field name made lowercase.
    notesceocontractpostceochairmans = models.TextField(db_column='NotesCEOContractPostCEOChairmans', blank=True) # Field name made lowercase.
    notesceocontractpostceochairman1 = models.TextField(db_column='NotesCEOContractPostCEOChairman1', blank=True) # Field name made lowercase.
    notesceocontractpostretirementco = models.TextField(db_column='NotesCEOContractPostRetirementCo', blank=True) # Field name made lowercase.
    notesceocontractpostretirementc1 = models.TextField(db_column='NotesCEOContractPostRetirementC1', blank=True) # Field name made lowercase.
    notesceocontractpostretirementbe = models.TextField(db_column='NotesCEOContractPostRetirementBe', blank=True) # Field name made lowercase.
    notesceocontractnotes = models.TextField(db_column='NotesCEOContractNotes', blank=True) # Field name made lowercase.
    ceobonus = models.TextField(db_column='CEOBonus', blank=True) # Field name made lowercase.
    ceostockawards = models.TextField(db_column='CEOStockAwards', blank=True) # Field name made lowercase.
    ceooptionawards = models.TextField(db_column='CEOOptionAwards', blank=True) # Field name made lowercase.
    ceononeqincentcomp = models.TextField(db_column='CEONonEqIncentComp', blank=True) # Field name made lowercase.
    ceopensionnqdc = models.TextField(db_column='CEOPensionNQDC', blank=True) # Field name made lowercase.
    ceototsumcomp = models.TextField(db_column='CEOTotSumComp', blank=True) # Field name made lowercase.
    ceototanncomp = models.TextField(db_column='CEOTotAnnComp', blank=True) # Field name made lowercase.
    ceototactcomp = models.TextField(db_column='CEOTotActComp', blank=True) # Field name made lowercase.
    ceoallothercompensation = models.TextField(db_column='CEOAllOtherCompensation', blank=True) # Field name made lowercase.
    ceosharestopaymultiple = models.TextField(db_column='CEOSharesToPayMultiple', blank=True) # Field name made lowercase.
    ceovariabletpm = models.TextField(db_column='CEOVariableTPM', blank=True) # Field name made lowercase.
    year = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'wrds_ceos_2009'

class WrdsCeos2010(models.Model):
    ticker = models.TextField(db_column='Ticker', blank=True) # Field name made lowercase.
    companyname = models.TextField(db_column='CompanyName', blank=True) # Field name made lowercase.
    ceocompensationyear = models.TextField(db_column='CEOCompensationYear', blank=True) # Field name made lowercase.
    dirfname = models.TextField(db_column='DirFName', blank=True) # Field name made lowercase.
    dirlname = models.TextField(db_column='DirLName', blank=True) # Field name made lowercase.
    dirage = models.TextField(db_column='DirAge', blank=True) # Field name made lowercase.
    dirtenure = models.TextField(db_column='DirTenure', blank=True) # Field name made lowercase.
    ceohireyr = models.TextField(db_column='CEOHireYr', blank=True) # Field name made lowercase.
    ceohascontract = models.TextField(db_column='CEOhasContract', blank=True) # Field name made lowercase.
    ceobasesalary = models.TextField(db_column='CEOBaseSalary', blank=True) # Field name made lowercase.
    ceoexercisableoptions = models.TextField(db_column='CEOExercisableOptions', blank=True) # Field name made lowercase.
    ceosharesheld = models.TextField(db_column='CEOSharesHeld', blank=True) # Field name made lowercase.
    ceosharesheldlastyear = models.TextField(db_column='CEOSharesHeldLastYear', blank=True) # Field name made lowercase.
    ceoannualoptiongrant1 = models.TextField(db_column='CEOAnnualOptionGrant1', blank=True) # Field name made lowercase.
    ceonumberofoptionsexercised = models.TextField(db_column='CEONumberofOptionsExercised', blank=True) # Field name made lowercase.
    ceooptionvaluerealized = models.TextField(db_column='CEOOptionValueRealized', blank=True) # Field name made lowercase.
    ceounexercisableoptions = models.TextField(db_column='CEOUnexercisableOptions', blank=True) # Field name made lowercase.
    ceoltiptotsharesreserveddilution = models.TextField(db_column='CEOLTIPTotSharesReservedDilution', blank=True) # Field name made lowercase.
    ceobonus = models.TextField(db_column='CEOBonus', blank=True) # Field name made lowercase.
    ceostockawards = models.TextField(db_column='CEOStockAwards', blank=True) # Field name made lowercase.
    ceooptionawards = models.TextField(db_column='CEOOptionAwards', blank=True) # Field name made lowercase.
    ceononeqincentcomp = models.TextField(db_column='CEONonEqIncentComp', blank=True) # Field name made lowercase.
    ceopensionnqdc = models.TextField(db_column='CEOPensionNQDC', blank=True) # Field name made lowercase.
    ceototsumcomp = models.TextField(db_column='CEOTotSumComp', blank=True) # Field name made lowercase.
    ceototanncomp = models.TextField(db_column='CEOTotAnnComp', blank=True) # Field name made lowercase.
    ceototactcomp = models.TextField(db_column='CEOTotActComp', blank=True) # Field name made lowercase.
    ceoallothercompensation = models.TextField(db_column='CEOAllOtherCompensation', blank=True) # Field name made lowercase.
    ceosharestopaymultiple = models.TextField(db_column='CEOSharesToPayMultiple', blank=True) # Field name made lowercase.
    ceovariabletpm = models.TextField(db_column='CEOVariableTPM', blank=True) # Field name made lowercase.
    year = models.TextField(blank=True)
    ceooptionawards_gdv = models.TextField(db_column='CEOOptionAwards_GDV', blank=True) # Field name made lowercase.
    ceostockawards_gdv = models.TextField(db_column='CEOStockAwards_GDV', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'wrds_ceos_2010'

class WrdsCeos2011(models.Model):
    ticker = models.TextField(db_column='Ticker', blank=True) # Field name made lowercase.
    companyname = models.TextField(db_column='CompanyName', blank=True) # Field name made lowercase.
    ceocompensationyear = models.TextField(db_column='CEOCompensationYear', blank=True) # Field name made lowercase.
    dirfname = models.TextField(db_column='DirFName', blank=True) # Field name made lowercase.
    dirlname = models.TextField(db_column='DirLName', blank=True) # Field name made lowercase.
    dirage = models.TextField(db_column='DirAge', blank=True) # Field name made lowercase.
    tenure = models.TextField(db_column='Tenure', blank=True) # Field name made lowercase.
    ceohireyr = models.TextField(db_column='CEOHireYr', blank=True) # Field name made lowercase.
    ceohascontract = models.TextField(db_column='CEOHasContract', blank=True) # Field name made lowercase.
    ceobasesalary = models.TextField(db_column='CEOBaseSalary', blank=True) # Field name made lowercase.
    ceoexercisableoptions = models.TextField(db_column='CEOExercisableOptions', blank=True) # Field name made lowercase.
    ceosharesheld = models.TextField(db_column='CEOSharesHeld', blank=True) # Field name made lowercase.
    ceosharesheldlastyear = models.TextField(db_column='CEOSharesHeldLastYear', blank=True) # Field name made lowercase.
    ceoannualoptiongrant1 = models.TextField(db_column='CEOAnnualOptionGrant1', blank=True) # Field name made lowercase.
    ceonumberofoptionsexercised = models.TextField(db_column='CEONumberofOptionsExercised', blank=True) # Field name made lowercase.
    ceooptionvaluerealized = models.TextField(db_column='CEOOptionValueRealized', blank=True) # Field name made lowercase.
    ceounexercisableoptions = models.TextField(db_column='CEOUnexercisableOptions', blank=True) # Field name made lowercase.
    ceoltiptotsharesreserveddilution = models.TextField(db_column='CEOLTIPTotSharesReservedDilution', blank=True) # Field name made lowercase.
    ceobonus = models.TextField(db_column='CEOBonus', blank=True) # Field name made lowercase.
    ceostockawards_gdv = models.TextField(db_column='CEOStockAwards_GDV', blank=True) # Field name made lowercase.
    ceooptionawards_gdv = models.TextField(db_column='CEOOptionAwards_GDV', blank=True) # Field name made lowercase.
    ceononeqincentcomp = models.TextField(db_column='CEONonEqIncentComp', blank=True) # Field name made lowercase.
    ceopensionnqdc = models.TextField(db_column='CEOPensionNQDC', blank=True) # Field name made lowercase.
    ceototsumcomp = models.TextField(db_column='CEOTotSumComp', blank=True) # Field name made lowercase.
    ceototanncomp = models.TextField(db_column='CEOTotAnnComp', blank=True) # Field name made lowercase.
    ceototactcomp = models.TextField(db_column='CEOTotActComp', blank=True) # Field name made lowercase.
    ceoallothercompensation = models.TextField(db_column='CEOAllOtherCompensation', blank=True) # Field name made lowercase.
    ceosharestopaymultiple = models.TextField(db_column='CEOSharesToPayMultiple', blank=True) # Field name made lowercase.
    ceovariabletpm = models.TextField(db_column='CEOVariableTPM', blank=True) # Field name made lowercase.
    year = models.TextField(db_column='YEAR', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'wrds_ceos_2011'

class WrdsCeos2012(models.Model):
    ticker = models.TextField(db_column='Ticker', blank=True) # Field name made lowercase.
    companyname = models.TextField(db_column='CompanyName', blank=True) # Field name made lowercase.
    ceocompensationyear = models.TextField(db_column='CEOCompensationYear', blank=True) # Field name made lowercase.
    dirfname = models.TextField(db_column='DirFName', blank=True) # Field name made lowercase.
    dirlname = models.TextField(db_column='DirLName', blank=True) # Field name made lowercase.
    dirage = models.TextField(db_column='DirAge', blank=True) # Field name made lowercase.
    tenure = models.TextField(db_column='Tenure', blank=True) # Field name made lowercase.
    ceohireyr = models.TextField(db_column='CEOHireYr', blank=True) # Field name made lowercase.
    ceohascontract = models.TextField(db_column='CEOHasContract', blank=True) # Field name made lowercase.
    ceobasesalary = models.TextField(db_column='CEOBaseSalary', blank=True) # Field name made lowercase.
    ceoexercisableoptions = models.TextField(db_column='CEOExercisableOptions', blank=True) # Field name made lowercase.
    ceosharesheld = models.TextField(db_column='CEOSharesHeld', blank=True) # Field name made lowercase.
    ceosharesheldlastyear = models.TextField(db_column='CEOSharesHeldLastYear', blank=True) # Field name made lowercase.
    ceoannualoptiongrant1 = models.TextField(db_column='CEOAnnualOptionGrant1', blank=True) # Field name made lowercase.
    ceonumberofoptionsexercised = models.TextField(db_column='CEONumberofOptionsExercised', blank=True) # Field name made lowercase.
    ceooptionvaluerealized = models.TextField(db_column='CEOOptionValueRealized', blank=True) # Field name made lowercase.
    ceounexercisableoptions = models.TextField(db_column='CEOUnexercisableOptions', blank=True) # Field name made lowercase.
    ceoltiptotsharesreserveddilution = models.TextField(db_column='CEOLTIPTotSharesReservedDilution', blank=True) # Field name made lowercase.
    ceobonus = models.TextField(db_column='CEOBonus', blank=True) # Field name made lowercase.
    ceostockawards_gdv = models.TextField(db_column='CEOStockAwards_GDV', blank=True) # Field name made lowercase.
    ceooptionawards_gdv = models.TextField(db_column='CEOOptionAwards_GDV', blank=True) # Field name made lowercase.
    ceononeqincentcomp = models.TextField(db_column='CEONonEqIncentComp', blank=True) # Field name made lowercase.
    ceopensionnqdc = models.TextField(db_column='CEOPensionNQDC', blank=True) # Field name made lowercase.
    ceototsumcomp = models.TextField(db_column='CEOTotSumComp', blank=True) # Field name made lowercase.
    ceototanncomp = models.TextField(db_column='CEOTotAnnComp', blank=True) # Field name made lowercase.
    ceototactcomp = models.TextField(db_column='CEOTotActComp', blank=True) # Field name made lowercase.
    ceoallothercompensation = models.TextField(db_column='CEOAllOtherCompensation', blank=True) # Field name made lowercase.
    ceosharestopaymultiple = models.TextField(db_column='CEOSharesToPayMultiple', blank=True) # Field name made lowercase.
    ceovariabletpm = models.TextField(db_column='CEOVariableTPM', blank=True) # Field name made lowercase.
    year = models.TextField(db_column='YEAR', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'wrds_ceos_2012'

class WrdsCompanies(models.Model):
    address1 = models.TextField(db_column='ADDRESS1', blank=True) # Field name made lowercase.
    address2 = models.TextField(db_column='ADDRESS2', blank=True) # Field name made lowercase.
    address3 = models.TextField(db_column='ADDRESS3', blank=True) # Field name made lowercase.
    adr = models.TextField(db_column='ADR', blank=True) # Field name made lowercase.
    annualmtg = models.TextField(db_column='ANNUALMTG', blank=True) # Field name made lowercase.
    annualmtgnext = models.TextField(db_column='ANNUALMTGNEXT', blank=True) # Field name made lowercase.
    annualmtgplace = models.TextField(db_column='ANNUALMTGPLACE', blank=True) # Field name made lowercase.
    auditfees = models.TextField(db_column='AUDITFEES', blank=True) # Field name made lowercase.
    auditfeesit = models.TextField(db_column='AUDITFEESIT', blank=True) # Field name made lowercase.
    auditfeesother = models.TextField(db_column='AUDITFEESOTHER', blank=True) # Field name made lowercase.
    auditfeesprcntg = models.TextField(db_column='AUDITFEESPRCNTG', blank=True) # Field name made lowercase.
    auditfeesrelated = models.TextField(db_column='AUDITFEESRELATED', blank=True) # Field name made lowercase.
    auditfeestax = models.TextField(db_column='AUDITFEESTAX', blank=True) # Field name made lowercase.
    auditfeestotal = models.TextField(db_column='AUDITFEESTOTAL', blank=True) # Field name made lowercase.
    auditnonauditfeespctg = models.TextField(db_column='AUDITNONAUDITFEESPCTG', blank=True) # Field name made lowercase.
    auditor = models.TextField(db_column='AUDITOR', blank=True) # Field name made lowercase.
    auditorchangenotes = models.TextField(db_column='AUDITORCHANGENOTES', blank=True) # Field name made lowercase.
    auditorindependent = models.TextField(db_column='AUDITORINDEPENDENT', blank=True) # Field name made lowercase.
    auditornominee = models.TextField(db_column='AUDITORNOMINEE', blank=True) # Field name made lowercase.
    auditorprevious = models.TextField(db_column='AUDITORPREVIOUS', blank=True) # Field name made lowercase.
    auditorsince = models.TextField(db_column='AUDITORSINCE', blank=True) # Field name made lowercase.
    bdclassified = models.TextField(db_column='BDCLASSIFIED', blank=True) # Field name made lowercase.
    bdmtgs = models.TextField(db_column='BDMTGS', blank=True) # Field name made lowercase.
    bdmtgsoutside = models.TextField(db_column='BDMTGSOUTSIDE', blank=True) # Field name made lowercase.
    bdoutsidemaj = models.TextField(db_column='BDOUTSIDEMAJ', blank=True) # Field name made lowercase.
    bdoutsidemajstrict = models.TextField(db_column='BDOUTSIDEMAJSTRICT', blank=True) # Field name made lowercase.
    bdoutsidemeets = models.TextField(db_column='BDOUTSIDEMEETS', blank=True) # Field name made lowercase.
    bdoutsidemtgsource = models.TextField(db_column='BDOUTSIDEMTGSOURCE', blank=True) # Field name made lowercase.
    busethicscode = models.TextField(db_column='BUSETHICSCODE', blank=True) # Field name made lowercase.
    ceoage = models.TextField(db_column='CEOAGE', blank=True) # Field name made lowercase.
    ceoallothercomp = models.TextField(db_column='CEOALLOTHERCOMP', blank=True) # Field name made lowercase.
    ceoalltotalcompensation = models.TextField(db_column='CEOALLTOTALCOMPENSATION', blank=True) # Field name made lowercase.
    ceoannoptiongrant = models.TextField(db_column='CEOANNOPTIONGRANT', blank=True) # Field name made lowercase.
    ceoannualbonus = models.TextField(db_column='CEOANNUALBONUS', blank=True) # Field name made lowercase.
    ceobasesalary = models.TextField(db_column='CEOBASESALARY', blank=True) # Field name made lowercase.
    ceocomphighlights = models.TextField(db_column='CEOCOMPHIGHLIGHTS', blank=True) # Field name made lowercase.
    ceofname = models.TextField(db_column='CEOFNAME', blank=True) # Field name made lowercase.
    ceohascontract = models.TextField(db_column='CEOHASCONTRACT', blank=True) # Field name made lowercase.
    ceohireyr = models.TextField(db_column='CEOHIREYR', blank=True) # Field name made lowercase.
    ceoischairman = models.TextField(db_column='CEOISCHAIRMAN', blank=True) # Field name made lowercase.
    ceolname = models.TextField(db_column='CEOLNAME', blank=True) # Field name made lowercase.
    ceoltipawardedinyear = models.TextField(db_column='CEOLTIPAWARDEDINYEAR', blank=True) # Field name made lowercase.
    ceoltippayout = models.TextField(db_column='CEOLTIPPAYOUT', blank=True) # Field name made lowercase.
    ceoltipvestedinyear = models.TextField(db_column='CEOLTIPVESTEDINYEAR', blank=True) # Field name made lowercase.
    ceooptionvaluerealized = models.TextField(db_column='CEOOPTIONVALUEREALIZED', blank=True) # Field name made lowercase.
    ceootherannualcomp = models.TextField(db_column='CEOOTHERANNUALCOMP', blank=True) # Field name made lowercase.
    ceopreviousfname = models.TextField(db_column='CEOPREVIOUSFNAME', blank=True) # Field name made lowercase.
    ceopreviouslname = models.TextField(db_column='CEOPREVIOUSLNAME', blank=True) # Field name made lowercase.
    ceoprevioustenure = models.TextField(db_column='CEOPREVIOUSTENURE', blank=True) # Field name made lowercase.
    ceoprofile = models.TextField(db_column='CEOPROFILE', blank=True) # Field name made lowercase.
    ceorestrictedstock = models.TextField(db_column='CEORESTRICTEDSTOCK', blank=True) # Field name made lowercase.
    ceosharesheld = models.TextField(db_column='CEOSHARESHELD', blank=True) # Field name made lowercase.
    ceosharesheldlastyear = models.TextField(db_column='CEOSHARESHELDLASTYEAR', blank=True) # Field name made lowercase.
    ceosharesheldoptions = models.TextField(db_column='CEOSHARESHELDOPTIONS', blank=True) # Field name made lowercase.
    ceosharestopaymultiple = models.TextField(db_column='CEOSHARESTOPAYMULTIPLE', blank=True) # Field name made lowercase.
    ceotenure = models.TextField(db_column='CEOTENURE', blank=True) # Field name made lowercase.
    ceototalannualcomp = models.TextField(db_column='CEOTOTALANNUALCOMP', blank=True) # Field name made lowercase.
    ceounexercisedoptions = models.TextField(db_column='CEOUNEXERCISEDOPTIONS', blank=True) # Field name made lowercase.
    ceovariablepayasstock = models.TextField(db_column='CEOVARIABLEPAYASSTOCK', blank=True) # Field name made lowercase.
    ceovariabletototalpaymultiple = models.TextField(db_column='CEOVARIABLETOTOTALPAYMULTIPLE', blank=True) # Field name made lowercase.
    cfoage = models.TextField(db_column='CFOAGE', blank=True) # Field name made lowercase.
    cfofname = models.TextField(db_column='CFOFNAME', blank=True) # Field name made lowercase.
    cfolname = models.TextField(db_column='CFOLNAME', blank=True) # Field name made lowercase.
    cfoprofile = models.TextField(db_column='CFOPROFILE', blank=True) # Field name made lowercase.
    cfotenure = models.TextField(db_column='CFOTENURE', blank=True) # Field name made lowercase.
    chairmanfname = models.TextField(db_column='CHAIRMANFNAME', blank=True) # Field name made lowercase.
    chairmanis = models.TextField(db_column='CHAIRMANIS', blank=True) # Field name made lowercase.
    chairmanlname = models.TextField(db_column='CHAIRMANLNAME', blank=True) # Field name made lowercase.
    chiefgovofficerfname = models.TextField(db_column='CHIEFGOVOFFICERFNAME', blank=True) # Field name made lowercase.
    chiefgovofficerlname = models.TextField(db_column='CHIEFGOVOFFICERLNAME', blank=True) # Field name made lowercase.
    cik = models.TextField(db_column='CIK', blank=True) # Field name made lowercase.
    city = models.TextField(db_column='CITY', blank=True) # Field name made lowercase.
    cochairmanfname = models.TextField(db_column='COCHAIRMANFNAME', blank=True) # Field name made lowercase.
    cochairmanlname = models.TextField(db_column='COCHAIRMANLNAME', blank=True) # Field name made lowercase.
    commauditfullyindependent = models.TextField(db_column='COMMAUDITFULLYINDEPENDENT', blank=True) # Field name made lowercase.
    commauditindependent = models.TextField(db_column='COMMAUDITINDEPENDENT', blank=True) # Field name made lowercase.
    commcompfullyindependent = models.TextField(db_column='COMMCOMPFULLYINDEPENDENT', blank=True) # Field name made lowercase.
    commcompindependent = models.TextField(db_column='COMMCOMPINDEPENDENT', blank=True) # Field name made lowercase.
    committeeauditnotes = models.TextField(db_column='COMMITTEEAUDITNOTES', blank=True) # Field name made lowercase.
    committeecompensationnotes = models.TextField(db_column='COMMITTEECOMPENSATIONNOTES', blank=True) # Field name made lowercase.
    committeeexecutivenotes = models.TextField(db_column='COMMITTEEEXECUTIVENOTES', blank=True) # Field name made lowercase.
    committeegovernancenotes = models.TextField(db_column='COMMITTEEGOVERNANCENOTES', blank=True) # Field name made lowercase.
    committeemiscnotes = models.TextField(db_column='COMMITTEEMISCNOTES', blank=True) # Field name made lowercase.
    committeenomgovfullyindependent = models.TextField(db_column='COMMITTEENOMGOVFULLYINDEPENDENT', blank=True) # Field name made lowercase.
    committeenomgovindependent = models.TextField(db_column='COMMITTEENOMGOVINDEPENDENT', blank=True) # Field name made lowercase.
    committeenominatingnotes = models.TextField(db_column='COMMITTEENOMINATINGNOTES', blank=True) # Field name made lowercase.
    commnomgovfullyindependent = models.TextField(db_column='COMMNOMGOVFULLYINDEPENDENT', blank=True) # Field name made lowercase.
    commnomgovindependent = models.TextField(db_column='COMMNOMGOVINDEPENDENT', blank=True) # Field name made lowercase.
    companyage = models.TextField(db_column='COMPANYAGE', blank=True) # Field name made lowercase.
    companyfedid = models.TextField(db_column='COMPANYFEDID', blank=True) # Field name made lowercase.
    companyname = models.TextField(db_column='COMPANYNAME', blank=True) # Field name made lowercase.
    companyprofileshort = models.TextField(db_column='COMPANYPROFILESHORT', blank=True) # Field name made lowercase.
    companyprofiletodcalc = models.TextField(db_column='COMPANYPROFILETODCALC', blank=True) # Field name made lowercase.
    compdescription = models.TextField(db_column='COMPDESCRIPTION', blank=True) # Field name made lowercase.
    compfounded = models.TextField(db_column='COMPFOUNDED', blank=True) # Field name made lowercase.
    compplanapproval = models.TextField(db_column='COMPPLANAPPROVAL', blank=True) # Field name made lowercase.
    controlledcompanyexemption = models.TextField(db_column='CONTROLLEDCOMPANYEXEMPTION', blank=True) # Field name made lowercase.
    corpsecretaryfname = models.TextField(db_column='CORPSECRETARYFNAME', blank=True) # Field name made lowercase.
    corpsecretarylname = models.TextField(db_column='CORPSECRETARYLNAME', blank=True) # Field name made lowercase.
    country = models.TextField(db_column='COUNTRY', blank=True) # Field name made lowercase.
    currentyear = models.TextField(db_column='CURRENTYEAR', blank=True) # Field name made lowercase.
    cusip = models.TextField(db_column='CUSIP', blank=True) # Field name made lowercase.
    dc_avgdircomp = models.TextField(db_column='DC_AVGDIRCOMP', blank=True) # Field name made lowercase.
    dc_committeemtgfeeschaira = models.TextField(db_column='DC_COMMITTEEMTGFEESCHAIRA', blank=True) # Field name made lowercase.
    dc_committeemtgfeeschairc = models.TextField(db_column='DC_COMMITTEEMTGFEESCHAIRC', blank=True) # Field name made lowercase.
    dc_committeemtgfeeschaire = models.TextField(db_column='DC_COMMITTEEMTGFEESCHAIRE', blank=True) # Field name made lowercase.
    dc_committeemtgfeeschairg = models.TextField(db_column='DC_COMMITTEEMTGFEESCHAIRG', blank=True) # Field name made lowercase.
    dc_committeemtgfeeschairn = models.TextField(db_column='DC_COMMITTEEMTGFEESCHAIRN', blank=True) # Field name made lowercase.
    dc_committeemtgfeesdira = models.TextField(db_column='DC_COMMITTEEMTGFEESDIRA', blank=True) # Field name made lowercase.
    dc_committeemtgfeesdirc = models.TextField(db_column='DC_COMMITTEEMTGFEESDIRC', blank=True) # Field name made lowercase.
    dc_committeemtgfeesdire = models.TextField(db_column='DC_COMMITTEEMTGFEESDIRE', blank=True) # Field name made lowercase.
    dc_committeemtgfeesdirg = models.TextField(db_column='DC_COMMITTEEMTGFEESDIRG', blank=True) # Field name made lowercase.
    dc_committeemtgfeesdirn = models.TextField(db_column='DC_COMMITTEEMTGFEESDIRN', blank=True) # Field name made lowercase.
    dc_committeemtgretainerchaira = models.TextField(db_column='DC_COMMITTEEMTGRETAINERCHAIRA', blank=True) # Field name made lowercase.
    dc_committeemtgretainerchairc = models.TextField(db_column='DC_COMMITTEEMTGRETAINERCHAIRC', blank=True) # Field name made lowercase.
    dc_committeemtgretainerchaire = models.TextField(db_column='DC_COMMITTEEMTGRETAINERCHAIRE', blank=True) # Field name made lowercase.
    dc_committeemtgretainerchairg = models.TextField(db_column='DC_COMMITTEEMTGRETAINERCHAIRG', blank=True) # Field name made lowercase.
    dc_committeemtgretainerchairn = models.TextField(db_column='DC_COMMITTEEMTGRETAINERCHAIRN', blank=True) # Field name made lowercase.
    dc_committeemtgretainerdira = models.TextField(db_column='DC_COMMITTEEMTGRETAINERDIRA', blank=True) # Field name made lowercase.
    dc_committeemtgretainerdirc = models.TextField(db_column='DC_COMMITTEEMTGRETAINERDIRC', blank=True) # Field name made lowercase.
    dc_committeemtgretainerdire = models.TextField(db_column='DC_COMMITTEEMTGRETAINERDIRE', blank=True) # Field name made lowercase.
    dc_committeemtgretainerdirg = models.TextField(db_column='DC_COMMITTEEMTGRETAINERDIRG', blank=True) # Field name made lowercase.
    dc_committeemtgretainerdirn = models.TextField(db_column='DC_COMMITTEEMTGRETAINERDIRN', blank=True) # Field name made lowercase.
    dc_directorscompensated = models.TextField(db_column='DC_DIRECTORSCOMPENSATED', blank=True) # Field name made lowercase.
    dc_directorsreceivinginitialawar = models.TextField(db_column='DC_DIRECTORSRECEIVINGINITIALAWAR', blank=True) # Field name made lowercase.
    dc_overrideoptionstotal = models.TextField(db_column='DC_OVERRIDEOPTIONSTOTAL', blank=True) # Field name made lowercase.
    dc_stockawardoverridetotals = models.TextField(db_column='DC_STOCKAWARDOVERRIDETOTALS', blank=True) # Field name made lowercase.
    dc_totalmtgfeespaid = models.TextField(db_column='DC_TOTALMTGFEESPAID', blank=True) # Field name made lowercase.
    dirbasepay = models.TextField(db_column='DIRBASEPAY', blank=True) # Field name made lowercase.
    dirbdmtgfees = models.TextField(db_column='DIRBDMTGFEES', blank=True) # Field name made lowercase.
    directorsactiveceopct = models.TextField(db_column='DIRECTORSACTIVECEOPCT', blank=True) # Field name made lowercase.
    directorsactiveceos = models.TextField(db_column='DIRECTORSACTIVECEOS', blank=True) # Field name made lowercase.
    directorsfailed = models.TextField(db_column='DIRECTORSFAILED', blank=True) # Field name made lowercase.
    directorsfailedpct = models.TextField(db_column='DIRECTORSFAILEDPCT', blank=True) # Field name made lowercase.
    directorsinside = models.TextField(db_column='DIRECTORSINSIDE', blank=True) # Field name made lowercase.
    directorsinsidepct = models.TextField(db_column='DIRECTORSINSIDEPCT', blank=True) # Field name made lowercase.
    directorsminority = models.TextField(db_column='DIRECTORSMINORITY', blank=True) # Field name made lowercase.
    directorsoutside = models.TextField(db_column='DIRECTORSOUTSIDE', blank=True) # Field name made lowercase.
    directorsoutsiderelated = models.TextField(db_column='DIRECTORSOUTSIDERELATED', blank=True) # Field name made lowercase.
    directorsoutsiderelatedpct = models.TextField(db_column='DIRECTORSOUTSIDERELATEDPCT', blank=True) # Field name made lowercase.
    directorsoutsidetotal = models.TextField(db_column='DIRECTORSOUTSIDETOTAL', blank=True) # Field name made lowercase.
    directorsover10yrstenure = models.TextField(db_column='DIRECTORSOVER10YRSTENURE', blank=True) # Field name made lowercase.
    directorsover10yrstenurepct = models.TextField(db_column='DIRECTORSOVER10YRSTENUREPCT', blank=True) # Field name made lowercase.
    directorsover15yrstenure = models.TextField(db_column='DIRECTORSOVER15YRSTENURE', blank=True) # Field name made lowercase.
    directorsover15yrstenurepct = models.TextField(db_column='DIRECTORSOVER15YRSTENUREPCT', blank=True) # Field name made lowercase.
    directorsover3boards = models.TextField(db_column='DIRECTORSOVER3BOARDS', blank=True) # Field name made lowercase.
    directorsover4boards = models.TextField(db_column='DIRECTORSOVER4BOARDS', blank=True) # Field name made lowercase.
    directorsover4publicboards = models.TextField(db_column='DIRECTORSOVER4PUBLICBOARDS', blank=True) # Field name made lowercase.
    directorsover4publicboardspct = models.TextField(db_column='DIRECTORSOVER4PUBLICBOARDSPCT', blank=True) # Field name made lowercase.
    directorsover70 = models.TextField(db_column='DIRECTORSOVER70', blank=True) # Field name made lowercase.
    directorsover70pct = models.TextField(db_column='DIRECTORSOVER70PCT', blank=True) # Field name made lowercase.
    directorsproblem = models.TextField(db_column='DIRECTORSPROBLEM', blank=True) # Field name made lowercase.
    directorsproblempct = models.TextField(db_column='DIRECTORSPROBLEMPCT', blank=True) # Field name made lowercase.
    directorstotal = models.TextField(db_column='DIRECTORSTOTAL', blank=True) # Field name made lowercase.
    directorswomen = models.TextField(db_column='DIRECTORSWOMEN', blank=True) # Field name made lowercase.
    directorswomenpct = models.TextField(db_column='DIRECTORSWOMENPCT', blank=True) # Field name made lowercase.
    directorszeroshares = models.TextField(db_column='DIRECTORSZEROSHARES', blank=True) # Field name made lowercase.
    directorszerosharesandtenureove0 = models.TextField(db_column='DIRECTORSZEROSHARESANDTENUREOVE0', blank=True) # Field name made lowercase.
    directorszerosharesandtenureove1 = models.TextField(db_column='DIRECTORSZEROSHARESANDTENUREOVE1', blank=True) # Field name made lowercase.
    directorszerosharesandtenureover = models.TextField(db_column='DIRECTORSZEROSHARESANDTENUREOVER', blank=True) # Field name made lowercase.
    dirleaddiraddtobase = models.TextField(db_column='DIRLEADDIRADDTOBASE', blank=True) # Field name made lowercase.
    dirleaddirectorfees = models.TextField(db_column='DIRLEADDIRECTORFEES', blank=True) # Field name made lowercase.
    dirstockaward = models.TextField(db_column='DIRSTOCKAWARD', blank=True) # Field name made lowercase.
    dirstockawardinitial = models.TextField(db_column='DIRSTOCKAWARDINITIAL', blank=True) # Field name made lowercase.
    dirstockawardpaidinyrinitial = models.TextField(db_column='DIRSTOCKAWARDPAIDINYRINITIAL', blank=True) # Field name made lowercase.
    dirstockoptionbsvalue = models.TextField(db_column='DIRSTOCKOPTIONBSVALUE', blank=True) # Field name made lowercase.
    dirstockoptionbsvalueinitial = models.TextField(db_column='DIRSTOCKOPTIONBSVALUEINITIAL', blank=True) # Field name made lowercase.
    dirstockoptionexprice = models.TextField(db_column='DIRSTOCKOPTIONEXPRICE', blank=True) # Field name made lowercase.
    dirstockoptionexpriceinitial = models.TextField(db_column='DIRSTOCKOPTIONEXPRICEINITIAL', blank=True) # Field name made lowercase.
    dirstockoptionnumber = models.TextField(db_column='DIRSTOCKOPTIONNUMBER', blank=True) # Field name made lowercase.
    dirstockoptionnumberinitial = models.TextField(db_column='DIRSTOCKOPTIONNUMBERINITIAL', blank=True) # Field name made lowercase.
    dirstockoptionvalue = models.TextField(db_column='DIRSTOCKOPTIONVALUE', blank=True) # Field name made lowercase.
    dirstockoptionvalueinitial = models.TextField(db_column='DIRSTOCKOPTIONVALUEINITIAL', blank=True) # Field name made lowercase.
    dirstockunitaward = models.TextField(db_column='DIRSTOCKUNITAWARD', blank=True) # Field name made lowercase.
    dirstockunitawardinitial = models.TextField(db_column='DIRSTOCKUNITAWARDINITIAL', blank=True) # Field name made lowercase.
    dividendyield = models.TextField(db_column='DIVIDENDYIELD', blank=True) # Field name made lowercase.
    dividendyld = models.TextField(db_column='DIVIDENDYLD', blank=True) # Field name made lowercase.
    dominantshareholder = models.TextField(db_column='DOMINANTSHAREHOLDER', blank=True) # Field name made lowercase.
    dominantshareholderpctg = models.TextField(db_column='DOMINANTSHAREHOLDERPCTG', blank=True) # Field name made lowercase.
    employees = models.TextField(db_column='EMPLOYEES', blank=True) # Field name made lowercase.
    exchange = models.TextField(db_column='EXCHANGE', blank=True) # Field name made lowercase.
    fiscalyrend = models.TextField(db_column='FISCALYREND', blank=True) # Field name made lowercase.
    float_shares = models.TextField(db_column='FLOAT_SHARES', blank=True) # Field name made lowercase.
    gcommitteetype = models.TextField(db_column='GCOMMITTEETYPE', blank=True) # Field name made lowercase.
    gencounselfname = models.TextField(db_column='GENCOUNSELFNAME', blank=True) # Field name made lowercase.
    gencounsellname = models.TextField(db_column='GENCOUNSELLNAME', blank=True) # Field name made lowercase.
    govpolicy = models.TextField(db_column='GOVPOLICY', blank=True) # Field name made lowercase.
    incorporationcountry = models.TextField(db_column='INCORPORATIONCOUNTRY', blank=True) # Field name made lowercase.
    indexedstock = models.TextField(db_column='INDEXEDSTOCK', blank=True) # Field name made lowercase.
    indexfortune = models.TextField(db_column='INDEXFORTUNE', blank=True) # Field name made lowercase.
    indexftglobal = models.TextField(db_column='INDEXFTGLOBAL', blank=True) # Field name made lowercase.
    indexrussell = models.TextField(db_column='INDEXRUSSELL', blank=True) # Field name made lowercase.
    indexsp = models.TextField(db_column='INDEXSP', blank=True) # Field name made lowercase.
    industry = models.TextField(db_column='INDUSTRY', blank=True) # Field name made lowercase.
    insiderscontrol = models.TextField(db_column='INSIDERSCONTROL', blank=True) # Field name made lowercase.
    insidersharesbought = models.TextField(db_column='INSIDERSHARESBOUGHT', blank=True) # Field name made lowercase.
    insidersharessold = models.TextField(db_column='INSIDERSHARESSOLD', blank=True) # Field name made lowercase.
    insiderspctg = models.TextField(db_column='INSIDERSPCTG', blank=True) # Field name made lowercase.
    insiderspluspctg = models.TextField(db_column='INSIDERSPLUSPCTG', blank=True) # Field name made lowercase.
    insidertransactionsdate = models.TextField(db_column='INSIDERTRANSACTIONSDATE', blank=True) # Field name made lowercase.
    institutionalmajority = models.TextField(db_column='INSTITUTIONALMAJORITY', blank=True) # Field name made lowercase.
    institutionpctg = models.TextField(db_column='INSTITUTIONPCTG', blank=True) # Field name made lowercase.
    leaddirectorfname = models.TextField(db_column='LEADDIRECTORFNAME', blank=True) # Field name made lowercase.
    leaddirectorindependent = models.TextField(db_column='LEADDIRECTORINDEPENDENT', blank=True) # Field name made lowercase.
    leaddirectorlname = models.TextField(db_column='LEADDIRECTORLNAME', blank=True) # Field name made lowercase.
    leadlawfirm = models.TextField(db_column='LEADLAWFIRM', blank=True) # Field name made lowercase.
    link20f = models.TextField(db_column='LINK20F', blank=True) # Field name made lowercase.
    linkannmtgwebcast = models.TextField(db_column='LINKANNMTGWEBCAST', blank=True) # Field name made lowercase.
    linkannualreport = models.TextField(db_column='LINKANNUALREPORT', blank=True) # Field name made lowercase.
    linkcomments = models.TextField(db_column='LINKCOMMENTS', blank=True) # Field name made lowercase.
    linkcomp = models.TextField(db_column='LINKCOMP', blank=True) # Field name made lowercase.
    linkcontract = models.TextField(db_column='LINKCONTRACT', blank=True) # Field name made lowercase.
    linkcountryprofile = models.TextField(db_column='LINKCOUNTRYPROFILE', blank=True) # Field name made lowercase.
    linkgovpolicy = models.TextField(db_column='LINKGOVPOLICY', blank=True) # Field name made lowercase.
    linkirpage = models.TextField(db_column='LINKIRPAGE', blank=True) # Field name made lowercase.
    linkproxy = models.TextField(db_column='LINKPROXY', blank=True) # Field name made lowercase.
    linkrelatedtransactions = models.TextField(db_column='LINKRELATEDTRANSACTIONS', blank=True) # Field name made lowercase.
    linksecfilings = models.TextField(db_column='LINKSECFILINGS', blank=True) # Field name made lowercase.
    linkshareprop = models.TextField(db_column='LINKSHAREPROP', blank=True) # Field name made lowercase.
    mailaddress = models.TextField(db_column='MAILADDRESS', blank=True) # Field name made lowercase.
    mailcity = models.TextField(db_column='MAILCITY', blank=True) # Field name made lowercase.
    mailcountry = models.TextField(db_column='MAILCOUNTRY', blank=True) # Field name made lowercase.
    mailfax = models.TextField(db_column='MAILFAX', blank=True) # Field name made lowercase.
    mailingaddress1a = models.TextField(db_column='MAILINGADDRESS1A', blank=True) # Field name made lowercase.
    mailingaddress2 = models.TextField(db_column='MAILINGADDRESS2', blank=True) # Field name made lowercase.
    mailphone = models.TextField(db_column='MAILPHONE', blank=True) # Field name made lowercase.
    mailpostcode = models.TextField(db_column='MAILPOSTCODE', blank=True) # Field name made lowercase.
    mailstate = models.TextField(db_column='MAILSTATE', blank=True) # Field name made lowercase.
    marketcap = models.TextField(db_column='MARKETCAP', blank=True) # Field name made lowercase.
    nacd = models.TextField(db_column='NACD', blank=True) # Field name made lowercase.
    notesceo = models.TextField(db_column='NOTESCEO', blank=True) # Field name made lowercase.
    notesdircomp = models.TextField(db_column='NOTESDIRCOMP', blank=True) # Field name made lowercase.
    novotes = models.TextField(db_column='NOVOTES', blank=True) # Field name made lowercase.
    optionsaccelerated = models.TextField(db_column='OPTIONSACCELERATED', blank=True) # Field name made lowercase.
    optionsaccelerateddate = models.TextField(db_column='OPTIONSACCELERATEDDATE', blank=True) # Field name made lowercase.
    optionsbackdating = models.TextField(db_column='OPTIONSBACKDATING', blank=True) # Field name made lowercase.
    optionsbackdatingsummary = models.TextField(db_column='OPTIONSBACKDATINGSUMMARY', blank=True) # Field name made lowercase.
    orgtype = models.TextField(db_column='ORGTYPE', blank=True) # Field name made lowercase.
    ownersfivepercentpctg = models.TextField(db_column='OWNERSFIVEPERCENTPCTG', blank=True) # Field name made lowercase.
    ownershipcategory = models.TextField(db_column='OWNERSHIPCATEGORY', blank=True) # Field name made lowercase.
    phone = models.TextField(db_column='PHONE', blank=True) # Field name made lowercase.
    phone_fax = models.TextField(db_column='PHONE_FAX', blank=True) # Field name made lowercase.
    postalcode = models.TextField(db_column='POSTALCODE', blank=True) # Field name made lowercase.
    pricebook = models.TextField(db_column='PRICEBOOK', blank=True) # Field name made lowercase.
    priceearnings = models.TextField(db_column='PRICEEARNINGS', blank=True) # Field name made lowercase.
    proxydate = models.TextField(db_column='PROXYDATE', blank=True) # Field name made lowercase.
    return1yr = models.TextField(db_column='RETURN1YR', blank=True) # Field name made lowercase.
    return3yr = models.TextField(db_column='RETURN3YR', blank=True) # Field name made lowercase.
    return5yr = models.TextField(db_column='RETURN5YR', blank=True) # Field name made lowercase.
    returnpeers1yr = models.TextField(db_column='RETURNPEERS1YR', blank=True) # Field name made lowercase.
    returnpeers3yr = models.TextField(db_column='RETURNPEERS3YR', blank=True) # Field name made lowercase.
    returnpeers5yr = models.TextField(db_column='RETURNPEERS5YR', blank=True) # Field name made lowercase.
    returnsp1yr = models.TextField(db_column='RETURNSP1YR', blank=True) # Field name made lowercase.
    returnsp3yr = models.TextField(db_column='RETURNSP3YR', blank=True) # Field name made lowercase.
    returnsp5yr = models.TextField(db_column='RETURNSP5YR', blank=True) # Field name made lowercase.
    revenues = models.TextField(db_column='REVENUES', blank=True) # Field name made lowercase.
    shareprice52wkhi = models.TextField(db_column='SHAREPRICE52WKHI', blank=True) # Field name made lowercase.
    shareprice52wklo = models.TextField(db_column='SHAREPRICE52WKLO', blank=True) # Field name made lowercase.
    sharepricecurrent = models.TextField(db_column='SHAREPRICECURRENT', blank=True) # Field name made lowercase.
    sharepriceyrend = models.TextField(db_column='SHAREPRICEYREND', blank=True) # Field name made lowercase.
    sharesdilution = models.TextField(db_column='SHARESDILUTION', blank=True) # Field name made lowercase.
    sharesoutstanding = models.TextField(db_column='SHARESOUTSTANDING', blank=True) # Field name made lowercase.
    sic = models.TextField(db_column='SIC', blank=True) # Field name made lowercase.
    sic1 = models.TextField(db_column='SIC1', blank=True) # Field name made lowercase.
    sic1descript = models.TextField(db_column='SIC1DESCRIPT', blank=True) # Field name made lowercase.
    sic2 = models.TextField(db_column='SIC2', blank=True) # Field name made lowercase.
    sic2descript = models.TextField(db_column='SIC2DESCRIPT', blank=True) # Field name made lowercase.
    sicdescription = models.TextField(db_column='SICDESCRIPTION', blank=True) # Field name made lowercase.
    soxcertification = models.TextField(db_column='SOXCERTIFICATION', blank=True) # Field name made lowercase.
    soxcompliance = models.TextField(db_column='SOXCOMPLIANCE', blank=True) # Field name made lowercase.
    soxloanscompliant = models.TextField(db_column='SOXLOANSCOMPLIANT', blank=True) # Field name made lowercase.
    state = models.TextField(db_column='STATE', blank=True) # Field name made lowercase.
    statehq = models.TextField(db_column='STATEHQ', blank=True) # Field name made lowercase.
    stateinc = models.TextField(db_column='STATEINC', blank=True) # Field name made lowercase.
    tddirelectionmajvote = models.TextField(db_column='TDDIRELECTIONMAJVOTE', blank=True) # Field name made lowercase.
    tddirelectionmajvotenotes = models.TextField(db_column='TDDIRELECTIONMAJVOTENOTES', blank=True) # Field name made lowercase.
    tddocumentnotations = models.TextField(db_column='TDDOCUMENTNOTATIONS', blank=True) # Field name made lowercase.
    tdpoisonpilldeadhand = models.TextField(db_column='TDPOISONPILLDEADHAND', blank=True) # Field name made lowercase.
    ticker = models.TextField(db_column='TICKER', blank=True) # Field name made lowercase.
    voteauditorno = models.TextField(db_column='VOTEAUDITORNO', blank=True) # Field name made lowercase.
    year = models.TextField(db_column='YEAR', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'wrds_companies'

class WrdsCompanies20012007(models.Model):
    ticker = models.TextField(db_column='TICKER', blank=True) # Field name made lowercase.
    companyname = models.TextField(db_column='COMPANYNAME', blank=True) # Field name made lowercase.
    year = models.TextField(db_column='YEAR', blank=True) # Field name made lowercase.
    annualmtgplace = models.TextField(db_column='ANNUALMTGPLACE', blank=True) # Field name made lowercase.
    auditor = models.TextField(db_column='AUDITOR', blank=True) # Field name made lowercase.
    auditorchangenotes = models.TextField(db_column='AUDITORCHANGENOTES', blank=True) # Field name made lowercase.
    cfolname = models.TextField(db_column='CFOLNAME', blank=True) # Field name made lowercase.
    cfoprofile = models.TextField(db_column='CFOPROFILE', blank=True) # Field name made lowercase.
    chairmanis = models.TextField(db_column='CHAIRMANIS', blank=True) # Field name made lowercase.
    industry = models.TextField(db_column='INDUSTRY', blank=True) # Field name made lowercase.
    leadlawfirm = models.TextField(db_column='LEADLAWFIRM', blank=True) # Field name made lowercase.
    mailcity = models.TextField(db_column='MAILCITY', blank=True) # Field name made lowercase.
    mailingaddress2 = models.TextField(db_column='MAILINGADDRESS2', blank=True) # Field name made lowercase.
    notesdircomp = models.TextField(db_column='NOTESDIRCOMP', blank=True) # Field name made lowercase.
    novotes = models.TextField(db_column='NOVOTES', blank=True) # Field name made lowercase.
    tddirelectionmajvote = models.TextField(db_column='TDDIRELECTIONMAJVOTE', blank=True) # Field name made lowercase.
    tddocumentnotations = models.TextField(db_column='TDDOCUMENTNOTATIONS', blank=True) # Field name made lowercase.
    cik = models.TextField(db_column='CIK', blank=True) # Field name made lowercase.
    adr = models.TextField(db_column='ADR', blank=True) # Field name made lowercase.
    annualmtg = models.TextField(db_column='ANNUALMTG', blank=True) # Field name made lowercase.
    bdclassified = models.TextField(db_column='BDCLASSIFIED', blank=True) # Field name made lowercase.
    bdoutsidemaj = models.TextField(db_column='BDOUTSIDEMAJ', blank=True) # Field name made lowercase.
    ceoage = models.TextField(db_column='CEOAGE', blank=True) # Field name made lowercase.
    ceoallothercomp = models.TextField(db_column='CEOALLOTHERCOMP', blank=True) # Field name made lowercase.
    ceoalltotalcompensation = models.TextField(db_column='CEOALLTOTALCOMPENSATION', blank=True) # Field name made lowercase.
    ceoannualbonus = models.TextField(db_column='CEOANNUALBONUS', blank=True) # Field name made lowercase.
    ceobasesalary = models.TextField(db_column='CEOBASESALARY', blank=True) # Field name made lowercase.
    ceofname = models.TextField(db_column='CEOFNAME', blank=True) # Field name made lowercase.
    ceohascontract = models.TextField(db_column='CEOHASCONTRACT', blank=True) # Field name made lowercase.
    ceohireyr = models.TextField(db_column='CEOHIREYR', blank=True) # Field name made lowercase.
    ceoischairman = models.TextField(db_column='CEOISCHAIRMAN', blank=True) # Field name made lowercase.
    ceolname = models.TextField(db_column='CEOLNAME', blank=True) # Field name made lowercase.
    ceooptionvaluerealized = models.TextField(db_column='CEOOPTIONVALUEREALIZED', blank=True) # Field name made lowercase.
    ceootherannualcomp = models.TextField(db_column='CEOOTHERANNUALCOMP', blank=True) # Field name made lowercase.
    ceoprofile = models.TextField(db_column='CEOPROFILE', blank=True) # Field name made lowercase.
    ceorestrictedstock = models.TextField(db_column='CEORESTRICTEDSTOCK', blank=True) # Field name made lowercase.
    ceosharesheld = models.TextField(db_column='CEOSHARESHELD', blank=True) # Field name made lowercase.
    ceosharesheldoptions = models.TextField(db_column='CEOSHARESHELDOPTIONS', blank=True) # Field name made lowercase.
    ceotenure = models.TextField(db_column='CEOTENURE', blank=True) # Field name made lowercase.
    ceototalannualcomp = models.TextField(db_column='CEOTOTALANNUALCOMP', blank=True) # Field name made lowercase.
    ceounexercisedoptions = models.TextField(db_column='CEOUNEXERCISEDOPTIONS', blank=True) # Field name made lowercase.
    cfofname = models.TextField(db_column='CFOFNAME', blank=True) # Field name made lowercase.
    chairmanfname = models.TextField(db_column='CHAIRMANFNAME', blank=True) # Field name made lowercase.
    chairmanlname = models.TextField(db_column='CHAIRMANLNAME', blank=True) # Field name made lowercase.
    committeeauditnotes = models.TextField(db_column='COMMITTEEAUDITNOTES', blank=True) # Field name made lowercase.
    committeecompensationnotes = models.TextField(db_column='COMMITTEECOMPENSATIONNOTES', blank=True) # Field name made lowercase.
    committeeexecutivenotes = models.TextField(db_column='COMMITTEEEXECUTIVENOTES', blank=True) # Field name made lowercase.
    committeegovernancenotes = models.TextField(db_column='COMMITTEEGOVERNANCENOTES', blank=True) # Field name made lowercase.
    committeemiscnotes = models.TextField(db_column='COMMITTEEMISCNOTES', blank=True) # Field name made lowercase.
    committeenominatingnotes = models.TextField(db_column='COMMITTEENOMINATINGNOTES', blank=True) # Field name made lowercase.
    companyage = models.TextField(db_column='COMPANYAGE', blank=True) # Field name made lowercase.
    compfounded = models.TextField(db_column='COMPFOUNDED', blank=True) # Field name made lowercase.
    corpsecretaryfname = models.TextField(db_column='CORPSECRETARYFNAME', blank=True) # Field name made lowercase.
    corpsecretarylname = models.TextField(db_column='CORPSECRETARYLNAME', blank=True) # Field name made lowercase.
    country = models.TextField(db_column='COUNTRY', blank=True) # Field name made lowercase.
    currentyear = models.TextField(db_column='CURRENTYEAR', blank=True) # Field name made lowercase.
    dirbasepay = models.TextField(db_column='DIRBASEPAY', blank=True) # Field name made lowercase.
    directorsactiveceos = models.TextField(db_column='DIRECTORSACTIVECEOS', blank=True) # Field name made lowercase.
    directorsfailed = models.TextField(db_column='DIRECTORSFAILED', blank=True) # Field name made lowercase.
    directorsminority = models.TextField(db_column='DIRECTORSMINORITY', blank=True) # Field name made lowercase.
    directorsoutside = models.TextField(db_column='DIRECTORSOUTSIDE', blank=True) # Field name made lowercase.
    directorsoutsiderelated = models.TextField(db_column='DIRECTORSOUTSIDERELATED', blank=True) # Field name made lowercase.
    directorsoutsidetotal = models.TextField(db_column='DIRECTORSOUTSIDETOTAL', blank=True) # Field name made lowercase.
    directorsover15yrstenure = models.TextField(db_column='DIRECTORSOVER15YRSTENURE', blank=True) # Field name made lowercase.
    directorsover4boards = models.TextField(db_column='DIRECTORSOVER4BOARDS', blank=True) # Field name made lowercase.
    directorsover70 = models.TextField(db_column='DIRECTORSOVER70', blank=True) # Field name made lowercase.
    directorstotal = models.TextField(db_column='DIRECTORSTOTAL', blank=True) # Field name made lowercase.
    directorswomen = models.TextField(db_column='DIRECTORSWOMEN', blank=True) # Field name made lowercase.
    directorszeroshares = models.TextField(db_column='DIRECTORSZEROSHARES', blank=True) # Field name made lowercase.
    employees = models.TextField(db_column='EMPLOYEES', blank=True) # Field name made lowercase.
    exchange = models.TextField(db_column='EXCHANGE', blank=True) # Field name made lowercase.
    gencounselfname = models.TextField(db_column='GENCOUNSELFNAME', blank=True) # Field name made lowercase.
    gencounsellname = models.TextField(db_column='GENCOUNSELLNAME', blank=True) # Field name made lowercase.
    govpolicy = models.TextField(db_column='GOVPOLICY', blank=True) # Field name made lowercase.
    indexedstock = models.TextField(db_column='INDEXEDSTOCK', blank=True) # Field name made lowercase.
    indexfortune = models.TextField(db_column='INDEXFORTUNE', blank=True) # Field name made lowercase.
    indexsp = models.TextField(db_column='INDEXSP', blank=True) # Field name made lowercase.
    insiderspctg = models.TextField(db_column='INSIDERSPCTG', blank=True) # Field name made lowercase.
    institutionpctg = models.TextField(db_column='INSTITUTIONPCTG', blank=True) # Field name made lowercase.
    leaddirectorfname = models.TextField(db_column='LEADDIRECTORFNAME', blank=True) # Field name made lowercase.
    leaddirectorlname = models.TextField(db_column='LEADDIRECTORLNAME', blank=True) # Field name made lowercase.
    linkcomp = models.TextField(db_column='LINKCOMP', blank=True) # Field name made lowercase.
    linkcontract = models.TextField(db_column='LINKCONTRACT', blank=True) # Field name made lowercase.
    linkgovpolicy = models.TextField(db_column='LINKGOVPOLICY', blank=True) # Field name made lowercase.
    linkproxy = models.TextField(db_column='LINKPROXY', blank=True) # Field name made lowercase.
    linkshareprop = models.TextField(db_column='LINKSHAREPROP', blank=True) # Field name made lowercase.
    mailaddress = models.TextField(db_column='MAILADDRESS', blank=True) # Field name made lowercase.
    mailcountry = models.TextField(db_column='MAILCOUNTRY', blank=True) # Field name made lowercase.
    mailfax = models.TextField(db_column='MAILFAX', blank=True) # Field name made lowercase.
    mailphone = models.TextField(db_column='MAILPHONE', blank=True) # Field name made lowercase.
    mailpostcode = models.TextField(db_column='MAILPOSTCODE', blank=True) # Field name made lowercase.
    mailstate = models.TextField(db_column='MAILSTATE', blank=True) # Field name made lowercase.
    marketcap = models.TextField(db_column='MARKETCAP', blank=True) # Field name made lowercase.
    orgtype = models.TextField(db_column='ORGTYPE', blank=True) # Field name made lowercase.
    proxydate = models.TextField(db_column='PROXYDATE', blank=True) # Field name made lowercase.
    returnpeers1yr = models.TextField(db_column='RETURNPEERS1YR', blank=True) # Field name made lowercase.
    returnpeers3yr = models.TextField(db_column='RETURNPEERS3YR', blank=True) # Field name made lowercase.
    returnpeers5yr = models.TextField(db_column='RETURNPEERS5YR', blank=True) # Field name made lowercase.
    returnsp1yr = models.TextField(db_column='RETURNSP1YR', blank=True) # Field name made lowercase.
    returnsp3yr = models.TextField(db_column='RETURNSP3YR', blank=True) # Field name made lowercase.
    returnsp5yr = models.TextField(db_column='RETURNSP5YR', blank=True) # Field name made lowercase.
    sharepriceyrend = models.TextField(db_column='SHAREPRICEYREND', blank=True) # Field name made lowercase.
    sic1 = models.TextField(db_column='SIC1', blank=True) # Field name made lowercase.
    sic1descript = models.TextField(db_column='SIC1DESCRIPT', blank=True) # Field name made lowercase.
    sic2 = models.TextField(db_column='SIC2', blank=True) # Field name made lowercase.
    sic2descript = models.TextField(db_column='SIC2DESCRIPT', blank=True) # Field name made lowercase.
    statehq = models.TextField(db_column='STATEHQ', blank=True) # Field name made lowercase.
    stateinc = models.TextField(db_column='STATEINC', blank=True) # Field name made lowercase.
    priceearnings = models.TextField(db_column='PRICEEARNINGS', blank=True) # Field name made lowercase.
    fiscalyrend = models.TextField(db_column='FISCALYREND', blank=True) # Field name made lowercase.
    return1yr = models.TextField(db_column='RETURN1YR', blank=True) # Field name made lowercase.
    return3yr = models.TextField(db_column='RETURN3YR', blank=True) # Field name made lowercase.
    return5yr = models.TextField(db_column='RETURN5YR', blank=True) # Field name made lowercase.
    cusip = models.TextField(db_column='CUSIP', blank=True) # Field name made lowercase.
    auditfees = models.TextField(db_column='AUDITFEES', blank=True) # Field name made lowercase.
    auditfeesit = models.TextField(db_column='AUDITFEESIT', blank=True) # Field name made lowercase.
    auditfeesother = models.TextField(db_column='AUDITFEESOTHER', blank=True) # Field name made lowercase.
    auditfeesprcntg = models.TextField(db_column='AUDITFEESPRCNTG', blank=True) # Field name made lowercase.
    auditfeestotal = models.TextField(db_column='AUDITFEESTOTAL', blank=True) # Field name made lowercase.
    ceoannoptiongrant = models.TextField(db_column='CEOANNOPTIONGRANT', blank=True) # Field name made lowercase.
    indexrussell = models.TextField(db_column='INDEXRUSSELL', blank=True) # Field name made lowercase.
    link20f = models.TextField(db_column='LINK20F', blank=True) # Field name made lowercase.
    linkannualreport = models.TextField(db_column='LINKANNUALREPORT', blank=True) # Field name made lowercase.
    notesceo = models.TextField(db_column='NOTESCEO', blank=True) # Field name made lowercase.
    indexftglobal = models.TextField(db_column='INDEXFTGLOBAL', blank=True) # Field name made lowercase.
    insiderscontrol = models.TextField(db_column='INSIDERSCONTROL', blank=True) # Field name made lowercase.
    insidersharesbought = models.TextField(db_column='INSIDERSHARESBOUGHT', blank=True) # Field name made lowercase.
    insidersharessold = models.TextField(db_column='INSIDERSHARESSOLD', blank=True) # Field name made lowercase.
    insidertransactionsdate = models.TextField(db_column='INSIDERTRANSACTIONSDATE', blank=True) # Field name made lowercase.
    insiderspluspctg = models.TextField(db_column='INSIDERSPLUSPCTG', blank=True) # Field name made lowercase.
    institutionalmajority = models.TextField(db_column='INSTITUTIONALMAJORITY', blank=True) # Field name made lowercase.
    nacd = models.TextField(db_column='NACD', blank=True) # Field name made lowercase.
    revenues = models.TextField(db_column='REVENUES', blank=True) # Field name made lowercase.
    sharesoutstanding = models.TextField(db_column='SHARESOUTSTANDING', blank=True) # Field name made lowercase.
    auditorindependent = models.TextField(db_column='AUDITORINDEPENDENT', blank=True) # Field name made lowercase.
    auditorprevious = models.TextField(db_column='AUDITORPREVIOUS', blank=True) # Field name made lowercase.
    bdmtgs = models.TextField(db_column='BDMTGS', blank=True) # Field name made lowercase.
    bdmtgsoutside = models.TextField(db_column='BDMTGSOUTSIDE', blank=True) # Field name made lowercase.
    bdoutsidemeets = models.TextField(db_column='BDOUTSIDEMEETS', blank=True) # Field name made lowercase.
    cochairmanfname = models.TextField(db_column='COCHAIRMANFNAME', blank=True) # Field name made lowercase.
    cochairmanlname = models.TextField(db_column='COCHAIRMANLNAME', blank=True) # Field name made lowercase.
    busethicscode = models.TextField(db_column='BUSETHICSCODE', blank=True) # Field name made lowercase.
    commauditindependent = models.TextField(db_column='COMMAUDITINDEPENDENT', blank=True) # Field name made lowercase.
    commcompindependent = models.TextField(db_column='COMMCOMPINDEPENDENT', blank=True) # Field name made lowercase.
    commnomgovindependent = models.TextField(db_column='COMMNOMGOVINDEPENDENT', blank=True) # Field name made lowercase.
    compplanapproval = models.TextField(db_column='COMPPLANAPPROVAL', blank=True) # Field name made lowercase.
    dominantshareholder = models.TextField(db_column='DOMINANTSHAREHOLDER', blank=True) # Field name made lowercase.
    dominantshareholderpctg = models.TextField(db_column='DOMINANTSHAREHOLDERPCTG', blank=True) # Field name made lowercase.
    linkannmtgwebcast = models.TextField(db_column='LINKANNMTGWEBCAST', blank=True) # Field name made lowercase.
    linkcomments = models.TextField(db_column='LINKCOMMENTS', blank=True) # Field name made lowercase.
    linkcountryprofile = models.TextField(db_column='LINKCOUNTRYPROFILE', blank=True) # Field name made lowercase.
    linkirpage = models.TextField(db_column='LINKIRPAGE', blank=True) # Field name made lowercase.
    linkrelatedtransactions = models.TextField(db_column='LINKRELATEDTRANSACTIONS', blank=True) # Field name made lowercase.
    linksecfilings = models.TextField(db_column='LINKSECFILINGS', blank=True) # Field name made lowercase.
    soxcertification = models.TextField(db_column='SOXCERTIFICATION', blank=True) # Field name made lowercase.
    soxcompliance = models.TextField(db_column='SOXCOMPLIANCE', blank=True) # Field name made lowercase.
    soxloanscompliant = models.TextField(db_column='SOXLOANSCOMPLIANT', blank=True) # Field name made lowercase.
    ceocomphighlights = models.TextField(db_column='CEOCOMPHIGHLIGHTS', blank=True) # Field name made lowercase.
    ceoltipawardedinyear = models.TextField(db_column='CEOLTIPAWARDEDINYEAR', blank=True) # Field name made lowercase.
    ceoltippayout = models.TextField(db_column='CEOLTIPPAYOUT', blank=True) # Field name made lowercase.
    ceoltipvestedinyear = models.TextField(db_column='CEOLTIPVESTEDINYEAR', blank=True) # Field name made lowercase.
    ceosharesheldlastyear = models.TextField(db_column='CEOSHARESHELDLASTYEAR', blank=True) # Field name made lowercase.
    ceosharestopaymultiple = models.TextField(db_column='CEOSHARESTOPAYMULTIPLE', blank=True) # Field name made lowercase.
    ceovariablepayasstock = models.TextField(db_column='CEOVARIABLEPAYASSTOCK', blank=True) # Field name made lowercase.
    ceovariabletototalpaymultiple = models.TextField(db_column='CEOVARIABLETOTOTALPAYMULTIPLE', blank=True) # Field name made lowercase.
    ceopreviousfname = models.TextField(db_column='CEOPREVIOUSFNAME', blank=True) # Field name made lowercase.
    ceopreviouslname = models.TextField(db_column='CEOPREVIOUSLNAME', blank=True) # Field name made lowercase.
    ceoprevioustenure = models.TextField(db_column='CEOPREVIOUSTENURE', blank=True) # Field name made lowercase.
    mailingaddress1a = models.TextField(db_column='MAILINGADDRESS1A', blank=True) # Field name made lowercase.
    ownershipcategory = models.TextField(db_column='OWNERSHIPCATEGORY', blank=True) # Field name made lowercase.
    sicdescription = models.TextField(db_column='SICDESCRIPTION', blank=True) # Field name made lowercase.
    auditfeesrelated = models.TextField(db_column='AUDITFEESRELATED', blank=True) # Field name made lowercase.
    auditfeestax = models.TextField(db_column='AUDITFEESTAX', blank=True) # Field name made lowercase.
    cfoage = models.TextField(db_column='CFOAGE', blank=True) # Field name made lowercase.
    cfotenure = models.TextField(db_column='CFOTENURE', blank=True) # Field name made lowercase.
    companyfedid = models.TextField(db_column='COMPANYFEDID', blank=True) # Field name made lowercase.
    directorsproblem = models.TextField(db_column='DIRECTORSPROBLEM', blank=True) # Field name made lowercase.
    float_shares = models.TextField(db_column='FLOAT_SHARES', blank=True) # Field name made lowercase.
    ownersfivepercentpctg = models.TextField(db_column='OWNERSFIVEPERCENTPCTG', blank=True) # Field name made lowercase.
    pricebook = models.TextField(db_column='PRICEBOOK', blank=True) # Field name made lowercase.
    shareprice52wkhi = models.TextField(db_column='SHAREPRICE52WKHI', blank=True) # Field name made lowercase.
    shareprice52wklo = models.TextField(db_column='SHAREPRICE52WKLO', blank=True) # Field name made lowercase.
    sharepricecurrent = models.TextField(db_column='SHAREPRICECURRENT', blank=True) # Field name made lowercase.
    sic = models.TextField(db_column='SIC', blank=True) # Field name made lowercase.
    compdescription = models.TextField(db_column='COMPDESCRIPTION', blank=True) # Field name made lowercase.
    directorsinside = models.TextField(db_column='DIRECTORSINSIDE', blank=True) # Field name made lowercase.
    auditornominee = models.TextField(db_column='AUDITORNOMINEE', blank=True) # Field name made lowercase.
    bdoutsidemajstrict = models.TextField(db_column='BDOUTSIDEMAJSTRICT', blank=True) # Field name made lowercase.
    bdoutsidemtgsource = models.TextField(db_column='BDOUTSIDEMTGSOURCE', blank=True) # Field name made lowercase.
    chiefgovofficerfname = models.TextField(db_column='CHIEFGOVOFFICERFNAME', blank=True) # Field name made lowercase.
    chiefgovofficerlname = models.TextField(db_column='CHIEFGOVOFFICERLNAME', blank=True) # Field name made lowercase.
    commauditfullyindependent = models.TextField(db_column='COMMAUDITFULLYINDEPENDENT', blank=True) # Field name made lowercase.
    commcompfullyindependent = models.TextField(db_column='COMMCOMPFULLYINDEPENDENT', blank=True) # Field name made lowercase.
    commnomgovfullyindependent = models.TextField(db_column='COMMNOMGOVFULLYINDEPENDENT', blank=True) # Field name made lowercase.
    companyprofileshort = models.TextField(db_column='COMPANYPROFILESHORT', blank=True) # Field name made lowercase.
    companyprofiletodcalc = models.TextField(db_column='COMPANYPROFILETODCALC', blank=True) # Field name made lowercase.
    controlledcompanyexemption = models.TextField(db_column='CONTROLLEDCOMPANYEXEMPTION', blank=True) # Field name made lowercase.
    dc_committeemtgretainerchaira = models.TextField(db_column='DC_COMMITTEEMTGRETAINERCHAIRA', blank=True) # Field name made lowercase.
    dc_committeemtgretainerchairc = models.TextField(db_column='DC_COMMITTEEMTGRETAINERCHAIRC', blank=True) # Field name made lowercase.
    dc_committeemtgretainerchaire = models.TextField(db_column='DC_COMMITTEEMTGRETAINERCHAIRE', blank=True) # Field name made lowercase.
    dc_committeemtgretainerchairg = models.TextField(db_column='DC_COMMITTEEMTGRETAINERCHAIRG', blank=True) # Field name made lowercase.
    dc_committeemtgretainerchairn = models.TextField(db_column='DC_COMMITTEEMTGRETAINERCHAIRN', blank=True) # Field name made lowercase.
    dc_committeemtgretainerdira = models.TextField(db_column='DC_COMMITTEEMTGRETAINERDIRA', blank=True) # Field name made lowercase.
    dc_committeemtgretainerdirc = models.TextField(db_column='DC_COMMITTEEMTGRETAINERDIRC', blank=True) # Field name made lowercase.
    dc_committeemtgretainerdire = models.TextField(db_column='DC_COMMITTEEMTGRETAINERDIRE', blank=True) # Field name made lowercase.
    dc_committeemtgretainerdirg = models.TextField(db_column='DC_COMMITTEEMTGRETAINERDIRG', blank=True) # Field name made lowercase.
    dc_committeemtgretainerdirn = models.TextField(db_column='DC_COMMITTEEMTGRETAINERDIRN', blank=True) # Field name made lowercase.
    dc_overrideoptionstotal = models.TextField(db_column='DC_OVERRIDEOPTIONSTOTAL', blank=True) # Field name made lowercase.
    dividendyld = models.TextField(db_column='DIVIDENDYLD', blank=True) # Field name made lowercase.
    gcommitteetype = models.TextField(db_column='GCOMMITTEETYPE', blank=True) # Field name made lowercase.
    leaddirectorindependent = models.TextField(db_column='LEADDIRECTORINDEPENDENT', blank=True) # Field name made lowercase.
    optionsaccelerated = models.TextField(db_column='OPTIONSACCELERATED', blank=True) # Field name made lowercase.
    optionsbackdating = models.TextField(db_column='OPTIONSBACKDATING', blank=True) # Field name made lowercase.
    optionsbackdatingsummary = models.TextField(db_column='OPTIONSBACKDATINGSUMMARY', blank=True) # Field name made lowercase.
    tddirelectionmajvotenotes = models.TextField(db_column='TDDIRELECTIONMAJVOTENOTES', blank=True) # Field name made lowercase.
    tdpoisonpilldeadhand = models.TextField(db_column='TDPOISONPILLDEADHAND', blank=True) # Field name made lowercase.
    annualmtgnext = models.TextField(db_column='ANNUALMTGNEXT', blank=True) # Field name made lowercase.
    auditnonauditfeespctg = models.TextField(db_column='AUDITNONAUDITFEESPCTG', blank=True) # Field name made lowercase.
    auditorsince = models.TextField(db_column='AUDITORSINCE', blank=True) # Field name made lowercase.
    directorsactiveceopct = models.TextField(db_column='DIRECTORSACTIVECEOPCT', blank=True) # Field name made lowercase.
    directorsfailedpct = models.TextField(db_column='DIRECTORSFAILEDPCT', blank=True) # Field name made lowercase.
    directorsinsidepct = models.TextField(db_column='DIRECTORSINSIDEPCT', blank=True) # Field name made lowercase.
    directorsoutsiderelatedpct = models.TextField(db_column='DIRECTORSOUTSIDERELATEDPCT', blank=True) # Field name made lowercase.
    directorsover10yrstenure = models.TextField(db_column='DIRECTORSOVER10YRSTENURE', blank=True) # Field name made lowercase.
    directorsover10yrstenurepct = models.TextField(db_column='DIRECTORSOVER10YRSTENUREPCT', blank=True) # Field name made lowercase.
    directorsover15yrstenurepct = models.TextField(db_column='DIRECTORSOVER15YRSTENUREPCT', blank=True) # Field name made lowercase.
    directorsover3boards = models.TextField(db_column='DIRECTORSOVER3BOARDS', blank=True) # Field name made lowercase.
    directorsover4publicboards = models.TextField(db_column='DIRECTORSOVER4PUBLICBOARDS', blank=True) # Field name made lowercase.
    directorsover4publicboardspct = models.TextField(db_column='DIRECTORSOVER4PUBLICBOARDSPCT', blank=True) # Field name made lowercase.
    directorsover70pct = models.TextField(db_column='DIRECTORSOVER70PCT', blank=True) # Field name made lowercase.
    directorsproblempct = models.TextField(db_column='DIRECTORSPROBLEMPCT', blank=True) # Field name made lowercase.
    directorswomenpct = models.TextField(db_column='DIRECTORSWOMENPCT', blank=True) # Field name made lowercase.
    directorszerosharesandtenureover = models.TextField(db_column='DIRECTORSZEROSHARESANDTENUREOVER', blank=True) # Field name made lowercase.
    directorszerosharesandtenureove0 = models.TextField(db_column='DIRECTORSZEROSHARESANDTENUREOVE0', blank=True) # Field name made lowercase.
    dc_avgdircomp = models.TextField(db_column='DC_AVGDIRCOMP', blank=True) # Field name made lowercase.
    dc_directorscompensated = models.TextField(db_column='DC_DIRECTORSCOMPENSATED', blank=True) # Field name made lowercase.
    dc_directorsreceivinginitialawar = models.TextField(db_column='DC_DIRECTORSRECEIVINGINITIALAWAR', blank=True) # Field name made lowercase.
    dc_stockawardoverridetotals = models.TextField(db_column='DC_STOCKAWARDOVERRIDETOTALS', blank=True) # Field name made lowercase.
    dc_totalmtgfeespaid = models.TextField(db_column='DC_TOTALMTGFEESPAID', blank=True) # Field name made lowercase.
    dividendyield = models.TextField(db_column='DIVIDENDYIELD', blank=True) # Field name made lowercase.
    sharesdilution = models.TextField(db_column='SHARESDILUTION', blank=True) # Field name made lowercase.
    dc_committeemtgfeeschaira = models.TextField(db_column='DC_COMMITTEEMTGFEESCHAIRA', blank=True) # Field name made lowercase.
    dc_committeemtgfeeschairc = models.TextField(db_column='DC_COMMITTEEMTGFEESCHAIRC', blank=True) # Field name made lowercase.
    dc_committeemtgfeeschaire = models.TextField(db_column='DC_COMMITTEEMTGFEESCHAIRE', blank=True) # Field name made lowercase.
    dc_committeemtgfeeschairg = models.TextField(db_column='DC_COMMITTEEMTGFEESCHAIRG', blank=True) # Field name made lowercase.
    dc_committeemtgfeeschairn = models.TextField(db_column='DC_COMMITTEEMTGFEESCHAIRN', blank=True) # Field name made lowercase.
    dc_committeemtgfeesdira = models.TextField(db_column='DC_COMMITTEEMTGFEESDIRA', blank=True) # Field name made lowercase.
    dc_committeemtgfeesdirc = models.TextField(db_column='DC_COMMITTEEMTGFEESDIRC', blank=True) # Field name made lowercase.
    dc_committeemtgfeesdire = models.TextField(db_column='DC_COMMITTEEMTGFEESDIRE', blank=True) # Field name made lowercase.
    dc_committeemtgfeesdirg = models.TextField(db_column='DC_COMMITTEEMTGFEESDIRG', blank=True) # Field name made lowercase.
    dc_committeemtgfeesdirn = models.TextField(db_column='DC_COMMITTEEMTGFEESDIRN', blank=True) # Field name made lowercase.
    optionsaccelerateddate = models.TextField(db_column='OPTIONSACCELERATEDDATE', blank=True) # Field name made lowercase.
    dirleaddiraddtobase = models.TextField(db_column='DIRLEADDIRADDTOBASE', blank=True) # Field name made lowercase.
    dirstockawardpaidinyrinitial = models.TextField(db_column='DIRSTOCKAWARDPAIDINYRINITIAL', blank=True) # Field name made lowercase.
    dirbdmtgfees = models.TextField(db_column='DIRBDMTGFEES', blank=True) # Field name made lowercase.
    dirleaddirectorfees = models.TextField(db_column='DIRLEADDIRECTORFEES', blank=True) # Field name made lowercase.
    dirstockaward = models.TextField(db_column='DIRSTOCKAWARD', blank=True) # Field name made lowercase.
    dirstockawardinitial = models.TextField(db_column='DIRSTOCKAWARDINITIAL', blank=True) # Field name made lowercase.
    dirstockoptionbsvalue = models.TextField(db_column='DIRSTOCKOPTIONBSVALUE', blank=True) # Field name made lowercase.
    dirstockoptionbsvalueinitial = models.TextField(db_column='DIRSTOCKOPTIONBSVALUEINITIAL', blank=True) # Field name made lowercase.
    dirstockoptionexprice = models.TextField(db_column='DIRSTOCKOPTIONEXPRICE', blank=True) # Field name made lowercase.
    dirstockoptionexpriceinitial = models.TextField(db_column='DIRSTOCKOPTIONEXPRICEINITIAL', blank=True) # Field name made lowercase.
    dirstockoptionnumber = models.TextField(db_column='DIRSTOCKOPTIONNUMBER', blank=True) # Field name made lowercase.
    dirstockoptionnumberinitial = models.TextField(db_column='DIRSTOCKOPTIONNUMBERINITIAL', blank=True) # Field name made lowercase.
    dirstockoptionvalue = models.TextField(db_column='DIRSTOCKOPTIONVALUE', blank=True) # Field name made lowercase.
    dirstockoptionvalueinitial = models.TextField(db_column='DIRSTOCKOPTIONVALUEINITIAL', blank=True) # Field name made lowercase.
    dirstockunitaward = models.TextField(db_column='DIRSTOCKUNITAWARD', blank=True) # Field name made lowercase.
    dirstockunitawardinitial = models.TextField(db_column='DIRSTOCKUNITAWARDINITIAL', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'wrds_companies_2001_2007'

class WrdsCompanies2008(models.Model):
    ticker = models.TextField(blank=True)
    companyname = models.TextField(db_column='companyName', blank=True) # Field name made lowercase.
    cik = models.TextField(blank=True)
    cusip = models.TextField(blank=True)
    adr = models.TextField(db_column='ADR', blank=True) # Field name made lowercase.
    annualmtgplace = models.TextField(db_column='AnnualMtgPlace', blank=True) # Field name made lowercase.
    auditor = models.TextField(db_column='Auditor', blank=True) # Field name made lowercase.
    auditorchangenotes = models.TextField(db_column='AuditorChangeNotes', blank=True) # Field name made lowercase.
    auditorindependent = models.TextField(db_column='AuditorIndependent', blank=True) # Field name made lowercase.
    auditornominee = models.TextField(db_column='AuditorNominee', blank=True) # Field name made lowercase.
    auditorprevious = models.TextField(db_column='AuditorPrevious', blank=True) # Field name made lowercase.
    bdoutsidemeets = models.TextField(db_column='BDOutsideMeets', blank=True) # Field name made lowercase.
    bdoutsidemaj = models.TextField(db_column='BdOutsideMaj', blank=True) # Field name made lowercase.
    bdoutsidemajstrict = models.TextField(db_column='BdOutsideMajStrict', blank=True) # Field name made lowercase.
    bdoutsidemtgsource = models.TextField(db_column='BdOutsideMtgSource', blank=True) # Field name made lowercase.
    busethicscode = models.TextField(db_column='BusEthicsCode', blank=True) # Field name made lowercase.
    cfofname = models.TextField(db_column='CFOFName', blank=True) # Field name made lowercase.
    cfolname = models.TextField(db_column='CFOLName', blank=True) # Field name made lowercase.
    cfoprofile = models.TextField(db_column='CFOProfile', blank=True) # Field name made lowercase.
    chairmanfname = models.TextField(db_column='ChairmanFName', blank=True) # Field name made lowercase.
    chairmanis = models.TextField(db_column='ChairmanIs', blank=True) # Field name made lowercase.
    chairmanlname = models.TextField(db_column='ChairmanLName', blank=True) # Field name made lowercase.
    chiefgovofficerfname = models.TextField(db_column='ChiefGovOfficerFName', blank=True) # Field name made lowercase.
    chiefgovofficerlname = models.TextField(db_column='ChiefGovOfficerLName', blank=True) # Field name made lowercase.
    cochairmanfname = models.TextField(db_column='CoChairmanFName', blank=True) # Field name made lowercase.
    cochairmanlname = models.TextField(db_column='CoChairmanLName', blank=True) # Field name made lowercase.
    commauditfullyindependent = models.TextField(db_column='CommAuditFullyIndependent', blank=True) # Field name made lowercase.
    commauditindependent = models.TextField(db_column='CommAuditIndependent', blank=True) # Field name made lowercase.
    commcompfullyindependent = models.TextField(db_column='CommCompFullyIndependent', blank=True) # Field name made lowercase.
    commcompindependent = models.TextField(db_column='CommCompIndependent', blank=True) # Field name made lowercase.
    commnomgovfullyindependent = models.TextField(db_column='CommNomGovFullyIndependent', blank=True) # Field name made lowercase.
    commnomgovindependent = models.TextField(db_column='CommNomGovIndependent', blank=True) # Field name made lowercase.
    compdescription = models.TextField(db_column='CompDescription', blank=True) # Field name made lowercase.
    compplanapproval = models.TextField(db_column='CompPlanApproval', blank=True) # Field name made lowercase.
    companyfedid = models.TextField(db_column='CompanyFedID', blank=True) # Field name made lowercase.
    companyprofileshort = models.TextField(db_column='CompanyProfileShort', blank=True) # Field name made lowercase.
    companyprofiletodcalc = models.TextField(db_column='CompanyProfileTODCalc', blank=True) # Field name made lowercase.
    controlledcompanyexemption = models.TextField(db_column='ControlledCompanyExemption', blank=True) # Field name made lowercase.
    corpsecretaryfname = models.TextField(db_column='CorpSecretaryFName', blank=True) # Field name made lowercase.
    corpsecretarylname = models.TextField(db_column='CorpSecretaryLName', blank=True) # Field name made lowercase.
    country = models.TextField(db_column='Country', blank=True) # Field name made lowercase.
    dirleaddiraddtobase = models.TextField(db_column='DirLeadDirAddToBase', blank=True) # Field name made lowercase.
    dirstockawardpaidinyrinitial = models.TextField(db_column='DirStockAwardPaidInYrInitial', blank=True) # Field name made lowercase.
    exchange = models.TextField(db_column='Exchange', blank=True) # Field name made lowercase.
    gencounselfname = models.TextField(db_column='GenCounselFName', blank=True) # Field name made lowercase.
    gencounsellname = models.TextField(db_column='GenCounselLName', blank=True) # Field name made lowercase.
    govpolicy = models.TextField(db_column='GovPolicy', blank=True) # Field name made lowercase.
    indexrussell = models.TextField(db_column='IndexRussell', blank=True) # Field name made lowercase.
    indexsp = models.TextField(db_column='IndexSP', blank=True) # Field name made lowercase.
    indexedstock = models.TextField(db_column='IndexedStock', blank=True) # Field name made lowercase.
    industry = models.TextField(db_column='Industry', blank=True) # Field name made lowercase.
    insiderscontrol = models.TextField(db_column='InsidersControl', blank=True) # Field name made lowercase.
    institutionalmajority = models.TextField(db_column='InstitutionalMajority', blank=True) # Field name made lowercase.
    leaddirectorfname = models.TextField(db_column='LeadDirectorFName', blank=True) # Field name made lowercase.
    leaddirectorindependent = models.TextField(db_column='LeadDirectorIndependent', blank=True) # Field name made lowercase.
    leaddirectorlname = models.TextField(db_column='LeadDirectorLName', blank=True) # Field name made lowercase.
    leadlawfirm = models.TextField(db_column='LeadLawFirm', blank=True) # Field name made lowercase.
    mailaddress = models.TextField(db_column='MailAddress', blank=True) # Field name made lowercase.
    mailcity = models.TextField(db_column='MailCity', blank=True) # Field name made lowercase.
    mailcountry = models.TextField(db_column='MailCountry', blank=True) # Field name made lowercase.
    mailfax = models.TextField(db_column='MailFax', blank=True) # Field name made lowercase.
    mailphone = models.TextField(db_column='MailPhone', blank=True) # Field name made lowercase.
    mailstate = models.TextField(db_column='MailState', blank=True) # Field name made lowercase.
    mailingaddress2 = models.TextField(db_column='MailingAddress2', blank=True) # Field name made lowercase.
    mailingaddress1a = models.TextField(db_column='MailingAddress1a', blank=True) # Field name made lowercase.
    novotes = models.TextField(db_column='NoVotes', blank=True) # Field name made lowercase.
    notesdircomp = models.TextField(db_column='NotesDirComp', blank=True) # Field name made lowercase.
    optionsaccelerated = models.TextField(db_column='OptionsAccelerated', blank=True) # Field name made lowercase.
    optionsbackdating = models.TextField(db_column='OptionsBackdating', blank=True) # Field name made lowercase.
    optionsbackdatingsummary = models.TextField(db_column='OptionsBackdatingSummary', blank=True) # Field name made lowercase.
    ownershipcategory = models.TextField(db_column='OwnershipCategory', blank=True) # Field name made lowercase.
    sicdescription = models.TextField(db_column='SICDescription', blank=True) # Field name made lowercase.
    statehq = models.TextField(db_column='StateHQ', blank=True) # Field name made lowercase.
    stateinc = models.TextField(db_column='StateInc', blank=True) # Field name made lowercase.
    tddirelectionmajvote = models.TextField(db_column='TDDirElectionMajVote', blank=True) # Field name made lowercase.
    tddirelectionmajvotenotes = models.TextField(db_column='TDDirElectionMajVoteNotes', blank=True) # Field name made lowercase.
    tddocumentnotations = models.TextField(db_column='TDDocumentNotations', blank=True) # Field name made lowercase.
    tdpoisonpilldeadhand = models.TextField(db_column='TDPoisonPillDeadHand', blank=True) # Field name made lowercase.
    gcommitteetype = models.TextField(db_column='gCommitteeType', blank=True) # Field name made lowercase.
    companyage = models.TextField(db_column='CompanyAge', blank=True) # Field name made lowercase.
    compfounded = models.TextField(db_column='CompFounded', blank=True) # Field name made lowercase.
    mailpostcode = models.TextField(db_column='MailPostCode', blank=True) # Field name made lowercase.
    indexfortune = models.TextField(db_column='IndexFortune', blank=True) # Field name made lowercase.
    sic = models.TextField(db_column='SIC', blank=True) # Field name made lowercase.
    insiderspctg = models.TextField(db_column='InsidersPctg', blank=True) # Field name made lowercase.
    insiderspluspctg = models.TextField(db_column='InsidersPlusPctg', blank=True) # Field name made lowercase.
    annualmtg = models.TextField(db_column='AnnualMtg', blank=True) # Field name made lowercase.
    fiscalyrend = models.TextField(db_column='FiscalYrEnd', blank=True) # Field name made lowercase.
    annualmtgnext = models.TextField(db_column='AnnualMtgNext', blank=True) # Field name made lowercase.
    proxydate = models.TextField(db_column='ProxyDate', blank=True) # Field name made lowercase.
    marketcap = models.TextField(db_column='MarketCap', blank=True) # Field name made lowercase.
    ownersfivepercentpctg = models.TextField(db_column='OwnersFivePercentPctg', blank=True) # Field name made lowercase.
    auditfees = models.TextField(db_column='AuditFees', blank=True) # Field name made lowercase.
    auditfeesother = models.TextField(db_column='AuditFeesOther', blank=True) # Field name made lowercase.
    auditfeesprcntg = models.TextField(db_column='AuditFeesPrcntg', blank=True) # Field name made lowercase.
    auditfeesrelated = models.TextField(db_column='AuditFeesRelated', blank=True) # Field name made lowercase.
    auditfeestax = models.TextField(db_column='AuditFeesTax', blank=True) # Field name made lowercase.
    auditfeestotal = models.TextField(db_column='AuditFeesTotal', blank=True) # Field name made lowercase.
    auditnonauditfeespctg = models.TextField(db_column='AuditNonAuditFeesPctg', blank=True) # Field name made lowercase.
    auditorsince = models.TextField(db_column='AuditorSince', blank=True) # Field name made lowercase.
    bdmtgs = models.TextField(db_column='BDMtgs', blank=True) # Field name made lowercase.
    bdmtgsoutside = models.TextField(db_column='BdMtgsOutside', blank=True) # Field name made lowercase.
    cfoage = models.TextField(db_column='CFOAge', blank=True) # Field name made lowercase.
    cfotenure = models.TextField(db_column='CFOTenure', blank=True) # Field name made lowercase.
    directorsactiveceos = models.TextField(db_column='DirectorsActiveCEOs', blank=True) # Field name made lowercase.
    directorsactiveceopct = models.TextField(db_column='DirectorsActiveCEOPct', blank=True) # Field name made lowercase.
    directorsfailed = models.TextField(db_column='DirectorsFailed', blank=True) # Field name made lowercase.
    directorsfailedpct = models.TextField(db_column='DirectorsFailedPct', blank=True) # Field name made lowercase.
    directorsinside = models.TextField(db_column='DirectorsInside', blank=True) # Field name made lowercase.
    directorsinsidepct = models.TextField(db_column='DirectorsInsidePct', blank=True) # Field name made lowercase.
    directorsoutside = models.TextField(db_column='DirectorsOutside', blank=True) # Field name made lowercase.
    directorsoutsiderelated = models.TextField(db_column='DirectorsOutsideRelated', blank=True) # Field name made lowercase.
    directorsoutsiderelatedpct = models.TextField(db_column='DirectorsOutsideRelatedPct', blank=True) # Field name made lowercase.
    directorsoutsidetotal = models.TextField(db_column='DirectorsOutsideTotal', blank=True) # Field name made lowercase.
    directorsover10yrstenure = models.TextField(db_column='DirectorsOver10YrsTenure', blank=True) # Field name made lowercase.
    directorsover10yrstenurepct = models.TextField(db_column='DirectorsOver10YrsTenurePct', blank=True) # Field name made lowercase.
    directorsover15yrstenure = models.TextField(db_column='DirectorsOver15YrsTenure', blank=True) # Field name made lowercase.
    directorsover15yrstenurepct = models.TextField(db_column='DirectorsOver15YrsTenurePct', blank=True) # Field name made lowercase.
    directorsover3boards = models.TextField(db_column='DirectorsOver3Boards', blank=True) # Field name made lowercase.
    directorsover4boards = models.TextField(db_column='DirectorsOver4Boards', blank=True) # Field name made lowercase.
    directorsover4publicboards = models.TextField(db_column='DirectorsOver4PublicBoards', blank=True) # Field name made lowercase.
    directorsover4publicboardspct = models.TextField(db_column='DirectorsOver4PublicBoardsPct', blank=True) # Field name made lowercase.
    directorsover70 = models.TextField(db_column='DirectorsOver70', blank=True) # Field name made lowercase.
    directorsover70pct = models.TextField(db_column='DirectorsOver70Pct', blank=True) # Field name made lowercase.
    directorsproblem = models.TextField(db_column='DirectorsProblem', blank=True) # Field name made lowercase.
    directorsproblempct = models.TextField(db_column='DirectorsProblemPct', blank=True) # Field name made lowercase.
    directorswomen = models.TextField(db_column='DirectorsWomen', blank=True) # Field name made lowercase.
    directorswomenpct = models.TextField(db_column='DirectorsWomenPct', blank=True) # Field name made lowercase.
    directorszeroshares = models.TextField(db_column='DirectorsZeroShares', blank=True) # Field name made lowercase.
    directorszerosharesandtenureover = models.TextField(db_column='DirectorsZeroSharesandTenureOver', blank=True) # Field name made lowercase.
    directorszerosharesandtenureove0 = models.TextField(db_column='DirectorsZeroSharesandTenureOve0', blank=True) # Field name made lowercase.
    directorstotal = models.TextField(db_column='DirectorsTotal', blank=True) # Field name made lowercase.
    dividendyield = models.TextField(db_column='DividendYield', blank=True) # Field name made lowercase.
    dividendyld = models.TextField(db_column='DividendYld', blank=True) # Field name made lowercase.
    optionsaccelerateddate = models.TextField(db_column='OptionsAcceleratedDate', blank=True) # Field name made lowercase.
    sharesdilution = models.TextField(db_column='SharesDilution', blank=True) # Field name made lowercase.
    dirbasepay = models.TextField(db_column='DirBasePay', blank=True) # Field name made lowercase.
    dirbdmtgfees = models.TextField(db_column='DirBdMtgFees', blank=True) # Field name made lowercase.
    dirleaddirectorfees = models.TextField(db_column='DirLeadDirectorFees', blank=True) # Field name made lowercase.
    dirstockaward = models.TextField(db_column='DirStockAward', blank=True) # Field name made lowercase.
    dirstockawardinitial = models.TextField(db_column='DirStockAwardInitial', blank=True) # Field name made lowercase.
    dirstockoptionbsvalue = models.TextField(db_column='DirStockOptionBSValue', blank=True) # Field name made lowercase.
    dirstockoptionbsvalueinitial = models.TextField(db_column='DirStockOptionBSValueInitial', blank=True) # Field name made lowercase.
    dirstockoptionexprice = models.TextField(db_column='DirStockOptionExPrice', blank=True) # Field name made lowercase.
    dirstockoptionexpriceinitial = models.TextField(db_column='DirStockOptionExPriceInitial', blank=True) # Field name made lowercase.
    dirstockoptionnumber = models.TextField(db_column='DirStockOptionNumber', blank=True) # Field name made lowercase.
    dirstockoptionnumberinitial = models.TextField(db_column='DirStockOptionNumberInitial', blank=True) # Field name made lowercase.
    dirstockoptionvalue = models.TextField(db_column='DirStockOptionValue', blank=True) # Field name made lowercase.
    dirstockoptionvalueinitial = models.TextField(db_column='DirStockOptionValueInitial', blank=True) # Field name made lowercase.
    dirstockunitaward = models.TextField(db_column='DirStockUnitAward', blank=True) # Field name made lowercase.
    dirstockunitawardinitial = models.TextField(db_column='DirStockUnitAwardInitial', blank=True) # Field name made lowercase.
    dc_avgdircomp = models.TextField(db_column='dc_AvgDirComp', blank=True) # Field name made lowercase.
    year = models.TextField(db_column='YEAR', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'wrds_companies_2008'

class WrdsCompanies2009(models.Model):
    ticker = models.TextField(db_column='Ticker', blank=True) # Field name made lowercase.
    companyname = models.TextField(db_column='CompanyName', blank=True) # Field name made lowercase.
    cik = models.TextField(db_column='CIK', blank=True) # Field name made lowercase.
    cusip = models.TextField(db_column='CUSIP', blank=True) # Field name made lowercase.
    companyfedid = models.TextField(db_column='CompanyFedID', blank=True) # Field name made lowercase.
    companyage = models.TextField(db_column='CompanyAge', blank=True) # Field name made lowercase.
    compfounded = models.TextField(db_column='CompFounded', blank=True) # Field name made lowercase.
    country = models.TextField(db_column='Country', blank=True) # Field name made lowercase.
    statehq = models.TextField(db_column='StateHQ', blank=True) # Field name made lowercase.
    stateinc = models.TextField(db_column='StateInc', blank=True) # Field name made lowercase.
    exchange = models.TextField(db_column='Exchange', blank=True) # Field name made lowercase.
    mailaddress = models.TextField(db_column='MailAddress', blank=True) # Field name made lowercase.
    mailingaddress1a = models.TextField(db_column='MailingAddress1a', blank=True) # Field name made lowercase.
    mailingaddress2 = models.TextField(db_column='MailingAddress2', blank=True) # Field name made lowercase.
    mailcity = models.TextField(db_column='MailCity', blank=True) # Field name made lowercase.
    mailstate = models.TextField(db_column='MailState', blank=True) # Field name made lowercase.
    mailpostcode = models.TextField(db_column='MailPostCode', blank=True) # Field name made lowercase.
    mailcountry = models.TextField(db_column='MailCountry', blank=True) # Field name made lowercase.
    mailfax = models.TextField(db_column='MailFax', blank=True) # Field name made lowercase.
    mailphone = models.TextField(db_column='MailPhone', blank=True) # Field name made lowercase.
    indexedstock = models.TextField(db_column='IndexedStock', blank=True) # Field name made lowercase.
    indexfortune = models.TextField(db_column='IndexFortune', blank=True) # Field name made lowercase.
    indexrussell = models.TextField(db_column='IndexRussell', blank=True) # Field name made lowercase.
    indexsp = models.TextField(db_column='IndexSP', blank=True) # Field name made lowercase.
    industry = models.TextField(db_column='Industry', blank=True) # Field name made lowercase.
    sic = models.TextField(db_column='SIC', blank=True) # Field name made lowercase.
    sicdescription = models.TextField(db_column='SICDescription', blank=True) # Field name made lowercase.
    insiderscontrol = models.TextField(db_column='InsidersControl', blank=True) # Field name made lowercase.
    insiderspctg = models.TextField(db_column='InsidersPctg', blank=True) # Field name made lowercase.
    insiderspluspctg = models.TextField(db_column='InsidersPlusPctg', blank=True) # Field name made lowercase.
    institutionalmajority = models.TextField(db_column='InstitutionalMajority', blank=True) # Field name made lowercase.
    annualmtg = models.TextField(db_column='AnnualMtg', blank=True) # Field name made lowercase.
    fiscalyrend = models.TextField(db_column='FiscalYrEnd', blank=True) # Field name made lowercase.
    annualmtgplace = models.TextField(db_column='AnnualMtgPlace', blank=True) # Field name made lowercase.
    annualmtgnext = models.TextField(db_column='AnnualMtgNext', blank=True) # Field name made lowercase.
    proxydate = models.TextField(db_column='ProxyDate', blank=True) # Field name made lowercase.
    marketcap = models.TextField(db_column='MarketCap', blank=True) # Field name made lowercase.
    ownersfivepercentpctg = models.TextField(db_column='OwnersFivePercentPctg', blank=True) # Field name made lowercase.
    ownershipcategory = models.TextField(db_column='OwnershipCategory', blank=True) # Field name made lowercase.
    auditfees = models.TextField(db_column='AuditFees', blank=True) # Field name made lowercase.
    auditfeesother = models.TextField(db_column='AuditFeesOther', blank=True) # Field name made lowercase.
    auditfeesprcntg = models.TextField(db_column='AuditFeesPrcntg', blank=True) # Field name made lowercase.
    auditfeesrelated = models.TextField(db_column='AuditFeesRelated', blank=True) # Field name made lowercase.
    auditfeestax = models.TextField(db_column='AuditFeesTax', blank=True) # Field name made lowercase.
    auditfeestotal = models.TextField(db_column='AuditFeesTotal', blank=True) # Field name made lowercase.
    auditnonauditfeespctg = models.TextField(db_column='AuditNonAuditFeesPctg', blank=True) # Field name made lowercase.
    auditor = models.TextField(db_column='Auditor', blank=True) # Field name made lowercase.
    auditorchangenotes = models.TextField(db_column='AuditorChangeNotes', blank=True) # Field name made lowercase.
    auditorindependent = models.TextField(db_column='AuditorIndependent', blank=True) # Field name made lowercase.
    auditornominee = models.TextField(db_column='AuditorNominee', blank=True) # Field name made lowercase.
    auditorprevious = models.TextField(db_column='AuditorPrevious', blank=True) # Field name made lowercase.
    auditorsince = models.TextField(db_column='AuditorSince', blank=True) # Field name made lowercase.
    bdmtgs = models.TextField(db_column='BDMtgs', blank=True) # Field name made lowercase.
    bdmtgsoutside = models.TextField(db_column='BdMtgsOutside', blank=True) # Field name made lowercase.
    bdoutsidemaj = models.TextField(db_column='BdOutsideMaj', blank=True) # Field name made lowercase.
    bdoutsidemajstrict = models.TextField(db_column='BdOutsideMajStrict', blank=True) # Field name made lowercase.
    bdoutsidemeets = models.TextField(db_column='BDOutsideMeets', blank=True) # Field name made lowercase.
    bdoutsidemtgsource = models.TextField(db_column='BdOutsideMtgSource', blank=True) # Field name made lowercase.
    busethicscode = models.TextField(db_column='BusEthicsCode', blank=True) # Field name made lowercase.
    cfofname = models.TextField(db_column='CFOFName', blank=True) # Field name made lowercase.
    cfolname = models.TextField(db_column='CFOLName', blank=True) # Field name made lowercase.
    cfoage = models.TextField(db_column='CFOAge', blank=True) # Field name made lowercase.
    cfotenure = models.TextField(db_column='CFOTenure', blank=True) # Field name made lowercase.
    cfoprofile = models.TextField(db_column='CFOProfile', blank=True) # Field name made lowercase.
    chairmanfname = models.TextField(db_column='ChairmanFName', blank=True) # Field name made lowercase.
    chairmanlname = models.TextField(db_column='ChairmanLName', blank=True) # Field name made lowercase.
    chairmanis = models.TextField(db_column='ChairmanIs', blank=True) # Field name made lowercase.
    cochairmanfname = models.TextField(db_column='CoChairmanFName', blank=True) # Field name made lowercase.
    cochairmanlname = models.TextField(db_column='CoChairmanLName', blank=True) # Field name made lowercase.
    chiefgovofficerfname = models.TextField(db_column='ChiefGovOfficerFName', blank=True) # Field name made lowercase.
    chiefgovofficerlname = models.TextField(db_column='ChiefGovOfficerLName', blank=True) # Field name made lowercase.
    corpsecretaryfname = models.TextField(db_column='CorpSecretaryFName', blank=True) # Field name made lowercase.
    corpsecretarylname = models.TextField(db_column='CorpSecretaryLName', blank=True) # Field name made lowercase.
    gencounselfname = models.TextField(db_column='GenCounselFName', blank=True) # Field name made lowercase.
    gencounsellname = models.TextField(db_column='GenCounselLName', blank=True) # Field name made lowercase.
    leaddirectorfname = models.TextField(db_column='LeadDirectorFName', blank=True) # Field name made lowercase.
    leaddirectorlname = models.TextField(db_column='LeadDirectorLName', blank=True) # Field name made lowercase.
    leadlawfirm = models.TextField(db_column='LeadLawFirm', blank=True) # Field name made lowercase.
    commauditindependent = models.TextField(db_column='CommAuditIndependent', blank=True) # Field name made lowercase.
    commauditfullyindependent = models.TextField(db_column='CommAuditFullyIndependent', blank=True) # Field name made lowercase.
    commcompindependent = models.TextField(db_column='CommCompIndependent', blank=True) # Field name made lowercase.
    commcompfullyindependent = models.TextField(db_column='CommCompFullyIndependent', blank=True) # Field name made lowercase.
    commnomgovindependent = models.TextField(db_column='CommNomGovIndependent', blank=True) # Field name made lowercase.
    commnomgovfullyindependent = models.TextField(db_column='CommNomGovFullyIndependent', blank=True) # Field name made lowercase.
    govpolicy = models.TextField(db_column='GovPolicy', blank=True) # Field name made lowercase.
    notesdircomp = models.TextField(db_column='NotesDirComp', blank=True) # Field name made lowercase.
    directorsactiveceos = models.TextField(db_column='DirectorsActiveCEOs', blank=True) # Field name made lowercase.
    directorsactiveceopct = models.TextField(db_column='DirectorsActiveCEOPct', blank=True) # Field name made lowercase.
    directorsfailed = models.TextField(db_column='DirectorsFailed', blank=True) # Field name made lowercase.
    directorsfailedpct = models.TextField(db_column='DirectorsFailedPct', blank=True) # Field name made lowercase.
    directorsinside = models.TextField(db_column='DirectorsInside', blank=True) # Field name made lowercase.
    directorsinsidepct = models.TextField(db_column='DirectorsInsidePct', blank=True) # Field name made lowercase.
    directorsoutside = models.TextField(db_column='DirectorsOutside', blank=True) # Field name made lowercase.
    directorsoutsiderelated = models.TextField(db_column='DirectorsOutsideRelated', blank=True) # Field name made lowercase.
    directorsoutsiderelatedpct = models.TextField(db_column='DirectorsOutsideRelatedPct', blank=True) # Field name made lowercase.
    directorsoutsidetotal = models.TextField(db_column='DirectorsOutsideTotal', blank=True) # Field name made lowercase.
    directorsover10yrstenure = models.TextField(db_column='DirectorsOver10YrsTenure', blank=True) # Field name made lowercase.
    directorsover10yrstenurepct = models.TextField(db_column='DirectorsOver10YrsTenurePct', blank=True) # Field name made lowercase.
    directorsover15yrstenure = models.TextField(db_column='DirectorsOver15YrsTenure', blank=True) # Field name made lowercase.
    directorsover15yrstenurepct = models.TextField(db_column='DirectorsOver15YrsTenurePct', blank=True) # Field name made lowercase.
    directorsover4boards = models.TextField(db_column='DirectorsOver4Boards', blank=True) # Field name made lowercase.
    directorsover4publicboards = models.TextField(db_column='DirectorsOver4PublicBoards', blank=True) # Field name made lowercase.
    directorsover4publicboardspct = models.TextField(db_column='DirectorsOver4PublicBoardsPct', blank=True) # Field name made lowercase.
    directorsover70 = models.TextField(db_column='DirectorsOver70', blank=True) # Field name made lowercase.
    directorsover70pct = models.TextField(db_column='DirectorsOver70Pct', blank=True) # Field name made lowercase.
    directorsproblem = models.TextField(db_column='DirectorsProblem', blank=True) # Field name made lowercase.
    directorsproblempct = models.TextField(db_column='DirectorsProblemPct', blank=True) # Field name made lowercase.
    directorswomen = models.TextField(db_column='DirectorsWomen', blank=True) # Field name made lowercase.
    directorswomenpct = models.TextField(db_column='DirectorsWomenPct', blank=True) # Field name made lowercase.
    directorszeroshares = models.TextField(db_column='DirectorsZeroShares', blank=True) # Field name made lowercase.
    directorszerosharesandtenureover = models.TextField(db_column='DirectorsZeroSharesAndTenureOver', blank=True) # Field name made lowercase.
    directorszerosharesandtenureove1 = models.TextField(db_column='DirectorsZeroSharesAndTenureOve1', blank=True) # Field name made lowercase.
    directorstotal = models.TextField(db_column='DirectorsTotal', blank=True) # Field name made lowercase.
    compdescription = models.TextField(db_column='CompDescription', blank=True) # Field name made lowercase.
    companyprofileshort = models.TextField(db_column='CompanyProfileShort', blank=True) # Field name made lowercase.
    companyprofiletodcalc = models.TextField(db_column='CompanyProfileTODCalc', blank=True) # Field name made lowercase.
    controlledcompanyexemption = models.TextField(db_column='ControlledCompanyExemption', blank=True) # Field name made lowercase.
    dividendyield = models.TextField(db_column='DividendYield', blank=True) # Field name made lowercase.
    voteauditorno = models.TextField(db_column='VoteAuditorNo', blank=True) # Field name made lowercase.
    optionsaccelerated = models.TextField(db_column='OptionsAccelerated', blank=True) # Field name made lowercase.
    optionsaccelerateddate = models.TextField(db_column='OptionsAcceleratedDate', blank=True) # Field name made lowercase.
    optionsbackdating = models.TextField(db_column='OptionsBackdating', blank=True) # Field name made lowercase.
    tddirelectionmajvote = models.TextField(db_column='TDDirElectionMajVote', blank=True) # Field name made lowercase.
    tddirelectionmajvotenotes = models.TextField(db_column='TDDirElectionMajVoteNotes', blank=True) # Field name made lowercase.
    tddocumentnotations = models.TextField(db_column='TDDocumentNotations', blank=True) # Field name made lowercase.
    tdpoisonpilldeadhand = models.TextField(db_column='TDPoisonPillDeadHand', blank=True) # Field name made lowercase.
    year = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'wrds_companies_2009'

class WrdsCompanies2010(models.Model):
    ticker = models.TextField(blank=True)
    companyname = models.TextField(db_column='companyName', blank=True) # Field name made lowercase.
    cik = models.TextField(blank=True)
    cusip = models.TextField(db_column='CUSIP', blank=True) # Field name made lowercase.
    companyfedid = models.TextField(db_column='CompanyFedID', blank=True) # Field name made lowercase.
    companyage = models.TextField(db_column='CompanyAge', blank=True) # Field name made lowercase.
    compfounded = models.TextField(db_column='CompFounded', blank=True) # Field name made lowercase.
    country = models.TextField(db_column='Country', blank=True) # Field name made lowercase.
    statehq = models.TextField(db_column='StateHQ', blank=True) # Field name made lowercase.
    stateinc = models.TextField(db_column='StateInc', blank=True) # Field name made lowercase.
    exchange = models.TextField(db_column='Exchange', blank=True) # Field name made lowercase.
    mailaddress = models.TextField(db_column='MailAddress', blank=True) # Field name made lowercase.
    mailingaddress1a = models.TextField(db_column='MailingAddress1a', blank=True) # Field name made lowercase.
    mailingaddress2 = models.TextField(db_column='MailingAddress2', blank=True) # Field name made lowercase.
    mailcity = models.TextField(db_column='MailCity', blank=True) # Field name made lowercase.
    mailstate = models.TextField(db_column='MailState', blank=True) # Field name made lowercase.
    mailpostcode = models.TextField(db_column='MailPostCode', blank=True) # Field name made lowercase.
    mailcountry = models.TextField(db_column='MailCountry', blank=True) # Field name made lowercase.
    mailfax = models.TextField(db_column='MailFax', blank=True) # Field name made lowercase.
    mailphone = models.TextField(db_column='MailPhone', blank=True) # Field name made lowercase.
    indexedstock = models.TextField(db_column='IndexedStock', blank=True) # Field name made lowercase.
    indexfortune = models.TextField(db_column='IndexFortune', blank=True) # Field name made lowercase.
    indexrussell = models.TextField(db_column='IndexRussell', blank=True) # Field name made lowercase.
    indexsp = models.TextField(db_column='IndexSP', blank=True) # Field name made lowercase.
    industry = models.TextField(db_column='Industry', blank=True) # Field name made lowercase.
    sic = models.TextField(db_column='SIC', blank=True) # Field name made lowercase.
    sicdescription = models.TextField(db_column='SICDescription', blank=True) # Field name made lowercase.
    insiderscontrol = models.TextField(db_column='InsidersControl', blank=True) # Field name made lowercase.
    insiderspctg = models.TextField(db_column='InsidersPctg', blank=True) # Field name made lowercase.
    insiderspluspctg = models.TextField(db_column='InsidersPlusPctg', blank=True) # Field name made lowercase.
    institutionalmajority = models.TextField(db_column='InstitutionalMajority', blank=True) # Field name made lowercase.
    annualmtg = models.TextField(db_column='AnnualMtg', blank=True) # Field name made lowercase.
    fiscalyrend = models.TextField(db_column='FiscalYrEnd', blank=True) # Field name made lowercase.
    annualmtgplace = models.TextField(db_column='AnnualMtgPlace', blank=True) # Field name made lowercase.
    annualmtgnext = models.TextField(db_column='AnnualMtgNext', blank=True) # Field name made lowercase.
    proxydate = models.TextField(db_column='ProxyDate', blank=True) # Field name made lowercase.
    marketcap = models.TextField(db_column='MarketCap', blank=True) # Field name made lowercase.
    ownersfivepercentpctg = models.TextField(db_column='OwnersFivePercentPctg', blank=True) # Field name made lowercase.
    ownershipcategory = models.TextField(db_column='OwnershipCategory', blank=True) # Field name made lowercase.
    auditfees = models.TextField(db_column='AuditFees', blank=True) # Field name made lowercase.
    auditfeesother = models.TextField(db_column='AuditFeesOther', blank=True) # Field name made lowercase.
    auditfeesprcntg = models.TextField(db_column='AuditFeesPrcntg', blank=True) # Field name made lowercase.
    auditfeesrelated = models.TextField(db_column='AuditFeesRelated', blank=True) # Field name made lowercase.
    auditfeestax = models.TextField(db_column='AuditFeesTax', blank=True) # Field name made lowercase.
    auditfeestotal = models.TextField(db_column='AuditFeesTotal', blank=True) # Field name made lowercase.
    auditnonauditfeespctg = models.TextField(db_column='AuditNonAuditFeesPctg', blank=True) # Field name made lowercase.
    auditor = models.TextField(db_column='Auditor', blank=True) # Field name made lowercase.
    auditorchangenotes = models.TextField(db_column='AuditorChangeNotes', blank=True) # Field name made lowercase.
    auditorindependent = models.TextField(db_column='AuditorIndependent', blank=True) # Field name made lowercase.
    auditornominee = models.TextField(db_column='AuditorNominee', blank=True) # Field name made lowercase.
    auditorprevious = models.TextField(db_column='AuditorPrevious', blank=True) # Field name made lowercase.
    auditorsince = models.TextField(db_column='AuditorSince', blank=True) # Field name made lowercase.
    bdmtgs = models.TextField(db_column='BDMtgs', blank=True) # Field name made lowercase.
    bdmtgsoutside = models.TextField(db_column='BdMtgsOutside', blank=True) # Field name made lowercase.
    bdoutsidemaj = models.TextField(db_column='BdOutsideMaj', blank=True) # Field name made lowercase.
    bdoutsidemajstrict = models.TextField(db_column='BdOutsideMajStrict', blank=True) # Field name made lowercase.
    bdoutsidemeets = models.TextField(db_column='BDOutsideMeets', blank=True) # Field name made lowercase.
    bdoutsidemtgsource = models.TextField(db_column='BdOutsideMtgSource', blank=True) # Field name made lowercase.
    busethicscode = models.TextField(db_column='BusEthicsCode', blank=True) # Field name made lowercase.
    chairmanis = models.TextField(db_column='ChairmanIs', blank=True) # Field name made lowercase.
    chiefgovofficerfname = models.TextField(db_column='ChiefGovOfficerFName', blank=True) # Field name made lowercase.
    chiefgovofficerlname = models.TextField(db_column='ChiefGovOfficerLName', blank=True) # Field name made lowercase.
    corpsecretaryfname = models.TextField(db_column='CorpSecretaryFName', blank=True) # Field name made lowercase.
    corpsecretarylname = models.TextField(db_column='CorpSecretaryLName', blank=True) # Field name made lowercase.
    gencounselfname = models.TextField(db_column='GenCounselFName', blank=True) # Field name made lowercase.
    gencounsellname = models.TextField(db_column='GenCounselLName', blank=True) # Field name made lowercase.
    leaddirectorfname = models.TextField(db_column='LeadDirectorFName', blank=True) # Field name made lowercase.
    leaddirectorlname = models.TextField(db_column='LeadDirectorLName', blank=True) # Field name made lowercase.
    leadlawfirm = models.TextField(db_column='LeadLawFirm', blank=True) # Field name made lowercase.
    commauditindependent = models.TextField(db_column='CommAuditIndependent', blank=True) # Field name made lowercase.
    commauditfullyindependent = models.TextField(db_column='CommAuditFullyIndependent', blank=True) # Field name made lowercase.
    commcompindependent = models.TextField(db_column='CommCompIndependent', blank=True) # Field name made lowercase.
    commcompfullyindependent = models.TextField(db_column='CommCompFullyIndependent', blank=True) # Field name made lowercase.
    commnomgovindependent = models.TextField(db_column='CommNomGovIndependent', blank=True) # Field name made lowercase.
    commnomgovfullyindependent = models.TextField(db_column='CommNomGovFullyIndependent', blank=True) # Field name made lowercase.
    govpolicy = models.TextField(db_column='GovPolicy', blank=True) # Field name made lowercase.
    notesdircomp = models.TextField(db_column='NotesDirComp', blank=True) # Field name made lowercase.
    directorsactiveceos = models.TextField(db_column='DirectorsActiveCEOs', blank=True) # Field name made lowercase.
    directorsactiveceopct = models.TextField(db_column='DirectorsActiveCEOPct', blank=True) # Field name made lowercase.
    directorsfailed = models.TextField(db_column='DirectorsFailed', blank=True) # Field name made lowercase.
    directorsfailedpct = models.TextField(db_column='DirectorsFailedPct', blank=True) # Field name made lowercase.
    directorsinside = models.TextField(db_column='DirectorsInside', blank=True) # Field name made lowercase.
    directorsinsidepct = models.TextField(db_column='DirectorsInsidePct', blank=True) # Field name made lowercase.
    directorsoutside = models.TextField(db_column='DirectorsOutside', blank=True) # Field name made lowercase.
    directorsoutsiderelated = models.TextField(db_column='DirectorsOutsideRelated', blank=True) # Field name made lowercase.
    directorsoutsiderelatedpct = models.TextField(db_column='DirectorsOutsideRelatedPct', blank=True) # Field name made lowercase.
    directorsoutsidetotal = models.TextField(db_column='DirectorsOutsideTotal', blank=True) # Field name made lowercase.
    directorsover10yrstenure = models.TextField(db_column='DirectorsOver10YrsTenure', blank=True) # Field name made lowercase.
    directorsover10yrstenurepct = models.TextField(db_column='DirectorsOver10YrsTenurePct', blank=True) # Field name made lowercase.
    directorsover15yrstenure = models.TextField(db_column='DirectorsOver15YrsTenure', blank=True) # Field name made lowercase.
    directorsover15yrstenurepct = models.TextField(db_column='DirectorsOver15YrsTenurePct', blank=True) # Field name made lowercase.
    directorsover4boards = models.TextField(db_column='DirectorsOver4Boards', blank=True) # Field name made lowercase.
    directorsover4publicboards = models.TextField(db_column='DirectorsOver4PublicBoards', blank=True) # Field name made lowercase.
    directorsover4publicboardspct = models.TextField(db_column='DirectorsOver4PublicBoardsPct', blank=True) # Field name made lowercase.
    directorsover70 = models.TextField(db_column='DirectorsOver70', blank=True) # Field name made lowercase.
    directorsover70pct = models.TextField(db_column='DirectorsOver70Pct', blank=True) # Field name made lowercase.
    directorsproblem = models.TextField(db_column='DirectorsProblem', blank=True) # Field name made lowercase.
    directorsproblempct = models.TextField(db_column='DirectorsProblemPct', blank=True) # Field name made lowercase.
    directorswomen = models.TextField(db_column='DirectorsWomen', blank=True) # Field name made lowercase.
    directorswomenpct = models.TextField(db_column='DirectorsWomenPct', blank=True) # Field name made lowercase.
    directorszeroshares = models.TextField(db_column='DirectorsZeroShares', blank=True) # Field name made lowercase.
    directorszerosharesandtenureover = models.TextField(db_column='DirectorsZeroSharesandTenureOver', blank=True) # Field name made lowercase.
    directorszerosharesandtenureove1 = models.TextField(db_column='DirectorsZeroSharesandTenureOve1', blank=True) # Field name made lowercase.
    directorstotal = models.TextField(db_column='DirectorsTotal', blank=True) # Field name made lowercase.
    compdescription = models.TextField(db_column='CompDescription', blank=True) # Field name made lowercase.
    companyprofileshort = models.TextField(db_column='CompanyProfileShort', blank=True) # Field name made lowercase.
    controlledcompanyexemption = models.TextField(db_column='ControlledCompanyExemption', blank=True) # Field name made lowercase.
    dividendyield = models.TextField(db_column='DividendYield', blank=True) # Field name made lowercase.
    voteauditorno = models.TextField(db_column='VoteAuditorNo', blank=True) # Field name made lowercase.
    optionsaccelerated = models.TextField(db_column='OptionsAccelerated', blank=True) # Field name made lowercase.
    optionsaccelerateddate = models.TextField(db_column='OptionsAcceleratedDate', blank=True) # Field name made lowercase.
    optionsbackdating = models.TextField(db_column='OptionsBackdating', blank=True) # Field name made lowercase.
    year = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'wrds_companies_2010'

class WrdsCompanies2011(models.Model):
    ticker = models.TextField(db_column='Ticker', blank=True) # Field name made lowercase.
    companyname = models.TextField(db_column='CompanyName', blank=True) # Field name made lowercase.
    cik = models.TextField(db_column='CIK', blank=True) # Field name made lowercase.
    cusip = models.TextField(db_column='CUSIP', blank=True) # Field name made lowercase.
    companyfedid = models.TextField(db_column='CompanyFedID', blank=True) # Field name made lowercase.
    companyage = models.TextField(db_column='CompanyAge', blank=True) # Field name made lowercase.
    compfounded = models.TextField(db_column='CompFounded', blank=True) # Field name made lowercase.
    country = models.TextField(db_column='Country', blank=True) # Field name made lowercase.
    statehq = models.TextField(db_column='StateHQ', blank=True) # Field name made lowercase.
    stateinc = models.TextField(db_column='StateInc', blank=True) # Field name made lowercase.
    exchange = models.TextField(db_column='Exchange', blank=True) # Field name made lowercase.
    address1 = models.TextField(db_column='Address1', blank=True) # Field name made lowercase.
    address2 = models.TextField(db_column='Address2', blank=True) # Field name made lowercase.
    address3 = models.TextField(db_column='Address3', blank=True) # Field name made lowercase.
    city = models.TextField(db_column='City', blank=True) # Field name made lowercase.
    state = models.TextField(db_column='State', blank=True) # Field name made lowercase.
    mailcountry = models.TextField(db_column='MailCountry', blank=True) # Field name made lowercase.
    phone_fax = models.TextField(db_column='Phone_Fax', blank=True) # Field name made lowercase.
    phone = models.TextField(db_column='Phone', blank=True) # Field name made lowercase.
    indexfortune = models.TextField(db_column='IndexFortune', blank=True) # Field name made lowercase.
    indexrussell = models.TextField(db_column='IndexRussell', blank=True) # Field name made lowercase.
    indexsp = models.TextField(db_column='IndexSP', blank=True) # Field name made lowercase.
    industry = models.TextField(db_column='Industry', blank=True) # Field name made lowercase.
    sic = models.TextField(db_column='SIC', blank=True) # Field name made lowercase.
    sicdescription = models.TextField(db_column='SICDescription', blank=True) # Field name made lowercase.
    insiderscontrol = models.TextField(db_column='InsidersControl', blank=True) # Field name made lowercase.
    insiderspctg = models.TextField(db_column='InsidersPctg', blank=True) # Field name made lowercase.
    insiderspluspctg = models.TextField(db_column='InsidersPlusPctg', blank=True) # Field name made lowercase.
    institutionalmajority = models.TextField(db_column='InstitutionalMajority', blank=True) # Field name made lowercase.
    annualmtg = models.TextField(db_column='AnnualMtg', blank=True) # Field name made lowercase.
    fiscalyrend = models.TextField(db_column='FiscalYrEnd', blank=True) # Field name made lowercase.
    annualmtgplace = models.TextField(db_column='AnnualMtgPlace', blank=True) # Field name made lowercase.
    annualmtgnext = models.TextField(db_column='AnnualMtgNext', blank=True) # Field name made lowercase.
    proxydate = models.TextField(db_column='ProxyDate', blank=True) # Field name made lowercase.
    ownersfivepercentpctg = models.TextField(db_column='OwnersFivePercentPctg', blank=True) # Field name made lowercase.
    ownershipcategory = models.TextField(db_column='OwnershipCategory', blank=True) # Field name made lowercase.
    auditfees = models.TextField(db_column='AuditFees', blank=True) # Field name made lowercase.
    auditfeesother = models.TextField(db_column='AuditFeesOther', blank=True) # Field name made lowercase.
    auditfeesprcntg = models.TextField(db_column='AuditFeesPrcntg', blank=True) # Field name made lowercase.
    auditfeesrelated = models.TextField(db_column='AuditFeesRelated', blank=True) # Field name made lowercase.
    auditfeestax = models.TextField(db_column='AuditFeesTax', blank=True) # Field name made lowercase.
    auditfeestotal = models.TextField(db_column='AuditFeesTotal', blank=True) # Field name made lowercase.
    auditnonauditfeespctg = models.TextField(db_column='AuditNonAuditFeesPctg', blank=True) # Field name made lowercase.
    auditor = models.TextField(db_column='Auditor', blank=True) # Field name made lowercase.
    auditorchangenotes = models.TextField(db_column='AuditorChangeNotes', blank=True) # Field name made lowercase.
    auditorindependent = models.TextField(db_column='AuditorIndependent', blank=True) # Field name made lowercase.
    auditornominee = models.TextField(db_column='AuditorNominee', blank=True) # Field name made lowercase.
    auditorprevious = models.TextField(db_column='AuditorPrevious', blank=True) # Field name made lowercase.
    auditorsince = models.TextField(db_column='AuditorSince', blank=True) # Field name made lowercase.
    bdmtgs = models.TextField(db_column='BDMtgs', blank=True) # Field name made lowercase.
    bdmtgsoutside = models.TextField(db_column='BdMtgsOutside', blank=True) # Field name made lowercase.
    bdoutsidemaj = models.TextField(db_column='BdOutsideMaj', blank=True) # Field name made lowercase.
    bdoutsidemajstrict = models.TextField(db_column='BdOutsideMajStrict', blank=True) # Field name made lowercase.
    bdoutsidemeets = models.TextField(db_column='BDOutsideMeets', blank=True) # Field name made lowercase.
    bdoutsidemtgsource = models.TextField(db_column='BdOutsideMtgSource', blank=True) # Field name made lowercase.
    busethicscode = models.TextField(db_column='BusEthicsCode', blank=True) # Field name made lowercase.
    chairmanis = models.TextField(db_column='ChairmanIs', blank=True) # Field name made lowercase.
    chiefgovofficerfname = models.TextField(db_column='ChiefGovOfficerFName', blank=True) # Field name made lowercase.
    chiefgovofficerlname = models.TextField(db_column='ChiefGovOfficerLName', blank=True) # Field name made lowercase.
    corpsecretaryfname = models.TextField(db_column='CorpSecretaryFName', blank=True) # Field name made lowercase.
    corpsecretarylname = models.TextField(db_column='CorpSecretaryLName', blank=True) # Field name made lowercase.
    gencounselfname = models.TextField(db_column='GenCounselFName', blank=True) # Field name made lowercase.
    gencounsellname = models.TextField(db_column='GenCounselLName', blank=True) # Field name made lowercase.
    leaddirectorfname = models.TextField(db_column='LeadDirectorFName', blank=True) # Field name made lowercase.
    leaddirectorlname = models.TextField(db_column='LeadDirectorLName', blank=True) # Field name made lowercase.
    leadlawfirm = models.TextField(db_column='LeadLawFirm', blank=True) # Field name made lowercase.
    commauditindependent = models.TextField(db_column='CommAuditIndependent', blank=True) # Field name made lowercase.
    commauditfullyindependent = models.TextField(db_column='CommAuditFullyIndependent', blank=True) # Field name made lowercase.
    commcompindependent = models.TextField(db_column='CommCompIndependent', blank=True) # Field name made lowercase.
    commcompfullyindependent = models.TextField(db_column='CommCompFullyIndependent', blank=True) # Field name made lowercase.
    committeenomgovindependent = models.TextField(db_column='CommitteeNomGovIndependent', blank=True) # Field name made lowercase.
    committeenomgovfullyindependent = models.TextField(db_column='CommitteeNomGovFullyIndependent', blank=True) # Field name made lowercase.
    govpolicy = models.TextField(db_column='GovPolicy', blank=True) # Field name made lowercase.
    notesdircomp = models.TextField(db_column='NotesDirComp', blank=True) # Field name made lowercase.
    directorsactiveceos = models.TextField(db_column='DirectorsActiveCEOs', blank=True) # Field name made lowercase.
    directorsactiveceopct = models.TextField(db_column='DirectorsActiveCEOPct', blank=True) # Field name made lowercase.
    directorsfailed = models.TextField(db_column='DirectorsFailed', blank=True) # Field name made lowercase.
    directorsfailedpct = models.TextField(db_column='DirectorsFailedPct', blank=True) # Field name made lowercase.
    directorsinside = models.TextField(db_column='DirectorsInside', blank=True) # Field name made lowercase.
    directorsinsidepct = models.TextField(db_column='DirectorsInsidePct', blank=True) # Field name made lowercase.
    directorsoutside = models.TextField(db_column='DirectorsOutside', blank=True) # Field name made lowercase.
    directorsoutsiderelated = models.TextField(db_column='DirectorsOutsideRelated', blank=True) # Field name made lowercase.
    directorsoutsiderelatedpct = models.TextField(db_column='DirectorsOutsideRelatedPct', blank=True) # Field name made lowercase.
    directorsoutsidetotal = models.TextField(db_column='DirectorsOutsideTotal', blank=True) # Field name made lowercase.
    directorsover10yrstenure = models.TextField(db_column='DirectorsOver10YrsTenure', blank=True) # Field name made lowercase.
    directorsover10yrstenurepct = models.TextField(db_column='DirectorsOver10YrsTenurePct', blank=True) # Field name made lowercase.
    directorsover15yrstenure = models.TextField(db_column='DirectorsOver15YrsTenure', blank=True) # Field name made lowercase.
    directorsover15yrstenurepct = models.TextField(db_column='DirectorsOver15YrsTenurePct', blank=True) # Field name made lowercase.
    directorsover4boards = models.TextField(db_column='DirectorsOver4Boards', blank=True) # Field name made lowercase.
    directorsover4publicboards = models.TextField(db_column='DirectorsOver4PublicBoards', blank=True) # Field name made lowercase.
    directorsover4publicboardspct = models.TextField(db_column='DirectorsOver4PublicBoardsPct', blank=True) # Field name made lowercase.
    directorsover70 = models.TextField(db_column='DirectorsOver70', blank=True) # Field name made lowercase.
    directorsover70pct = models.TextField(db_column='DirectorsOver70Pct', blank=True) # Field name made lowercase.
    directorsproblem = models.TextField(db_column='DirectorsProblem', blank=True) # Field name made lowercase.
    directorsproblempct = models.TextField(db_column='DirectorsProblemPct', blank=True) # Field name made lowercase.
    directorswomen = models.TextField(db_column='DirectorsWomen', blank=True) # Field name made lowercase.
    directorswomenpct = models.TextField(db_column='DirectorsWomenPct', blank=True) # Field name made lowercase.
    directorszeroshares = models.TextField(db_column='DirectorsZeroShares', blank=True) # Field name made lowercase.
    directorszerosharesandtenureover = models.TextField(db_column='DirectorsZeroSharesAndTenureOver', blank=True) # Field name made lowercase.
    directorszerosharesandtenureove1 = models.TextField(db_column='DirectorsZeroSharesAndTenureOve1', blank=True) # Field name made lowercase.
    directorstotal = models.TextField(db_column='DirectorsTotal', blank=True) # Field name made lowercase.
    compdescription = models.TextField(db_column='CompDescription', blank=True) # Field name made lowercase.
    companyprofileshort = models.TextField(db_column='CompanyProfileShort', blank=True) # Field name made lowercase.
    controlledcompanyexemption = models.TextField(db_column='ControlledCompanyExemption', blank=True) # Field name made lowercase.
    voteauditorno = models.TextField(db_column='VoteAuditorNo', blank=True) # Field name made lowercase.
    optionsaccelerated = models.TextField(db_column='OptionsAccelerated', blank=True) # Field name made lowercase.
    optionsaccelerateddate = models.TextField(db_column='OptionsAcceleratedDate', blank=True) # Field name made lowercase.
    optionsbackdating = models.TextField(db_column='OptionsBackdating', blank=True) # Field name made lowercase.
    year = models.TextField(db_column='YEAR', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'wrds_companies_2011'

class WrdsCompanies2012(models.Model):
    ticker = models.TextField(db_column='Ticker', blank=True) # Field name made lowercase.
    companyname = models.TextField(db_column='CompanyName', blank=True) # Field name made lowercase.
    cik = models.TextField(db_column='CIK', blank=True) # Field name made lowercase.
    cusip = models.TextField(db_column='CUSIP', blank=True) # Field name made lowercase.
    companyfedid = models.TextField(db_column='CompanyFedID', blank=True) # Field name made lowercase.
    companyage = models.TextField(db_column='CompanyAge', blank=True) # Field name made lowercase.
    compfounded = models.TextField(db_column='CompFounded', blank=True) # Field name made lowercase.
    incorporationcountry = models.TextField(db_column='IncorporationCountry', blank=True) # Field name made lowercase.
    statehq = models.TextField(db_column='StateHQ', blank=True) # Field name made lowercase.
    stateinc = models.TextField(db_column='StateInc', blank=True) # Field name made lowercase.
    exchange = models.TextField(db_column='Exchange', blank=True) # Field name made lowercase.
    address1 = models.TextField(db_column='Address1', blank=True) # Field name made lowercase.
    address2 = models.TextField(db_column='Address2', blank=True) # Field name made lowercase.
    address3 = models.TextField(db_column='Address3', blank=True) # Field name made lowercase.
    city = models.TextField(db_column='City', blank=True) # Field name made lowercase.
    state = models.TextField(db_column='State', blank=True) # Field name made lowercase.
    postalcode = models.TextField(db_column='PostalCode', blank=True) # Field name made lowercase.
    mailcountry = models.TextField(db_column='MailCountry', blank=True) # Field name made lowercase.
    phone_fax = models.TextField(db_column='Phone_Fax', blank=True) # Field name made lowercase.
    phone = models.TextField(db_column='Phone', blank=True) # Field name made lowercase.
    indexfortune = models.TextField(db_column='IndexFortune', blank=True) # Field name made lowercase.
    indexrussell = models.TextField(db_column='IndexRussell', blank=True) # Field name made lowercase.
    indexsp = models.TextField(db_column='IndexSP', blank=True) # Field name made lowercase.
    industry = models.TextField(db_column='Industry', blank=True) # Field name made lowercase.
    sic = models.TextField(db_column='SIC', blank=True) # Field name made lowercase.
    sicdescription = models.TextField(db_column='SICDescription', blank=True) # Field name made lowercase.
    insiderscontrol = models.TextField(db_column='InsidersControl', blank=True) # Field name made lowercase.
    insiderspctg = models.TextField(db_column='InsidersPctg', blank=True) # Field name made lowercase.
    insiderspluspctg = models.TextField(db_column='InsidersPlusPctg', blank=True) # Field name made lowercase.
    institutionalmajority = models.TextField(db_column='InstitutionalMajority', blank=True) # Field name made lowercase.
    annualmtg = models.TextField(db_column='AnnualMtg', blank=True) # Field name made lowercase.
    fiscalyrend = models.TextField(db_column='FiscalYrEnd', blank=True) # Field name made lowercase.
    annualmtgplace = models.TextField(db_column='AnnualMtgPlace', blank=True) # Field name made lowercase.
    annualmtgnext = models.TextField(db_column='AnnualMtgNext', blank=True) # Field name made lowercase.
    proxydate = models.TextField(db_column='ProxyDate', blank=True) # Field name made lowercase.
    ownersfivepercentpctg = models.TextField(db_column='OwnersFivePercentPctg', blank=True) # Field name made lowercase.
    ownershipcategory = models.TextField(db_column='OwnershipCategory', blank=True) # Field name made lowercase.
    auditfees = models.TextField(db_column='AuditFees', blank=True) # Field name made lowercase.
    auditfeesother = models.TextField(db_column='AuditFeesOther', blank=True) # Field name made lowercase.
    auditfeesprcntg = models.TextField(db_column='AuditFeesPrcntg', blank=True) # Field name made lowercase.
    auditfeesrelated = models.TextField(db_column='AuditFeesRelated', blank=True) # Field name made lowercase.
    auditfeestax = models.TextField(db_column='AuditFeesTax', blank=True) # Field name made lowercase.
    auditfeestotal = models.TextField(db_column='AuditFeesTotal', blank=True) # Field name made lowercase.
    auditnonauditfeespctg = models.TextField(db_column='AuditNonAuditFeesPctg', blank=True) # Field name made lowercase.
    auditor = models.TextField(db_column='Auditor', blank=True) # Field name made lowercase.
    auditorchangenotes = models.TextField(db_column='AuditorChangeNotes', blank=True) # Field name made lowercase.
    auditorindependent = models.TextField(db_column='AuditorIndependent', blank=True) # Field name made lowercase.
    auditornominee = models.TextField(db_column='AuditorNominee', blank=True) # Field name made lowercase.
    auditorprevious = models.TextField(db_column='AuditorPrevious', blank=True) # Field name made lowercase.
    auditorsince = models.TextField(db_column='AuditorSince', blank=True) # Field name made lowercase.
    bdmtgs = models.TextField(db_column='BDMtgs', blank=True) # Field name made lowercase.
    bdmtgsoutside = models.TextField(db_column='BdMtgsOutside', blank=True) # Field name made lowercase.
    bdoutsidemaj = models.TextField(db_column='BdOutsideMaj', blank=True) # Field name made lowercase.
    bdoutsidemajstrict = models.TextField(db_column='BdOutsideMajStrict', blank=True) # Field name made lowercase.
    bdoutsidemeets = models.TextField(db_column='BDOutsideMeets', blank=True) # Field name made lowercase.
    bdoutsidemtgsource = models.TextField(db_column='BdOutsideMtgSource', blank=True) # Field name made lowercase.
    busethicscode = models.TextField(db_column='BusEthicsCode', blank=True) # Field name made lowercase.
    chairmanis = models.TextField(db_column='ChairmanIs', blank=True) # Field name made lowercase.
    chiefgovofficerfname = models.TextField(db_column='ChiefGovOfficerFName', blank=True) # Field name made lowercase.
    chiefgovofficerlname = models.TextField(db_column='ChiefGovOfficerLName', blank=True) # Field name made lowercase.
    corpsecretaryfname = models.TextField(db_column='CorpSecretaryFName', blank=True) # Field name made lowercase.
    corpsecretarylname = models.TextField(db_column='CorpSecretaryLName', blank=True) # Field name made lowercase.
    gencounselfname = models.TextField(db_column='GenCounselFName', blank=True) # Field name made lowercase.
    gencounsellname = models.TextField(db_column='GenCounselLName', blank=True) # Field name made lowercase.
    leaddirectorfname = models.TextField(db_column='LeadDirectorFName', blank=True) # Field name made lowercase.
    leaddirectorlname = models.TextField(db_column='LeadDirectorLName', blank=True) # Field name made lowercase.
    leadlawfirm = models.TextField(db_column='LeadLawFirm', blank=True) # Field name made lowercase.
    commauditindependent = models.TextField(db_column='CommAuditIndependent', blank=True) # Field name made lowercase.
    commauditfullyindependent = models.TextField(db_column='CommAuditFullyIndependent', blank=True) # Field name made lowercase.
    commcompindependent = models.TextField(db_column='CommCompIndependent', blank=True) # Field name made lowercase.
    commcompfullyindependent = models.TextField(db_column='CommCompFullyIndependent', blank=True) # Field name made lowercase.
    committeenomgovindependent = models.TextField(db_column='CommitteeNomGovIndependent', blank=True) # Field name made lowercase.
    committeenomgovfullyindependent = models.TextField(db_column='CommitteeNomGovFullyIndependent', blank=True) # Field name made lowercase.
    govpolicy = models.TextField(db_column='GovPolicy', blank=True) # Field name made lowercase.
    notesdircomp = models.TextField(db_column='NotesDirComp', blank=True) # Field name made lowercase.
    directorsactiveceos = models.TextField(db_column='DirectorsActiveCEOs', blank=True) # Field name made lowercase.
    directorsactiveceopct = models.TextField(db_column='DirectorsActiveCEOPct', blank=True) # Field name made lowercase.
    directorsfailed = models.TextField(db_column='DirectorsFailed', blank=True) # Field name made lowercase.
    directorsfailedpct = models.TextField(db_column='DirectorsFailedPct', blank=True) # Field name made lowercase.
    directorsinside = models.TextField(db_column='DirectorsInside', blank=True) # Field name made lowercase.
    directorsinsidepct = models.TextField(db_column='DirectorsInsidePct', blank=True) # Field name made lowercase.
    directorsoutside = models.TextField(db_column='DirectorsOutside', blank=True) # Field name made lowercase.
    directorsoutsiderelated = models.TextField(db_column='DirectorsOutsideRelated', blank=True) # Field name made lowercase.
    directorsoutsiderelatedpct = models.TextField(db_column='DirectorsOutsideRelatedPct', blank=True) # Field name made lowercase.
    directorsoutsidetotal = models.TextField(db_column='DirectorsOutsideTotal', blank=True) # Field name made lowercase.
    directorsover10yrstenure = models.TextField(db_column='DirectorsOver10YrsTenure', blank=True) # Field name made lowercase.
    directorsover10yrstenurepct = models.TextField(db_column='DirectorsOver10YrsTenurePct', blank=True) # Field name made lowercase.
    directorsover15yrstenure = models.TextField(db_column='DirectorsOver15YrsTenure', blank=True) # Field name made lowercase.
    directorsover15yrstenurepct = models.TextField(db_column='DirectorsOver15YrsTenurePct', blank=True) # Field name made lowercase.
    directorsover4boards = models.TextField(db_column='DirectorsOver4Boards', blank=True) # Field name made lowercase.
    directorsover4publicboards = models.TextField(db_column='DirectorsOver4PublicBoards', blank=True) # Field name made lowercase.
    directorsover4publicboardspct = models.TextField(db_column='DirectorsOver4PublicBoardsPct', blank=True) # Field name made lowercase.
    directorsover70 = models.TextField(db_column='DirectorsOver70', blank=True) # Field name made lowercase.
    directorsover70pct = models.TextField(db_column='DirectorsOver70Pct', blank=True) # Field name made lowercase.
    directorsproblem = models.TextField(db_column='DirectorsProblem', blank=True) # Field name made lowercase.
    directorsproblempct = models.TextField(db_column='DirectorsProblemPct', blank=True) # Field name made lowercase.
    directorswomen = models.TextField(db_column='DirectorsWomen', blank=True) # Field name made lowercase.
    directorswomenpct = models.TextField(db_column='DirectorsWomenPct', blank=True) # Field name made lowercase.
    directorszeroshares = models.TextField(db_column='DirectorsZeroShares', blank=True) # Field name made lowercase.
    directorszerosharesandtenureover = models.TextField(db_column='DirectorsZeroSharesAndTenureOver', blank=True) # Field name made lowercase.
    directorszerosharesandtenureove1 = models.TextField(db_column='DirectorsZeroSharesAndTenureOve1', blank=True) # Field name made lowercase.
    directorstotal = models.TextField(db_column='DirectorsTotal', blank=True) # Field name made lowercase.
    compdescription = models.TextField(db_column='CompDescription', blank=True) # Field name made lowercase.
    companyprofileshort = models.TextField(db_column='CompanyProfileShort', blank=True) # Field name made lowercase.
    controlledcompanyexemption = models.TextField(db_column='ControlledCompanyExemption', blank=True) # Field name made lowercase.
    voteauditorno = models.TextField(db_column='VoteAuditorNo', blank=True) # Field name made lowercase.
    optionsaccelerated = models.TextField(db_column='OptionsAccelerated', blank=True) # Field name made lowercase.
    optionsaccelerateddate = models.TextField(db_column='OptionsAcceleratedDate', blank=True) # Field name made lowercase.
    optionsbackdating = models.TextField(db_column='OptionsBackdating', blank=True) # Field name made lowercase.
    year = models.TextField(db_column='YEAR', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'wrds_companies_2012'

class WrdsDirectorship(models.Model):
    acceleratedoptions = models.TextField(db_column='ACCELERATEDOPTIONS', blank=True) # Field name made lowercase.
    activeceo = models.TextField(db_column='ACTIVECEO', blank=True) # Field name made lowercase.
    addbusinessname = models.TextField(db_column='ADDBUSINESSNAME', blank=True) # Field name made lowercase.
    addcity = models.TextField(db_column='ADDCITY', blank=True) # Field name made lowercase.
    addcountry = models.TextField(db_column='ADDCOUNTRY', blank=True) # Field name made lowercase.
    addexectitle = models.TextField(db_column='ADDEXECTITLE', blank=True) # Field name made lowercase.
    addpostcode = models.TextField(db_column='ADDPOSTCODE', blank=True) # Field name made lowercase.
    address1 = models.TextField(db_column='ADDRESS1', blank=True) # Field name made lowercase.
    address1a = models.TextField(db_column='ADDRESS1A', blank=True) # Field name made lowercase.
    address2 = models.TextField(db_column='ADDRESS2', blank=True) # Field name made lowercase.
    address3 = models.TextField(db_column='ADDRESS3', blank=True) # Field name made lowercase.
    addstate = models.TextField(db_column='ADDSTATE', blank=True) # Field name made lowercase.
    auditor = models.TextField(db_column='AUDITOR', blank=True) # Field name made lowercase.
    boardname = models.TextField(db_column='BOARDNAME', blank=True) # Field name made lowercase.
    ceoischairman = models.TextField(db_column='CEOISCHAIRMAN', blank=True) # Field name made lowercase.
    cfosince = models.TextField(db_column='CFOSINCE', blank=True) # Field name made lowercase.
    cfountil = models.TextField(db_column='CFOUNTIL', blank=True) # Field name made lowercase.
    cik = models.TextField(db_column='CIK', blank=True) # Field name made lowercase.
    city = models.TextField(db_column='CITY', blank=True) # Field name made lowercase.
    committeeaudit = models.TextField(db_column='COMMITTEEAUDIT', blank=True) # Field name made lowercase.
    committeeauditfinancialexpert = models.TextField(db_column='COMMITTEEAUDITFINANCIALEXPERT', blank=True) # Field name made lowercase.
    committeecompensation = models.TextField(db_column='COMMITTEECOMPENSATION', blank=True) # Field name made lowercase.
    committeeexecutive = models.TextField(db_column='COMMITTEEEXECUTIVE', blank=True) # Field name made lowercase.
    committeegovernance = models.TextField(db_column='COMMITTEEGOVERNANCE', blank=True) # Field name made lowercase.
    committeenominating = models.TextField(db_column='COMMITTEENOMINATING', blank=True) # Field name made lowercase.
    companyname = models.TextField(db_column='COMPANYNAME', blank=True) # Field name made lowercase.
    compid = models.TextField(db_column='COMPID', blank=True) # Field name made lowercase.
    country = models.TextField(db_column='COUNTRY', blank=True) # Field name made lowercase.
    datebegan = models.TextField(db_column='DATEBEGAN', blank=True) # Field name made lowercase.
    dateended = models.TextField(db_column='DATEENDED', blank=True) # Field name made lowercase.
    dateretiring = models.TextField(db_column='DATERETIRING', blank=True) # Field name made lowercase.
    dc_totalalldirectorshipscompensa = models.TextField(db_column='DC_TOTALALLDIRECTORSHIPSCOMPENSA', blank=True) # Field name made lowercase.
    dc_totalcompanycompensation = models.TextField(db_column='DC_TOTALCOMPANYCOMPENSATION', blank=True) # Field name made lowercase.
    dirage = models.TextField(db_column='DIRAGE', blank=True) # Field name made lowercase.
    dirattendance = models.TextField(db_column='DIRATTENDANCE', blank=True) # Field name made lowercase.
    dirbasepay = models.TextField(db_column='DIRBASEPAY', blank=True) # Field name made lowercase.
    directorsaudittotal = models.TextField(db_column='DIRECTORSAUDITTOTAL', blank=True) # Field name made lowercase.
    directorscompensationtotal = models.TextField(db_column='DIRECTORSCOMPENSATIONTOTAL', blank=True) # Field name made lowercase.
    directorsexecutivetotal = models.TextField(db_column='DIRECTORSEXECUTIVETOTAL', blank=True) # Field name made lowercase.
    directorsgovernancetotal = models.TextField(db_column='DIRECTORSGOVERNANCETOTAL', blank=True) # Field name made lowercase.
    directorsnominatingtotal = models.TextField(db_column='DIRECTORSNOMINATINGTOTAL', blank=True) # Field name made lowercase.
    directorstotal = models.TextField(db_column='DIRECTORSTOTAL', blank=True) # Field name made lowercase.
    diremail = models.TextField(db_column='DIREMAIL', blank=True) # Field name made lowercase.
    dirfname = models.TextField(db_column='DIRFNAME', blank=True) # Field name made lowercase.
    dirgender = models.TextField(db_column='DIRGENDER', blank=True) # Field name made lowercase.
    dirlname = models.TextField(db_column='DIRLNAME', blank=True) # Field name made lowercase.
    dirmultiple = models.TextField(db_column='DIRMULTIPLE', blank=True) # Field name made lowercase.
    dirmultiple_newprivate = models.TextField(db_column='DIRMULTIPLE_NEWPRIVATE', blank=True) # Field name made lowercase.
    dirmultiple_newpublic = models.TextField(db_column='DIRMULTIPLE_NEWPUBLIC', blank=True) # Field name made lowercase.
    diroutside = models.TextField(db_column='DIROUTSIDE', blank=True) # Field name made lowercase.
    dirphone1 = models.TextField(db_column='DIRPHONE1', blank=True) # Field name made lowercase.
    dirphonefax = models.TextField(db_column='DIRPHONEFAX', blank=True) # Field name made lowercase.
    dirprofile = models.TextField(db_column='DIRPROFILE', blank=True) # Field name made lowercase.
    dirprofile1 = models.TextField(db_column='DIRPROFILE1', blank=True) # Field name made lowercase.
    dirprofile2 = models.TextField(db_column='DIRPROFILE2', blank=True) # Field name made lowercase.
    dirprofilebasic = models.TextField(db_column='DIRPROFILEBASIC', blank=True) # Field name made lowercase.
    dirreasonended = models.TextField(db_column='DIRREASONENDED', blank=True) # Field name made lowercase.
    dirreelectionyear = models.TextField(db_column='DIRREELECTIONYEAR', blank=True) # Field name made lowercase.
    dirretiredreason = models.TextField(db_column='DIRRETIREDREASON', blank=True) # Field name made lowercase.
    dirsharesexerciseableoptions = models.TextField(db_column='DIRSHARESEXERCISEABLEOPTIONS', blank=True) # Field name made lowercase.
    dirsharesheld = models.TextField(db_column='DIRSHARESHELD', blank=True) # Field name made lowercase.
    dirsharesreported = models.TextField(db_column='DIRSHARESREPORTED', blank=True) # Field name made lowercase.
    dirsharesvalue = models.TextField(db_column='DIRSHARESVALUE', blank=True) # Field name made lowercase.
    dirsharesvotingpower = models.TextField(db_column='DIRSHARESVOTINGPOWER', blank=True) # Field name made lowercase.
    dirsince = models.TextField(db_column='DIRSINCE', blank=True) # Field name made lowercase.
    dirstatus = models.TextField(db_column='DIRSTATUS', blank=True) # Field name made lowercase.
    dirtenure = models.TextField(db_column='DIRTENURE', blank=True) # Field name made lowercase.
    diryrofbirth = models.TextField(db_column='DIRYROFBIRTH', blank=True) # Field name made lowercase.
    employees = models.TextField(db_column='EMPLOYEES', blank=True) # Field name made lowercase.
    exchange = models.TextField(db_column='EXCHANGE', blank=True) # Field name made lowercase.
    executivetitle = models.TextField(db_column='EXECUTIVETITLE', blank=True) # Field name made lowercase.
    fiscalyrend = models.TextField(db_column='FISCALYREND', blank=True) # Field name made lowercase.
    gics_industry = models.TextField(db_column='GICS_INDUSTRY', blank=True) # Field name made lowercase.
    highest_executive_title = models.TextField(db_column='HIGHEST_EXECUTIVE_TITLE', blank=True) # Field name made lowercase.
    iddir = models.TextField(db_column='IDDIR', blank=True) # Field name made lowercase.
    iddirship = models.TextField(db_column='IDDIRSHIP', blank=True) # Field name made lowercase.
    id_individual = models.TextField(db_column='ID_INDIVIDUAL', blank=True) # Field name made lowercase.
    indexfortune = models.TextField(db_column='INDEXFORTUNE', blank=True) # Field name made lowercase.
    indexrussell = models.TextField(db_column='INDEXRUSSELL', blank=True) # Field name made lowercase.
    indexsp = models.TextField(db_column='INDEXSP', blank=True) # Field name made lowercase.
    industry = models.TextField(db_column='INDUSTRY', blank=True) # Field name made lowercase.
    insiderspctg = models.TextField(db_column='INSIDERSPCTG', blank=True) # Field name made lowercase.
    institutionpctg = models.TextField(db_column='INSTITUTIONPCTG', blank=True) # Field name made lowercase.
    isceo = models.TextField(db_column='ISCEO', blank=True) # Field name made lowercase.
    isceo2 = models.TextField(db_column='ISCEO2', blank=True) # Field name made lowercase.
    iscfo = models.TextField(db_column='ISCFO', blank=True) # Field name made lowercase.
    ischairman = models.TextField(db_column='ISCHAIRMAN', blank=True) # Field name made lowercase.
    iscochair = models.TextField(db_column='ISCOCHAIR', blank=True) # Field name made lowercase.
    isformerleaddirector = models.TextField(db_column='ISFORMERLEADDIRECTOR', blank=True) # Field name made lowercase.
    isfounder = models.TextField(db_column='ISFOUNDER', blank=True) # Field name made lowercase.
    isleaddirector = models.TextField(db_column='ISLEADDIRECTOR', blank=True) # Field name made lowercase.
    linkbadirprofile = models.TextField(db_column='LINKBADIRPROFILE', blank=True) # Field name made lowercase.
    linkproxy = models.TextField(db_column='LINKPROXY', blank=True) # Field name made lowercase.
    marketcap = models.TextField(db_column='MARKETCAP', blank=True) # Field name made lowercase.
    nationality = models.TextField(db_column='NATIONALITY', blank=True) # Field name made lowercase.
    notesdircomp = models.TextField(db_column='NOTESDIRCOMP', blank=True) # Field name made lowercase.
    phone = models.TextField(db_column='PHONE', blank=True) # Field name made lowercase.
    phonefax = models.TextField(db_column='PHONEFAX', blank=True) # Field name made lowercase.
    phone_fax = models.TextField(db_column='PHONE_FAX', blank=True) # Field name made lowercase.
    position = models.TextField(db_column='POSITION', blank=True) # Field name made lowercase.
    position_date_began = models.TextField(db_column='POSITION_DATE_BEGAN', blank=True) # Field name made lowercase.
    position_date_ended = models.TextField(db_column='POSITION_DATE_ENDED', blank=True) # Field name made lowercase.
    position_status = models.TextField(db_column='POSITION_STATUS', blank=True) # Field name made lowercase.
    postalcode = models.TextField(db_column='POSTALCODE', blank=True) # Field name made lowercase.
    prefix = models.TextField(db_column='PREFIX', blank=True) # Field name made lowercase.
    problemdirector = models.TextField(db_column='PROBLEMDIRECTOR', blank=True) # Field name made lowercase.
    problemdirectoryn = models.TextField(db_column='PROBLEMDIRECTORYN', blank=True) # Field name made lowercase.
    proxydate = models.TextField(db_column='PROXYDATE', blank=True) # Field name made lowercase.
    relstatus = models.TextField(db_column='RELSTATUS', blank=True) # Field name made lowercase.
    sic1 = models.TextField(db_column='SIC1', blank=True) # Field name made lowercase.
    sic1descript = models.TextField(db_column='SIC1DESCRIPT', blank=True) # Field name made lowercase.
    sic2 = models.TextField(db_column='SIC2', blank=True) # Field name made lowercase.
    sic2descript = models.TextField(db_column='SIC2DESCRIPT', blank=True) # Field name made lowercase.
    state = models.TextField(db_column='STATE', blank=True) # Field name made lowercase.
    statehq = models.TextField(db_column='STATEHQ', blank=True) # Field name made lowercase.
    stateinc = models.TextField(db_column='STATEINC', blank=True) # Field name made lowercase.
    suffix = models.TextField(db_column='SUFFIX', blank=True) # Field name made lowercase.
    sumover4publicboards = models.TextField(db_column='SUMOVER4PUBLICBOARDS', blank=True) # Field name made lowercase.
    sumoverfourpublicboards = models.TextField(db_column='SUMOVERFOURPUBLICBOARDS', blank=True) # Field name made lowercase.
    tenure = models.TextField(db_column='TENURE', blank=True) # Field name made lowercase.
    ticker = models.TextField(db_column='TICKER', blank=True) # Field name made lowercase.
    totalindcompensation = models.TextField(db_column='TOTALINDCOMPENSATION', blank=True) # Field name made lowercase.
    year = models.TextField(db_column='YEAR', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'wrds_directorship'

class WrdsDirectorship20012007(models.Model):
    ticker = models.TextField(db_column='TICKER', blank=True) # Field name made lowercase.
    companyname = models.TextField(db_column='COMPANYNAME', blank=True) # Field name made lowercase.
    year = models.TextField(db_column='YEAR', blank=True) # Field name made lowercase.
    acceleratedoptions = models.TextField(db_column='ACCELERATEDOPTIONS', blank=True) # Field name made lowercase.
    addexectitle = models.TextField(db_column='ADDEXECTITLE', blank=True) # Field name made lowercase.
    diroutside = models.TextField(db_column='DIROUTSIDE', blank=True) # Field name made lowercase.
    dirstatus = models.TextField(db_column='DIRSTATUS', blank=True) # Field name made lowercase.
    industry = models.TextField(db_column='INDUSTRY', blank=True) # Field name made lowercase.
    address1a = models.TextField(db_column='ADDRESS1A', blank=True) # Field name made lowercase.
    activeceo = models.TextField(db_column='ACTIVECEO', blank=True) # Field name made lowercase.
    addbusinessname = models.TextField(db_column='ADDBUSINESSNAME', blank=True) # Field name made lowercase.
    addcity = models.TextField(db_column='ADDCITY', blank=True) # Field name made lowercase.
    addcountry = models.TextField(db_column='ADDCOUNTRY', blank=True) # Field name made lowercase.
    addpostcode = models.TextField(db_column='ADDPOSTCODE', blank=True) # Field name made lowercase.
    address1 = models.TextField(db_column='ADDRESS1', blank=True) # Field name made lowercase.
    address2 = models.TextField(db_column='ADDRESS2', blank=True) # Field name made lowercase.
    addstate = models.TextField(db_column='ADDSTATE', blank=True) # Field name made lowercase.
    auditor = models.TextField(db_column='AUDITOR', blank=True) # Field name made lowercase.
    boardname = models.TextField(db_column='BOARDNAME', blank=True) # Field name made lowercase.
    ceoischairman = models.TextField(db_column='CEOISCHAIRMAN', blank=True) # Field name made lowercase.
    cik = models.TextField(db_column='CIK', blank=True) # Field name made lowercase.
    committeeaudit = models.TextField(db_column='COMMITTEEAUDIT', blank=True) # Field name made lowercase.
    committeeauditfinancialexpert = models.TextField(db_column='COMMITTEEAUDITFINANCIALEXPERT', blank=True) # Field name made lowercase.
    committeecompensation = models.TextField(db_column='COMMITTEECOMPENSATION', blank=True) # Field name made lowercase.
    committeeexecutive = models.TextField(db_column='COMMITTEEEXECUTIVE', blank=True) # Field name made lowercase.
    committeegovernance = models.TextField(db_column='COMMITTEEGOVERNANCE', blank=True) # Field name made lowercase.
    committeenominating = models.TextField(db_column='COMMITTEENOMINATING', blank=True) # Field name made lowercase.
    compid = models.TextField(db_column='COMPID', blank=True) # Field name made lowercase.
    country = models.TextField(db_column='COUNTRY', blank=True) # Field name made lowercase.
    dirage = models.TextField(db_column='DIRAGE', blank=True) # Field name made lowercase.
    dirattendance = models.TextField(db_column='DIRATTENDANCE', blank=True) # Field name made lowercase.
    dirbasepay = models.TextField(db_column='DIRBASEPAY', blank=True) # Field name made lowercase.
    diremail = models.TextField(db_column='DIREMAIL', blank=True) # Field name made lowercase.
    dirfname = models.TextField(db_column='DIRFNAME', blank=True) # Field name made lowercase.
    dirgender = models.TextField(db_column='DIRGENDER', blank=True) # Field name made lowercase.
    dirlname = models.TextField(db_column='DIRLNAME', blank=True) # Field name made lowercase.
    dirmultiple = models.TextField(db_column='DIRMULTIPLE', blank=True) # Field name made lowercase.
    dirphone1 = models.TextField(db_column='DIRPHONE1', blank=True) # Field name made lowercase.
    dirphonefax = models.TextField(db_column='DIRPHONEFAX', blank=True) # Field name made lowercase.
    dirprofile = models.TextField(db_column='DIRPROFILE', blank=True) # Field name made lowercase.
    dirprofilebasic = models.TextField(db_column='DIRPROFILEBASIC', blank=True) # Field name made lowercase.
    dirsharesexerciseableoptions = models.TextField(db_column='DIRSHARESEXERCISEABLEOPTIONS', blank=True) # Field name made lowercase.
    dirsharesheld = models.TextField(db_column='DIRSHARESHELD', blank=True) # Field name made lowercase.
    dirsharesreported = models.TextField(db_column='DIRSHARESREPORTED', blank=True) # Field name made lowercase.
    dirsharesvalue = models.TextField(db_column='DIRSHARESVALUE', blank=True) # Field name made lowercase.
    dirsharesvotingpower = models.TextField(db_column='DIRSHARESVOTINGPOWER', blank=True) # Field name made lowercase.
    dirsince = models.TextField(db_column='DIRSINCE', blank=True) # Field name made lowercase.
    dirtenure = models.TextField(db_column='DIRTENURE', blank=True) # Field name made lowercase.
    diryrofbirth = models.TextField(db_column='DIRYROFBIRTH', blank=True) # Field name made lowercase.
    employees = models.TextField(db_column='EMPLOYEES', blank=True) # Field name made lowercase.
    exchange = models.TextField(db_column='EXCHANGE', blank=True) # Field name made lowercase.
    executivetitle = models.TextField(db_column='EXECUTIVETITLE', blank=True) # Field name made lowercase.
    fiscalyrend = models.TextField(db_column='FISCALYREND', blank=True) # Field name made lowercase.
    iddir = models.TextField(db_column='IDDIR', blank=True) # Field name made lowercase.
    indexfortune = models.TextField(db_column='INDEXFORTUNE', blank=True) # Field name made lowercase.
    indexrussell = models.TextField(db_column='INDEXRUSSELL', blank=True) # Field name made lowercase.
    indexsp = models.TextField(db_column='INDEXSP', blank=True) # Field name made lowercase.
    insiderspctg = models.TextField(db_column='INSIDERSPCTG', blank=True) # Field name made lowercase.
    institutionpctg = models.TextField(db_column='INSTITUTIONPCTG', blank=True) # Field name made lowercase.
    isceo = models.TextField(db_column='ISCEO', blank=True) # Field name made lowercase.
    iscfo = models.TextField(db_column='ISCFO', blank=True) # Field name made lowercase.
    ischairman = models.TextField(db_column='ISCHAIRMAN', blank=True) # Field name made lowercase.
    iscochair = models.TextField(db_column='ISCOCHAIR', blank=True) # Field name made lowercase.
    isfounder = models.TextField(db_column='ISFOUNDER', blank=True) # Field name made lowercase.
    isleaddirector = models.TextField(db_column='ISLEADDIRECTOR', blank=True) # Field name made lowercase.
    linkbadirprofile = models.TextField(db_column='LINKBADIRPROFILE', blank=True) # Field name made lowercase.
    linkproxy = models.TextField(db_column='LINKPROXY', blank=True) # Field name made lowercase.
    marketcap = models.TextField(db_column='MARKETCAP', blank=True) # Field name made lowercase.
    nationality = models.TextField(db_column='NATIONALITY', blank=True) # Field name made lowercase.
    notesdircomp = models.TextField(db_column='NOTESDIRCOMP', blank=True) # Field name made lowercase.
    prefix = models.TextField(db_column='PREFIX', blank=True) # Field name made lowercase.
    problemdirectoryn = models.TextField(db_column='PROBLEMDIRECTORYN', blank=True) # Field name made lowercase.
    proxydate = models.TextField(db_column='PROXYDATE', blank=True) # Field name made lowercase.
    sic1 = models.TextField(db_column='SIC1', blank=True) # Field name made lowercase.
    sic1descript = models.TextField(db_column='SIC1DESCRIPT', blank=True) # Field name made lowercase.
    sic2 = models.TextField(db_column='SIC2', blank=True) # Field name made lowercase.
    sic2descript = models.TextField(db_column='SIC2DESCRIPT', blank=True) # Field name made lowercase.
    statehq = models.TextField(db_column='STATEHQ', blank=True) # Field name made lowercase.
    stateinc = models.TextField(db_column='STATEINC', blank=True) # Field name made lowercase.
    suffix = models.TextField(db_column='SUFFIX', blank=True) # Field name made lowercase.
    dateretiring = models.TextField(db_column='DATERETIRING', blank=True) # Field name made lowercase.
    iddirship = models.TextField(db_column='IDDIRSHIP', blank=True) # Field name made lowercase.
    directorsexecutivetotal = models.TextField(db_column='DIRECTORSEXECUTIVETOTAL', blank=True) # Field name made lowercase.
    directorstotal = models.TextField(db_column='DIRECTORSTOTAL', blank=True) # Field name made lowercase.
    directorsaudittotal = models.TextField(db_column='DIRECTORSAUDITTOTAL', blank=True) # Field name made lowercase.
    directorscompensationtotal = models.TextField(db_column='DIRECTORSCOMPENSATIONTOTAL', blank=True) # Field name made lowercase.
    directorsgovernancetotal = models.TextField(db_column='DIRECTORSGOVERNANCETOTAL', blank=True) # Field name made lowercase.
    directorsnominatingtotal = models.TextField(db_column='DIRECTORSNOMINATINGTOTAL', blank=True) # Field name made lowercase.
    dirreelectionyear = models.TextField(db_column='DIRREELECTIONYEAR', blank=True) # Field name made lowercase.
    dirretiredreason = models.TextField(db_column='DIRRETIREDREASON', blank=True) # Field name made lowercase.
    isceo2 = models.TextField(db_column='ISCEO2', blank=True) # Field name made lowercase.
    isformerleaddirector = models.TextField(db_column='ISFORMERLEADDIRECTOR', blank=True) # Field name made lowercase.
    sumover4publicboards = models.TextField(db_column='SUMOVER4PUBLICBOARDS', blank=True) # Field name made lowercase.
    dc_totalalldirectorshipscompensa = models.TextField(db_column='DC_TOTALALLDIRECTORSHIPSCOMPENSA', blank=True) # Field name made lowercase.
    problemdirector = models.TextField(db_column='PROBLEMDIRECTOR', blank=True) # Field name made lowercase.
    dirmultiple_newprivate = models.TextField(db_column='DIRMULTIPLE_NEWPRIVATE', blank=True) # Field name made lowercase.
    dirmultiple_newpublic = models.TextField(db_column='DIRMULTIPLE_NEWPUBLIC', blank=True) # Field name made lowercase.
    dc_totalcompanycompensation = models.TextField(db_column='DC_TOTALCOMPANYCOMPENSATION', blank=True) # Field name made lowercase.
    cfosince = models.TextField(db_column='CFOSINCE', blank=True) # Field name made lowercase.
    cfountil = models.TextField(db_column='CFOUNTIL', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'wrds_directorship_2001_2007'

class WrdsDirectorship2008(models.Model):
    acceleratedoptions = models.TextField(db_column='AcceleratedOptions', blank=True) # Field name made lowercase.
    activeceo = models.TextField(db_column='ActiveCEO', blank=True) # Field name made lowercase.
    addbusinessname = models.TextField(db_column='AddBusinessName', blank=True) # Field name made lowercase.
    addcity = models.TextField(db_column='AddCity', blank=True) # Field name made lowercase.
    addcountry = models.TextField(db_column='AddCountry', blank=True) # Field name made lowercase.
    addexectitle = models.TextField(db_column='AddExecTitle', blank=True) # Field name made lowercase.
    addstate = models.TextField(db_column='AddState', blank=True) # Field name made lowercase.
    address1 = models.TextField(db_column='Address1', blank=True) # Field name made lowercase.
    address2 = models.TextField(db_column='Address2', blank=True) # Field name made lowercase.
    address1a = models.TextField(db_column='Address1A', blank=True) # Field name made lowercase.
    committeeaudit = models.TextField(db_column='CommitteeAudit', blank=True) # Field name made lowercase.
    committeeauditfinancialexpert = models.TextField(db_column='CommitteeAuditFinancialExpert', blank=True) # Field name made lowercase.
    committeecompensation = models.TextField(db_column='CommitteeCompensation', blank=True) # Field name made lowercase.
    committeeexecutive = models.TextField(db_column='CommitteeExecutive', blank=True) # Field name made lowercase.
    committeegovernance = models.TextField(db_column='CommitteeGovernance', blank=True) # Field name made lowercase.
    committeenominating = models.TextField(db_column='CommitteeNominating', blank=True) # Field name made lowercase.
    companyname = models.TextField(db_column='CompanyName', blank=True) # Field name made lowercase.
    dirattendance = models.TextField(db_column='DirAttendance', blank=True) # Field name made lowercase.
    diremail = models.TextField(db_column='DirEMail', blank=True) # Field name made lowercase.
    dirfname = models.TextField(db_column='DirFName', blank=True) # Field name made lowercase.
    dirgender = models.TextField(db_column='DirGender', blank=True) # Field name made lowercase.
    dirlname = models.TextField(db_column='DirLName', blank=True) # Field name made lowercase.
    diroutside = models.TextField(db_column='DirOutside', blank=True) # Field name made lowercase.
    dirphone1 = models.TextField(db_column='DirPhone1', blank=True) # Field name made lowercase.
    dirphonefax = models.TextField(db_column='DirPhonefax', blank=True) # Field name made lowercase.
    dirreelectionyear = models.TextField(db_column='DirReelectionYear', blank=True) # Field name made lowercase.
    dirretiredreason = models.TextField(db_column='DirRetiredReason', blank=True) # Field name made lowercase.
    dirstatus = models.TextField(db_column='DirStatus', blank=True) # Field name made lowercase.
    executivetitle = models.TextField(db_column='ExecutiveTitle', blank=True) # Field name made lowercase.
    indexrussell = models.TextField(db_column='IndexRussell', blank=True) # Field name made lowercase.
    indexsp = models.TextField(db_column='IndexSP', blank=True) # Field name made lowercase.
    industry = models.TextField(db_column='Industry', blank=True) # Field name made lowercase.
    isceo = models.TextField(db_column='IsCEO', blank=True) # Field name made lowercase.
    isceo2 = models.TextField(db_column='IsCEO2', blank=True) # Field name made lowercase.
    iscfo = models.TextField(db_column='IsCFO', blank=True) # Field name made lowercase.
    ischairman = models.TextField(db_column='IsChairman', blank=True) # Field name made lowercase.
    iscochair = models.TextField(db_column='IsCoChair', blank=True) # Field name made lowercase.
    isformerleaddirector = models.TextField(db_column='IsFormerLeadDirector', blank=True) # Field name made lowercase.
    isfounder = models.TextField(db_column='IsFounder', blank=True) # Field name made lowercase.
    isleaddirector = models.TextField(db_column='IsLeadDirector', blank=True) # Field name made lowercase.
    prefix = models.TextField(db_column='Prefix', blank=True) # Field name made lowercase.
    problemdirectoryn = models.TextField(db_column='ProblemDirectorYN', blank=True) # Field name made lowercase.
    suffix = models.TextField(db_column='Suffix', blank=True) # Field name made lowercase.
    ticker = models.TextField(db_column='Ticker', blank=True) # Field name made lowercase.
    indexfortune = models.TextField(db_column='IndexFortune', blank=True) # Field name made lowercase.
    proxydate = models.TextField(db_column='ProxyDate', blank=True) # Field name made lowercase.
    iddir = models.TextField(db_column='IDDir', blank=True) # Field name made lowercase.
    dirsince = models.TextField(db_column='DirSince', blank=True) # Field name made lowercase.
    dirtenure = models.TextField(db_column='DirTenure', blank=True) # Field name made lowercase.
    dateretiring = models.TextField(db_column='DateRetiring', blank=True) # Field name made lowercase.
    dirsharesexerciseableoptions = models.TextField(db_column='DirSharesExerciseableOptions', blank=True) # Field name made lowercase.
    dirsharesheld = models.TextField(db_column='DirSharesHeld', blank=True) # Field name made lowercase.
    dirsharesreported = models.TextField(db_column='DirSharesReported', blank=True) # Field name made lowercase.
    dirsharesvalue = models.TextField(db_column='DirSharesValue', blank=True) # Field name made lowercase.
    dirsharesvotingpower = models.TextField(db_column='DirSharesVotingPower', blank=True) # Field name made lowercase.
    addpostcode = models.TextField(db_column='AddPostcode', blank=True) # Field name made lowercase.
    problemdirector = models.TextField(db_column='ProblemDirector', blank=True) # Field name made lowercase.
    dirage = models.TextField(db_column='DirAge', blank=True) # Field name made lowercase.
    diryrofbirth = models.TextField(db_column='DirYrofBirth', blank=True) # Field name made lowercase.
    dirmultiple = models.TextField(db_column='DirMultiple', blank=True) # Field name made lowercase.
    dirmultiple_newprivate = models.TextField(db_column='DirMultiple_NewPrivate', blank=True) # Field name made lowercase.
    dirmultiple_newpublic = models.TextField(db_column='DirMultiple_NewPublic', blank=True) # Field name made lowercase.
    totalindcompensation = models.TextField(db_column='TotalIndCompensation', blank=True) # Field name made lowercase.
    cfosince = models.TextField(db_column='CFOSince', blank=True) # Field name made lowercase.
    cfountil = models.TextField(db_column='CFOUntil', blank=True) # Field name made lowercase.
    sumoverfourpublicboards = models.TextField(blank=True)
    dc_totalcompanycompensation = models.TextField(db_column='dc_TotalCompanyCompensation', blank=True) # Field name made lowercase.
    dc_totalalldirectorshipscompensa = models.TextField(db_column='dc_TotalAllDirectorshipsCompensa', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'wrds_directorship_2008'

class WrdsDirectorship2009(models.Model):
    indexsp = models.TextField(db_column='IndexSP', blank=True) # Field name made lowercase.
    indexrussell = models.TextField(db_column='IndexRussell', blank=True) # Field name made lowercase.
    indexfortune = models.TextField(db_column='IndexFortune', blank=True) # Field name made lowercase.
    iddir = models.TextField(db_column='IDDir', blank=True) # Field name made lowercase.
    prefix = models.TextField(db_column='Prefix', blank=True) # Field name made lowercase.
    dirfname = models.TextField(db_column='DirFName', blank=True) # Field name made lowercase.
    dirlname = models.TextField(db_column='DirLName', blank=True) # Field name made lowercase.
    suffix = models.TextField(db_column='Suffix', blank=True) # Field name made lowercase.
    dirstatus = models.TextField(db_column='DirStatus', blank=True) # Field name made lowercase.
    dirsince = models.TextField(db_column='DirSince', blank=True) # Field name made lowercase.
    dirtenure = models.TextField(db_column='DirTenure', blank=True) # Field name made lowercase.
    dateended = models.TextField(db_column='DateEnded', blank=True) # Field name made lowercase.
    dirattendance = models.TextField(db_column='DirAttendance', blank=True) # Field name made lowercase.
    diroutside = models.TextField(db_column='DirOutside', blank=True) # Field name made lowercase.
    dirsharesexerciseableoptions = models.TextField(db_column='DirSharesExerciseableOptions', blank=True) # Field name made lowercase.
    dirsharesheld = models.TextField(db_column='DirSharesHeld', blank=True) # Field name made lowercase.
    dirsharesreported = models.TextField(db_column='DirSharesReported', blank=True) # Field name made lowercase.
    dirsharesvalue = models.TextField(db_column='DirSharesValue', blank=True) # Field name made lowercase.
    dirsharesvotingpower = models.TextField(db_column='DirSharesVotingPower', blank=True) # Field name made lowercase.
    isceo = models.TextField(db_column='IsCEO', blank=True) # Field name made lowercase.
    isceo2 = models.TextField(db_column='IsCEO2', blank=True) # Field name made lowercase.
    ischairman = models.TextField(db_column='IsChairman', blank=True) # Field name made lowercase.
    iscochair = models.TextField(db_column='IsCoChair', blank=True) # Field name made lowercase.
    iscfo = models.TextField(db_column='IsCFO', blank=True) # Field name made lowercase.
    isfounder = models.TextField(db_column='IsFounder', blank=True) # Field name made lowercase.
    isleaddirector = models.TextField(db_column='IsLeadDirector', blank=True) # Field name made lowercase.
    isformerleaddirector = models.TextField(db_column='IsFormerLeadDirector', blank=True) # Field name made lowercase.
    committeeauditfinancialexpert = models.TextField(db_column='CommitteeAuditFinancialExpert', blank=True) # Field name made lowercase.
    committeeaudit = models.TextField(db_column='CommitteeAudit', blank=True) # Field name made lowercase.
    committeeexecutive = models.TextField(db_column='CommitteeExecutive', blank=True) # Field name made lowercase.
    committeecompensation = models.TextField(db_column='CommitteeCompensation', blank=True) # Field name made lowercase.
    committeegovernance = models.TextField(db_column='CommitteeGovernance', blank=True) # Field name made lowercase.
    committeenominating = models.TextField(db_column='CommitteeNominating', blank=True) # Field name made lowercase.
    executivetitle = models.TextField(db_column='ExecutiveTitle', blank=True) # Field name made lowercase.
    addexectitle = models.TextField(db_column='AddExecTitle', blank=True) # Field name made lowercase.
    addbusinessname = models.TextField(db_column='AddBusinessName', blank=True) # Field name made lowercase.
    address1 = models.TextField(db_column='Address1', blank=True) # Field name made lowercase.
    address1a = models.TextField(db_column='Address1A', blank=True) # Field name made lowercase.
    address2 = models.TextField(db_column='Address2', blank=True) # Field name made lowercase.
    addcity = models.TextField(db_column='AddCity', blank=True) # Field name made lowercase.
    addstate = models.TextField(db_column='AddState', blank=True) # Field name made lowercase.
    addpostcode = models.TextField(db_column='AddPostcode', blank=True) # Field name made lowercase.
    addcountry = models.TextField(db_column='AddCountry', blank=True) # Field name made lowercase.
    dirphone1 = models.TextField(db_column='DirPhone1', blank=True) # Field name made lowercase.
    dirphonefax = models.TextField(db_column='DirPhonefax', blank=True) # Field name made lowercase.
    problemdirector = models.TextField(db_column='ProblemDirector', blank=True) # Field name made lowercase.
    problemdirectoryn = models.TextField(db_column='ProblemDirectorYN', blank=True) # Field name made lowercase.
    activeceo = models.TextField(db_column='ActiveCEO', blank=True) # Field name made lowercase.
    dirage = models.TextField(db_column='DirAge', blank=True) # Field name made lowercase.
    diryrofbirth = models.TextField(db_column='DirYrofBirth', blank=True) # Field name made lowercase.
    dirgender = models.TextField(db_column='DirGender', blank=True) # Field name made lowercase.
    dirmultiple = models.TextField(db_column='DirMultiple', blank=True) # Field name made lowercase.
    dirmultiple_newprivate = models.TextField(db_column='DirMultiple_NewPrivate', blank=True) # Field name made lowercase.
    dirmultiple_newpublic = models.TextField(db_column='DirMultiple_NewPublic', blank=True) # Field name made lowercase.
    acceleratedoptions = models.TextField(db_column='AcceleratedOptions', blank=True) # Field name made lowercase.
    totalindcompensation = models.TextField(db_column='TotalIndCompensation', blank=True) # Field name made lowercase.
    cfosince = models.TextField(db_column='CFOSince', blank=True) # Field name made lowercase.
    cfountil = models.TextField(db_column='CFOUntil', blank=True) # Field name made lowercase.
    dirreelectionyear = models.TextField(db_column='DirReelectionYear', blank=True) # Field name made lowercase.
    dirreasonended = models.TextField(db_column='DirReasonEnded', blank=True) # Field name made lowercase.
    dirprofile = models.TextField(db_column='DirProfile', blank=True) # Field name made lowercase.
    year = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'wrds_directorship_2009'

class WrdsDirectorship2010(models.Model):
    ticker = models.TextField(db_column='Ticker', blank=True) # Field name made lowercase.
    companyname = models.TextField(db_column='CompanyName', blank=True) # Field name made lowercase.
    indexsp = models.TextField(db_column='IndexSP', blank=True) # Field name made lowercase.
    indexrussell = models.TextField(db_column='IndexRussell', blank=True) # Field name made lowercase.
    indexfortune = models.TextField(db_column='IndexFortune', blank=True) # Field name made lowercase.
    industry = models.TextField(db_column='Industry', blank=True) # Field name made lowercase.
    proxydate = models.TextField(db_column='ProxyDate', blank=True) # Field name made lowercase.
    iddir = models.TextField(db_column='IDDir', blank=True) # Field name made lowercase.
    prefix = models.TextField(db_column='Prefix', blank=True) # Field name made lowercase.
    dirfname = models.TextField(db_column='DirFName', blank=True) # Field name made lowercase.
    dirlname = models.TextField(db_column='DirLName', blank=True) # Field name made lowercase.
    suffix = models.TextField(db_column='Suffix', blank=True) # Field name made lowercase.
    dirsince = models.TextField(db_column='DirSince', blank=True) # Field name made lowercase.
    dirtenure = models.TextField(db_column='DirTenure', blank=True) # Field name made lowercase.
    dateretiring = models.TextField(db_column='DateRetiring', blank=True) # Field name made lowercase.
    dirattendance = models.TextField(db_column='DirAttendance', blank=True) # Field name made lowercase.
    diroutside = models.TextField(db_column='DirOutside', blank=True) # Field name made lowercase.
    dirsharesexerciseableoptions = models.TextField(db_column='DirSharesExerciseableOptions', blank=True) # Field name made lowercase.
    dirsharesheld = models.TextField(db_column='DirSharesHeld', blank=True) # Field name made lowercase.
    dirsharesreported = models.TextField(db_column='DirSharesReported', blank=True) # Field name made lowercase.
    dirsharesvalue = models.TextField(db_column='DirSharesValue', blank=True) # Field name made lowercase.
    dirsharesvotingpower = models.TextField(db_column='DirSharesVotingPower', blank=True) # Field name made lowercase.
    isfounder = models.TextField(db_column='IsFounder', blank=True) # Field name made lowercase.
    committeeauditfinancialexpert = models.TextField(db_column='CommitteeAuditFinancialExpert', blank=True) # Field name made lowercase.
    committeeaudit = models.TextField(db_column='CommitteeAudit', blank=True) # Field name made lowercase.
    committeeexecutive = models.TextField(db_column='CommitteeExecutive', blank=True) # Field name made lowercase.
    committeecompensation = models.TextField(db_column='CommitteeCompensation', blank=True) # Field name made lowercase.
    committeegovernance = models.TextField(db_column='CommitteeGovernance', blank=True) # Field name made lowercase.
    committeenominating = models.TextField(db_column='CommitteeNominating', blank=True) # Field name made lowercase.
    addexectitle = models.TextField(db_column='AddExecTitle', blank=True) # Field name made lowercase.
    address1 = models.TextField(db_column='Address1', blank=True) # Field name made lowercase.
    address2 = models.TextField(db_column='Address2', blank=True) # Field name made lowercase.
    address3 = models.TextField(db_column='Address3', blank=True) # Field name made lowercase.
    city = models.TextField(db_column='City', blank=True) # Field name made lowercase.
    state = models.TextField(db_column='State', blank=True) # Field name made lowercase.
    postalcode = models.TextField(db_column='Postalcode', blank=True) # Field name made lowercase.
    country = models.TextField(db_column='Country', blank=True) # Field name made lowercase.
    phone = models.TextField(db_column='Phone', blank=True) # Field name made lowercase.
    phonefax = models.TextField(db_column='Phonefax', blank=True) # Field name made lowercase.
    problemdirector = models.TextField(db_column='ProblemDirector', blank=True) # Field name made lowercase.
    problemdirectoryn = models.TextField(db_column='ProblemDirectorYN', blank=True) # Field name made lowercase.
    activeceo = models.TextField(db_column='ActiveCEO', blank=True) # Field name made lowercase.
    dirage = models.TextField(db_column='DirAge', blank=True) # Field name made lowercase.
    diryrofbirth = models.TextField(db_column='DirYrofBirth', blank=True) # Field name made lowercase.
    dirgender = models.TextField(db_column='DirGender', blank=True) # Field name made lowercase.
    dirmultiple = models.TextField(db_column='DirMultiple', blank=True) # Field name made lowercase.
    dirmultiple_newpublic = models.TextField(db_column='DirMultiple_NewPublic', blank=True) # Field name made lowercase.
    acceleratedoptions = models.TextField(db_column='AcceleratedOptions', blank=True) # Field name made lowercase.
    totalindcompensation = models.TextField(db_column='TotalIndCompensation', blank=True) # Field name made lowercase.
    dirreelectionyear = models.TextField(db_column='DirReelectionYear', blank=True) # Field name made lowercase.
    dirretiredreason = models.TextField(db_column='DirRetiredReason', blank=True) # Field name made lowercase.
    dc_totalcompanycompensation = models.TextField(db_column='dc_TotalCompanyCompensation', blank=True) # Field name made lowercase.
    dirprofile1 = models.TextField(db_column='DirProfile1', blank=True) # Field name made lowercase.
    dirprofile2 = models.TextField(db_column='DirProfile2', blank=True) # Field name made lowercase.
    position = models.TextField(blank=True)
    position_status = models.TextField(blank=True)
    highest_executive_title = models.TextField(blank=True)
    position_date_began = models.TextField(blank=True)
    position_date_ended = models.TextField(blank=True)
    year = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'wrds_directorship_2010'

class WrdsDirectorship2011(models.Model):
    ticker = models.TextField(blank=True)
    companyname = models.TextField(db_column='CompanyName', blank=True) # Field name made lowercase.
    indexsp = models.TextField(db_column='IndexSP', blank=True) # Field name made lowercase.
    indexrussell = models.TextField(db_column='IndexRussell', blank=True) # Field name made lowercase.
    gics_industry = models.TextField(blank=True)
    proxydate = models.TextField(db_column='ProxyDate', blank=True) # Field name made lowercase.
    id_individual = models.TextField(blank=True)
    prefix = models.TextField(blank=True)
    dirfname = models.TextField(db_column='DirFName', blank=True) # Field name made lowercase.
    dirlname = models.TextField(db_column='DirLName', blank=True) # Field name made lowercase.
    suffix = models.TextField(db_column='Suffix', blank=True) # Field name made lowercase.
    datebegan = models.TextField(db_column='DateBegan', blank=True) # Field name made lowercase.
    tenure = models.TextField(db_column='Tenure', blank=True) # Field name made lowercase.
    dateretiring = models.TextField(db_column='DateRetiring', blank=True) # Field name made lowercase.
    dirattendance = models.TextField(db_column='DirAttendance', blank=True) # Field name made lowercase.
    diroutside = models.TextField(db_column='DirOutside', blank=True) # Field name made lowercase.
    dirsharesexerciseableoptions = models.TextField(db_column='DirSharesExerciseableOptions', blank=True) # Field name made lowercase.
    dirsharesheld = models.TextField(db_column='DirSharesHeld', blank=True) # Field name made lowercase.
    dirsharesreported = models.TextField(db_column='DirSharesReported', blank=True) # Field name made lowercase.
    dirsharesvalue = models.TextField(db_column='DirSharesValue', blank=True) # Field name made lowercase.
    dirsharesvotingpower = models.TextField(db_column='DirSharesVotingPower', blank=True) # Field name made lowercase.
    isfounder = models.TextField(db_column='IsFounder', blank=True) # Field name made lowercase.
    committeeauditfinancialexpert = models.TextField(db_column='CommitteeAuditFinancialExpert', blank=True) # Field name made lowercase.
    committeeaudit = models.TextField(db_column='CommitteeAudit', blank=True) # Field name made lowercase.
    committeeexecutive = models.TextField(db_column='CommitteeExecutive', blank=True) # Field name made lowercase.
    committeegovernance = models.TextField(db_column='CommitteeGovernance', blank=True) # Field name made lowercase.
    committeenominating = models.TextField(db_column='CommitteeNominating', blank=True) # Field name made lowercase.
    addexectitle = models.TextField(db_column='AddExecTitle', blank=True) # Field name made lowercase.
    address1 = models.TextField(db_column='Address1', blank=True) # Field name made lowercase.
    address2 = models.TextField(db_column='Address2', blank=True) # Field name made lowercase.
    address3 = models.TextField(db_column='Address3', blank=True) # Field name made lowercase.
    city = models.TextField(db_column='City', blank=True) # Field name made lowercase.
    state = models.TextField(db_column='State', blank=True) # Field name made lowercase.
    postalcode = models.TextField(db_column='PostalCode', blank=True) # Field name made lowercase.
    country = models.TextField(db_column='Country', blank=True) # Field name made lowercase.
    phone = models.TextField(db_column='Phone', blank=True) # Field name made lowercase.
    phone_fax = models.TextField(db_column='Phone_Fax', blank=True) # Field name made lowercase.
    problemdirector = models.TextField(db_column='ProblemDirector', blank=True) # Field name made lowercase.
    problemdirectoryn = models.TextField(db_column='ProblemDirectorYN', blank=True) # Field name made lowercase.
    activeceo = models.TextField(db_column='ActiveCEO', blank=True) # Field name made lowercase.
    dirage = models.TextField(db_column='DirAge', blank=True) # Field name made lowercase.
    diryrofbirth = models.TextField(db_column='DirYrofBirth', blank=True) # Field name made lowercase.
    dirgender = models.TextField(db_column='DirGender', blank=True) # Field name made lowercase.
    dirmultiple = models.TextField(db_column='DirMultiple', blank=True) # Field name made lowercase.
    dirmultiple_newpublic = models.TextField(db_column='DirMultiple_NewPublic', blank=True) # Field name made lowercase.
    acceleratedoptions = models.TextField(db_column='AcceleratedOptions', blank=True) # Field name made lowercase.
    totalindcompensation = models.TextField(db_column='TotalIndCompensation', blank=True) # Field name made lowercase.
    dirprofile = models.TextField(db_column='DirProfile', blank=True) # Field name made lowercase.
    position = models.TextField(blank=True)
    relstatus = models.TextField(db_column='RelStatus', blank=True) # Field name made lowercase.
    year = models.TextField(db_column='YEAR', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'wrds_directorship_2011'

class WrdsDirectorship2012(models.Model):
    ticker = models.TextField(db_column='Ticker', blank=True) # Field name made lowercase.
    companyname = models.TextField(db_column='CompanyName', blank=True) # Field name made lowercase.
    indexsp = models.TextField(db_column='IndexSP', blank=True) # Field name made lowercase.
    indexrussell = models.TextField(db_column='IndexRussell', blank=True) # Field name made lowercase.
    gics_industry = models.TextField(blank=True)
    proxydate = models.TextField(db_column='ProxyDate', blank=True) # Field name made lowercase.
    id_individual = models.TextField(blank=True)
    prefix = models.TextField(db_column='Prefix', blank=True) # Field name made lowercase.
    dirfname = models.TextField(db_column='DirFName', blank=True) # Field name made lowercase.
    dirlname = models.TextField(db_column='DirLName', blank=True) # Field name made lowercase.
    suffix = models.TextField(db_column='Suffix', blank=True) # Field name made lowercase.
    datebegan = models.TextField(db_column='DateBegan', blank=True) # Field name made lowercase.
    tenure = models.TextField(db_column='Tenure', blank=True) # Field name made lowercase.
    dateretiring = models.TextField(db_column='DateRetiring', blank=True) # Field name made lowercase.
    dirattendance = models.TextField(db_column='DirAttendance', blank=True) # Field name made lowercase.
    diroutside = models.TextField(db_column='DirOutside', blank=True) # Field name made lowercase.
    dirsharesexerciseableoptions = models.TextField(db_column='DirSharesExerciseableOptions', blank=True) # Field name made lowercase.
    dirsharesheld = models.TextField(db_column='DirSharesHeld', blank=True) # Field name made lowercase.
    dirsharesreported = models.TextField(db_column='DirSharesReported', blank=True) # Field name made lowercase.
    dirsharesvalue = models.TextField(db_column='DirSharesValue', blank=True) # Field name made lowercase.
    dirsharesvotingpower = models.TextField(db_column='DirSharesVotingPower', blank=True) # Field name made lowercase.
    isfounder = models.TextField(db_column='IsFounder', blank=True) # Field name made lowercase.
    committeeauditfinancialexpert = models.TextField(db_column='CommitteeAuditFinancialExpert', blank=True) # Field name made lowercase.
    committeeaudit = models.TextField(db_column='CommitteeAudit', blank=True) # Field name made lowercase.
    committeeexecutive = models.TextField(db_column='CommitteeExecutive', blank=True) # Field name made lowercase.
    committeegovernance = models.TextField(db_column='CommitteeGovernance', blank=True) # Field name made lowercase.
    committeenominating = models.TextField(db_column='CommitteeNominating', blank=True) # Field name made lowercase.
    addexectitle = models.TextField(db_column='AddExecTitle', blank=True) # Field name made lowercase.
    address1 = models.TextField(db_column='Address1', blank=True) # Field name made lowercase.
    address2 = models.TextField(db_column='Address2', blank=True) # Field name made lowercase.
    address3 = models.TextField(db_column='Address3', blank=True) # Field name made lowercase.
    city = models.TextField(db_column='City', blank=True) # Field name made lowercase.
    state = models.TextField(db_column='State', blank=True) # Field name made lowercase.
    postalcode = models.TextField(db_column='PostalCode', blank=True) # Field name made lowercase.
    country = models.TextField(db_column='Country', blank=True) # Field name made lowercase.
    phone = models.TextField(db_column='Phone', blank=True) # Field name made lowercase.
    phone_fax = models.TextField(db_column='Phone_Fax', blank=True) # Field name made lowercase.
    problemdirector = models.TextField(db_column='ProblemDirector', blank=True) # Field name made lowercase.
    problemdirectoryn = models.TextField(db_column='ProblemDirectorYN', blank=True) # Field name made lowercase.
    activeceo = models.TextField(db_column='ActiveCEO', blank=True) # Field name made lowercase.
    dirage = models.TextField(db_column='DirAge', blank=True) # Field name made lowercase.
    diryrofbirth = models.TextField(db_column='DirYrofBirth', blank=True) # Field name made lowercase.
    dirgender = models.TextField(db_column='DirGender', blank=True) # Field name made lowercase.
    dirmultiple = models.TextField(db_column='DirMultiple', blank=True) # Field name made lowercase.
    dirmultiple_newpublic = models.TextField(db_column='DirMultiple_NewPublic', blank=True) # Field name made lowercase.
    acceleratedoptions = models.TextField(db_column='AcceleratedOptions', blank=True) # Field name made lowercase.
    totalindcompensation = models.TextField(db_column='TotalIndCompensation', blank=True) # Field name made lowercase.
    dirprofile = models.TextField(db_column='DirProfile', blank=True) # Field name made lowercase.
    position = models.TextField(blank=True)
    relstatus = models.TextField(db_column='RelStatus', blank=True) # Field name made lowercase.
    year = models.TextField(db_column='YEAR', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'wrds_directorship_2012'

class YahooIpos(models.Model):
    company = models.TextField(blank=True)
    symbol = models.TextField(blank=True)
    shares = models.TextField(blank=True)
    price = models.TextField(blank=True)
    file_date = models.TextField(blank=True)
    ipo_date = models.TextField(blank=True)
    status = models.TextField(blank=True)
    info = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'yahoo_ipos'

