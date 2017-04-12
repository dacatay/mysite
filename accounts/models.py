from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist


class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=50, blank=False)
    balance = models.FloatField(default=500)

    def save(self, *args, **kwargs):
        if not self.pk:
            try:
                p = UserAccount.objects.get(user=self.user)
                self.pk = p.pk
            except UserAccount.DoesNotExist:
                pass

        super(UserAccount, self).save(*args, **kwargs)


@receiver(post_save, sender=User)
def create_user_account(sender, instance, created, **kwargs):
    if created:
        UserAccount.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_account(sender, instance, **kwargs):
    try:
        instance.account.save()
    except ObjectDoesNotExist:
        print('Account doesn''t exist.')
        #profile = Profile(user=User)
        instance.account.save()