from __future__ import unicode_literals

import uuid

from django.db import models

# Create your models here.
from django_countries.fields import CountryField

from contacts.constants import GenderSource

GENDER_CHOICES = (
    (GenderSource.Male, 'M',),
    (GenderSource.Female, 'F',),
)

# Create your models here.
class Person(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=90, blank=True)
    last_name = models.CharField(max_length=90, blank=True)
    middle_name = models.CharField(max_length=90, blank=True)
    date_of_birth = models.DateField(null=True)
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, blank=True, null=True)
    mobile_number = models.CharField(max_length=32, blank=True)
    email = models.CharField(max_length=128, blank=True)
    is_email_verified = models.BooleanField(default=False)
    email_verification_code = models.CharField(blank=True, default='', max_length=16)


class Location(models.Model):
    person = models.ForeignKey(Person, null=True)
    raw = models.CharField(max_length=200, blank=True, help_text='address line 1')
    unit_no = models.CharField(max_length=6, blank=True)
    street_number = models.CharField(max_length=32, blank=True)
    street_name = models.CharField(max_length=128, blank=True)
    city = models.CharField(max_length=64, blank=True)
    suburb = models.CharField(max_length=64, blank=True)
    state_province_code = models.CharField(max_length=32, blank=True)
    postal_code = models.CharField(max_length=32, blank=True)
    country = CountryField(blank=True)
