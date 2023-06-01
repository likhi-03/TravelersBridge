from django.contrib import admin
from django.contrib import messages
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('msg_id','name', 'message', 'email', 'timestamp')
    list_filter = ['timestamp']
    readonly_fields = ('msg_id','name', 'email', 'message', 'timestamp')

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

admin.site.register(Contact, ContactAdmin)
