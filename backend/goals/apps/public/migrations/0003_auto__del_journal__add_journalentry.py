# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Journal'
        db.delete_table(u'public_journal')

        # Adding model 'JournalEntry'
        db.create_table(u'public_journalentry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('topic', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('entry', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'public', ['JournalEntry'])


    def backwards(self, orm):
        # Adding model 'Journal'
        db.create_table(u'public_journal', (
            ('entry', self.gf('django.db.models.fields.TextField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'public', ['Journal'])

        # Deleting model 'JournalEntry'
        db.delete_table(u'public_journalentry')


    models = {
        u'public.childgoal': {
            'Meta': {'object_name': 'ChildGoal'},
            'goal': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'children'", 'to': u"orm['public.Goal']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'step': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'timeFrame': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['public.TimeFrame']"})
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
        u'public.journalentry': {
            'Meta': {'object_name': 'JournalEntry'},
            'entry': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'topic': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'public.timeframe': {
            'Meta': {'object_name': 'TimeFrame'},
            'days': ('django.db.models.fields.IntegerField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['public']