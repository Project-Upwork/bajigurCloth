from django.contrib import admin
from .models import Account, Wish

class WishInline(admin.TabularInline):
    model=Wish

class AccountAdmin(admin.ModelAdmin):
    list_display = ("member_id","username","email","telephone")
    inlines = [
        WishInline
    ]

class WishAdmin(admin.ModelAdmin):
    list_display = ("account","title","image","pricing","date","note","order_date")

admin.site.register(Wish, WishAdmin)
admin.site.register(Account, AccountAdmin)