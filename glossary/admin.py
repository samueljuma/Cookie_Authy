from django.contrib import admin
from glossary.models import GlossaryTerm

@admin.register(GlossaryTerm)
class GlossaryTermAdmin(admin.ModelAdmin):
    list_display = ('term', 'category')
    search_fields = ('term', 'category')
    list_filter = ('category',)
