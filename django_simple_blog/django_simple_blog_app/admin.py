from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Entry


class EntryAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'


admin.site.register(Entry, EntryAdmin)
