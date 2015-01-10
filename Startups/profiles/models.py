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
    name = models.TextField(blank=True)
    website = models.TextField(blank=True)
    founded_on = models.TextField(blank=True)
    contact_info_email = models.TextField(blank=True)
    contact_info_tel = models.TextField(blank=True)
    postal_code = models.TextField(blank=True)
    city = models.TextField(blank=True)
    people = models.TextField(blank=True)
    blog = models.TextField(blank=True)
    state = models.TextField(blank=True)
    location = models.TextField(blank=True)
    profile_completion = models.TextField(blank=True)
    short_description = models.TextField(blank=True)
    status = models.TextField(blank=True)
    branch = models.TextField(blank=True)
    tags = models.TextField(blank=True)
    yearly_revenue = models.TextField(blank=True)
    country = models.TextField(blank=True)
    industry = models.TextField(blank=True)
    summary = models.TextField(blank=True)
    alias = models.TextField(blank=True)
    address_line = models.TextField(blank=True)

    def __str__(self):
        return "No. %d: %s" % (self.cid, self.name)

    class Meta:
        managed = False
        db_table = 'company'


class funding_ent(models.Model):
    fid = models.BigIntegerField(primary_key=True)
    investors = models.TextField(blank=True)
    cid = models.ForeignKey('company_ent', db_column='cid', blank=True, null=True)
    series = models.TextField(blank=True)
    date = models.TextField(blank=True)
    amount = models.IntegerField(blank=True)

    def __str__(self):
        return "%s invested %r in series %s of %s on %s" % (self.investors, self.amount, self.series, self.cid, self.date)

    class Meta:
        managed = False
        db_table = 'funding'
		
class acquisition_ent(models.Model):
    aid = models.FloatField(primary_key=True)
    status = models.TextField(blank=True)
    since = models.TextField(blank=True)
    name = models.TextField(blank=True)
    cid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acquisitions'
		
class member_ent(models.Model):
    member_id = models.FloatField(primary_key=True)
    category = models.TextField(blank=True)
    since = models.TextField(blank=True)
    cid = models.IntegerField(blank=True, null=True)
    name = models.TextField(blank=True)
    title = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'member'
		
class people_ent(models.Model):
    website = models.TextField(blank=True)
    name = models.TextField(blank=True)
    title = models.TextField(blank=True)
    company = models.TextField(blank=True)
    pid = models.IntegerField(primary_key=True)
    summary = models.TextField(blank=True)
    blog = models.TextField(blank=True)
    location = models.TextField(blank=True)
    profile_completion = models.TextField(blank=True)
    industry = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'people'

class career_ent(models.Model):
    career_id = models.FloatField(primary_key=True)
    date = models.TextField(blank=True)
    company = models.TextField(blank=True)
    pid = models.ForeignKey('people_ent', db_column='pid', blank=True, null=True)
    title = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'career'		
		
class colleague_ent(models.Model):
    colleague_id = models.FloatField(primary_key=True)
    date = models.TextField(blank=True)
    executive = models.TextField(blank=True)
    pid = models.ForeignKey('people_ent', db_column='pid', blank=True, null=True)
    name = models.TextField(blank=True)
    title = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'colleague'

		
class education_ent(models.Model):
    edu_id = models.FloatField(primary_key=True)
    school = models.TextField(blank=True)
    pid = models.ForeignKey('people_ent', db_column='pid', blank=True, null=True)
    major = models.TextField(blank=True)
    year = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'education'