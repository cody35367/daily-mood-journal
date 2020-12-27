from django.contrib import admin
from django.forms import CheckboxSelectMultiple
from django.db import models

from .models import Journal,Emotion,Thought,Distortion

class EmotionInline(admin.TabularInline):
    model = Emotion
    extra = 0

class ThoughtInline(admin.TabularInline):
    model = Thought
    fields = ['negative_thoughts','now_percent','after_percent','distortions','positive_thoughts','belief_percent']
    extra = 0
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

class DistortionAdmin(admin.ModelAdmin):
    list_display = ['name','description']
    
class JournalAdmin(admin.ModelAdmin):
    inlines = [EmotionInline,ThoughtInline]
    list_display = ['upsetting_event','create_date','update_date']

admin.site.register(Journal,JournalAdmin)
admin.site.register(Distortion,DistortionAdmin)