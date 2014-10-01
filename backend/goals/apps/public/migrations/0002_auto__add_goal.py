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
            ('categories', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('timeframe', self.gf('django.db.models.fields.DateField')()),
            ('status', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'public', ['Goal'])

        # Adding M2M table for field child_goals on 'Goal'
        m2m_table_name = db.shorten_name(u'public_goal_child_goals')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_goal', models.ForeignKey(orm[u'public.goal'], null=False)),
            ('to_goal', models.ForeignKey(orm[u'public.goal'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_goal_id', 'to_goal_id'])


    def backwards(self, orm):
        # Deleting model 'Goal'
        db.delete_table(u'public_goal')

        # Removing M2M table for field child_goals on 'Goal'
        db.delete_table(db.shorten_name(u'public_goal_child_goals'))


    models = {
        u'public.goal': {
            'Meta': {'object_name': 'Goal'},
            'categories': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'child_goals': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['public.Goal']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "'No description has been entered yet'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'timeframe': ('django.db.models.fields.DateField', [], {})
        }
    }

    complete_apps = ['public']