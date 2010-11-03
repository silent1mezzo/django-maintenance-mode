# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'MaintenancePeriod'
        db.create_table('maintenance_maintenanceperiod', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('end_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('notificiation_period', self.gf('django.db.models.fields.IntegerField')()),
            ('template', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('notify_users', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('maintenance', ['MaintenancePeriod'])


    def backwards(self, orm):
        
        # Deleting model 'MaintenancePeriod'
        db.delete_table('maintenance_maintenanceperiod')


    models = {
        'maintenance.maintenanceperiod': {
            'Meta': {'object_name': 'MaintenancePeriod'},
            'end_date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'notificiation_period': ('django.db.models.fields.IntegerField', [], {}),
            'notify_users': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {}),
            'template': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['maintenance']
