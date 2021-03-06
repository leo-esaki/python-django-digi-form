from __future__ import unicode_literals
from django.db import models
from django.contrib.postgres.fields import (
    ArrayField,
    JSONField,
)
from core.models import (
    TimeStampedModel,
    PublishableModel,
)
from django.utils.translation import ugettext_lazy as _


class DataSourceModel(TimeStampedModel, PublishableModel, models.Model):
    source_name = models.CharField(max_length=64)
    columns = ArrayField(
        models.CharField(max_length=32, blank=True)
    )
    model_name = models.CharField(max_length=64)



class AFSLicenseeEntry(TimeStampedModel, models.Model):
    name = models.CharField(max_length=256)
    license_no = models.IntegerField()
    abn = models.BigIntegerField(null=True)
    acn = models.BigIntegerField(null=True)
    commenced_date = models.DateField(null=True)
    service_address = models.CharField(max_length=512, null=True)
    status = models.CharField(max_length=32, null=True)
    principle_business_address = models.CharField(max_length=512, null=True)

    def __unicode__(self):
        return '{0} <{1}>'.format(self.name, self.license_no)

    class Meta(object):
        verbose_name = _('Australian Financial Services Licensee')
        verbose_name_plural = _('Australian Financial Services Licensee')


class AFSAuthorisedRepresentative(TimeStampedModel, models.Model):
    name = models.CharField(max_length=256)
    license_no = models.IntegerField()
    licensed_by = models.ForeignKey(AFSLicenseeEntry, null=True)

    def __unicode__(self):
        return '{0} <{1}>'.format(self.name, self.license_no)

    class Meta(object):
        verbose_name = _('Australian Financial Services Authorised Representative')
        verbose_name_plural = _('Australian Financial Services Authorised Representatives')


class JusticeOfPeace(TimeStampedModel, models.Model):
    jp_number = models.CharField(max_length=32, blank=True, default='')
    first_name = models.CharField(_('first name'), max_length=30, blank=True, default='')
    last_name = models.CharField(_('last name'), max_length=30, blank=True, default='')
    email = models.EmailField(_('email address'), blank=True, default='')
    mobile_number = models.CharField(_('Mobile Number'), max_length=128, blank=True, default='')
    phone = models.CharField(_('Contact Number'), max_length=128, blank=True, default='')
    phone2 = models.CharField(_('Contact Number2'), max_length=128, blank=True, help_text='After hour', default='')
    state = models.CharField(_('State'), blank=True, max_length=128, default='')
    suburb = models.CharField(_('Suburb'), blank=True, max_length=32, default='')
    raw = JSONField()

    def __unicode__(self):
        return '{0} <{1}>'.format(self.first_name, self.jp_number)

    class Meta(object):
        verbose_name = _('Justice Of Peace')
        verbose_name_plural = _('Justice Of Peace')
