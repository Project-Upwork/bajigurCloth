from django.db.models.signals import post_save
from django.dispatch import receiver
from createwish.models import Account, Wish
from simplycrm.models import JobDesk

@receiver(post_save, sender=Wish)
def update_jobdesk(sender, instance, created, **kwargs):
    '''
     Create query to Jobdesk model
    '''
    if created:
        jobs= "Wishlist"
        mid= Account.objects.filter(pk=int(instance.account.account_id))
        mname= Account.objects.filter(pk=int(instance.account.account_id))
        task =JobDesk(jobs=jobs, member_id=mid.get().member_id, member_name=mname.get().username.username, board="On_Progress")
        task.save()
