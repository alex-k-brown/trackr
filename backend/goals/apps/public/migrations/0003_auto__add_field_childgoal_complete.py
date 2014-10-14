# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ChildGoal.complete'
        db.add_column(u'public_childgoal', 'complete',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ChildGoal.complete'
        db.delete_column(u'public_childgoal', 'complete')


    models = {
        u'public.childgoal': {
            'Meta': {'object_name': 'ChildGoal'},
            'complete': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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