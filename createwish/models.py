from django.db import models
from django.conf import settings

class Account(models.Model):
    account_id = models.AutoField(primary_key=True)
    member_id = models.CharField(max_length=100)
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,null=True, related_name="member_account")
    email = models.CharField(max_length=100)
    telephone = models.CharField(max_length=15)

    class Meta:
        verbose_name = "Account"
        verbose_name_plural ="Account"

    def __str__(self):
        return "{}".format(self.username)

class Wish(models.Model):
    account = models.ForeignKey('Account', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=30)
    image = models.TextField(null=True, blank=True)
    pricing = models.DecimalField(max_digits=15, decimal_places=2)
    date  = models.DateTimeField(auto_now_add=True)
    note = models.TextField(null=True, blank=True)
    order_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Wishlist"
        verbose_name_plural ="Wishlist"

    def __str__(self):
        return self.title 