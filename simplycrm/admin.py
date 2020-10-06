from django.contrib import admin

from simplycrm.models import Staff, JobDesk

class JobDeskInline(admin.TabularInline):
    model = JobDesk

class StaffAdmin(admin.ModelAdmin):
    list_display = ('name','staff_status')
    list_filter = ('name',)
    inlines = [
        JobDeskInline
    ]

class JobdeskAdmin(admin.ModelAdmin):
    list_display = ('jobs','member_id','member_name','board', "delegation")

admin.site.register(Staff, StaffAdmin)
admin.site.register(JobDesk, JobdeskAdmin)