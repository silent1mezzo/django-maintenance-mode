from datetime import datetime, timedelta
from django import template
from django.template import RequestContext
from django.db import settings
from django.utils.translation import ugettext as _
from django.utils.safestring import mark_safe
from maintenance.models import MaintenancePeriod
register = template.Library()


@register.simple_tag
def get_maintenance_message():
    """
        Displays any maintenance messages that are approaching
    """
    
    now = datetime.now()
    msg = u''
    maintenance = MaintenancePeriod.objects.all()
    for maint in maintenance:
        notification = timedelta(minutes=maint.notificiation_period)
        notify = now + notification
        if maint.start_date < notify and maint.start_date > now:
            countdown = maint.start_date - now 
            countdown = (countdown.seconds % 3600) // 60
            msg += u"<div class='maintenance_msg'>There's an upcomming maintenance mode in %s minutes. Please save all of your current work.</div>" % countdown
    return mark_safe(msg)
