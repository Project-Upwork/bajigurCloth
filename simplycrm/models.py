from django.db import models
from django.conf import settings

class Staff(models.Model):
    PERMISSION = [
        ('Admin', "admin"),
        ('Tim', "tim")
    ]
    staff_id = models.AutoField(primary_key=True)
    name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="staff_office")
    staff_status = models.CharField(max_length=10, choices=PERMISSION)

    class Meta:
        verbose_name ="Staff"
        verbose_name_plural ="Staff"
    
    def __unicode__(self):
        return unicode(self.staff_id)

    def __str__(self):
        return "{}".format(self.name)

class JobDesk(models.Model):
    JOBS =[
        ("Wishlist","Wishlist"),
        ("Email_marketing", "Emailing")
    ]
    PROGRESS = [
        ("Todo","To Do"),
        ("On_Progress","On Progress"),
        ("Report","Report"),
        ("Done", "Done")
    ]
    jobs = models.CharField(max_length=25, choices=JOBS)
    member_id = models.CharField(max_length=100)
    member_name = models.CharField(max_length=30)
    board = models.CharField(max_length=25, choices=PROGRESS, blank=True)
    delegation = models.ForeignKey('Staff', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name ="Jobdesk"
        verbose_name_plural ="Jobsdesk"
    
    def __str__(self):
        return self.jobs