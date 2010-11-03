# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'MaintenancePeriod.template'
        db.alter_column('maintenance_maintenanceperiod', 'template', self.gf('django.db.models.fields.CharField')(max_length=254))


    def backwards(self, orm):
        
        # Changing field 'MaintenancePeriod.template'
        db.alter_column('maintenance_maintenanceperiod', 'template', self.gf('django.db.models.fields.CharField')(max_length=255))


    models = {
        'maintenance.maintenanceperiod': {
            'Meta': {'object_name': 'MaintenancePeriod'},
            'end_date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'notificiation_period': ('django.db.models.fields.IntegerField', [], {}),
            'notify_users': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {}),
            'template': ('django.db.models.fields.CharField', [], {'max_length': '254'})
        }
    }

    complete_apps = ['maintenance']
