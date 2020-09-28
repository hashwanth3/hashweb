from django.contrib import admin
from django.utils import timezone

from . import models

def mark_complete(model_admin, request, queryset):
    queryset.update( status = models.TweetStatus.COMPLETED, completed_at=timezone.now(),)

def mark_pending(model_admin, request, quesryset):
    quesryset.update( status = models.TweetStatus.PENDING, completed_at=None,)

mark_pending.short_description = 'Mark these as pending'
# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    fields = ['content','tags','tweeted_by']
    list_display = ['content','created_at','get_all_tags','tweeted_by']
    #list_editable = ['status']
    #actions = [mark_complete,mark_pending]
    #list_filter = ['status']
    search_fields = ['content','tags__name']

    def get_ordering(self, request):
        if request.user.is_superuser:
            return['status']
        else:
            return['content']



admin.site.register(models.Tweet, TaskAdmin)
admin.site.register(models.Tag)
