from django.contrib import admin

from .models import AssessmentResult, ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email', 'message')
    list_filter = ('created_at',)
    ordering = ('-created_at',)


@admin.register(AssessmentResult)
class AssessmentResultAdmin(admin.ModelAdmin):
    list_display = ('overall_score', 'weakest_pillar', 'created_at')
    list_filter = ('weakest_pillar', 'created_at')
    ordering = ('-created_at',)
