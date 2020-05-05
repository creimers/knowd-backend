from django.contrib import admin

from apps.knowd.models import Note


class NoteAdmin(admin.ModelAdmin):
    list_display = ["owner", "created"]


admin.site.register(Note, NoteAdmin)
