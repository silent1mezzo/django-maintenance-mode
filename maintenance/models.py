from datetime import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _
import settings

class MaintenancePeriod(models.Model):
    name = models.CharField(_('Maintenance Name'), max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    notificiation_period = models.IntegerField(_('Notification Period'), help_text='Notification period before maintenance (in minutes)')
    notify_users = models.BooleanField(default=settings.EMAIL_USERS)
    template = models.CharField(_('Display Template'), max_length=255, blank=True, null=True)

    def __unicode__(self):
        return self.name
