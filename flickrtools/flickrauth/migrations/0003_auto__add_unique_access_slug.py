# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'Access', fields ['slug']
        db.create_unique('flickrauth_access', ['slug'])


    def backwards(self, orm):
        # Removing unique constraint on 'Access', fields ['slug']
        db.delete_unique('flickrauth_access', ['slug'])


    models = {
        'flickrauth.access': {
            'Meta': {'object_name': 'Access'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'secret': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['flickrauth']