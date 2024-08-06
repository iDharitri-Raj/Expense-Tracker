from django.contrib import admin
from .models import *

# Register your models here.

admin.site.site_header = "Expense Tracker"
admin.site.site_title = "Expense Tracker"
admin.site.site_url = "Expense Tracker"


admin.site.register(CurrentBalance)


class TrackingHistoryAdmin(admin.ModelAdmin):
    list_display = [
        "amount",
        "current_balance",
        "expense_type",
        "description",
        "created_at",
    ]

    search_fields = ['expense_type']
    list_filter = ['expense_type']
    ordering = ['-created_at']

admin.site.register(TrackingHistory, TrackingHistoryAdmin)
