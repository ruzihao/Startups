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

class SiAcquisitions04Oct2014(models.Model):
    status = models.TextField(blank=True)
    since = models.TextField(blank=True)
    name = models.TextField(blank=True)
    cid = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'si_acquisitions_04oct2014'

class SiCareers(models.Model):
    date = models.TextField(blank=True)
    company = models.TextField(blank=True)
    cid = models.IntegerField(blank=True, null=True)
    title = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'si_careers'

class SiColleagues(models.Model):
    date = models.TextField(blank=True)
    executive = models.TextField(blank=True)
    cid = models.IntegerField(blank=True, null=True)
    name = models.TextField(blank=True)
    title = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'si_colleagues'

class SiCompanies04Oct2014(models.Model):
    cid = models.IntegerField(blank=True, null=True)
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
    class Meta:
        managed = False
        db_table = 'si_companies_04oct2014'

class SiEducation(models.Model):
    school = models.TextField(blank=True)
    cid = models.IntegerField(blank=True, null=True)
    major = models.TextField(blank=True)
    year = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'si_education'

class SiFundings04Oct2014(models.Model):
    investors = models.TextField(blank=True)
    cid = models.IntegerField(blank=True, null=True)
    series = models.TextField(blank=True)
    amount = models.TextField(blank=True)
    date = models.TextField(blank=True)
    partners_count = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'si_fundings_04oct2014'

class SiMembers04Oct2014(models.Model):
    category = models.TextField(blank=True)
    since = models.TextField(blank=True)
    cid = models.IntegerField(blank=True, null=True)
    name = models.TextField(blank=True)
    title = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'si_members_04oct2014'

class SiPeople(models.Model):
    website = models.TextField(blank=True)
    name = models.TextField(blank=True)
    title = models.TextField(blank=True)
    company = models.TextField(blank=True)
    cid = models.IntegerField(blank=True, null=True)
    summary = models.TextField(blank=True)
    blog = models.TextField(blank=True)
    location = models.TextField(blank=True)
    profile_completion = models.TextField(blank=True)
    industry = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'si_people'

class SiPeople16Oct2014(models.Model):
    website = models.TextField(blank=True)
    name = models.TextField(blank=True)
    title = models.TextField(blank=True)
    company = models.TextField(blank=True)
    cid = models.IntegerField(blank=True, null=True)
    summary = models.TextField(blank=True)
    blog = models.TextField(blank=True)
    location = models.TextField(blank=True)
    profile_completion = models.TextField(blank=True)
    industry = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'si_people_16oct2014'