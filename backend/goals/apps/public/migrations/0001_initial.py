# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Goal'
        db.create_table(u'public_goal', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(default='No description has been entered yet')),
            ('timeFrame', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['public.TimeFrame'])),
            ('status', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('dueDate', self.gf('django.db.models.fields.DateField')(default=False)),
        ))
        db.send_create_signal(u'public', ['Goal'])

        # Adding model 'TimeFrame'
        db.create_table(u'public_timeframe', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('days', self.gf('django.db.models.fields.IntegerField')(default=False)),
        ))
        db.send_create_signal(u'public', ['TimeFrame'])

        # Adding model 'ChildGoal'
        db.create_table(u'public_childgoal', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('step', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('status', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('goal', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['public.Goal'])),
        ))
        db.send_create_signal(u'public', ['ChildGoal'])

        # Adding model 'Journal'
        db.create_table(u'public_journal', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('entry', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'public', ['Journal'])


    def backwards(self, orm):
        # Deleting model 'Goal'
        db.delete_table(u'public_goal')

        # Deleting model 'TimeFrame'
        db.delete_table(u'public_timeframe')

        # Deleting model 'ChildGoal'
        db.delete_table(u'public_childgoal')

        # Deleting model 'Journal'
        db.delete_table(u'public_journal')


    models = {
        u'public.childgoal': {
            'Meta': {'object_name': 'ChildGoal'},
            'goal': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['public.Goal']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'step': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'public.goal': {
            'Meta': {'object_name': 'Goal'},
            'description': ('django.db.models.fields.TextField', [], {'default': "'No description has been entered yet'"}),
            'dueDate': ('django.db.models.fields.DateField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'timeFrame': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['public.TimeFrame']"})
        },
        u'public.journal': {
            'Meta': {'object_name': 'Journal'},
            'entry': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'public.timeframe': {
            'Meta': {'object_name': 'TimeFrame'},
            'days': ('django.db.models.fields.IntegerField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['public']