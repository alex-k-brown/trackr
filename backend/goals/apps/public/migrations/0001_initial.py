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
            ('timeframe', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['public.TimeFrame'])),
            ('status', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('duedate', self.gf('django.db.models.fields.DateField')(default=False)),
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

        # Adding model 'TimeFrame'
        db.create_table(u'public_timeframe', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('days', self.gf('django.db.models.fields.IntegerField')(default=False)),
        ))
        db.send_create_signal(u'public', ['TimeFrame'])

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

        # Removing M2M table for field child_goals on 'Goal'
        db.delete_table(db.shorten_name(u'public_goal_child_goals'))

        # Deleting model 'TimeFrame'
        db.delete_table(u'public_timeframe')

        # Deleting model 'Journal'
        db.delete_table(u'public_journal')


    models = {
        u'public.goal': {
            'Meta': {'object_name': 'Goal'},
            'child_goals': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['public.Goal']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "'No description has been entered yet'"}),
            'duedate': ('django.db.models.fields.DateField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'timeframe': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['public.TimeFrame']"})
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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['public']