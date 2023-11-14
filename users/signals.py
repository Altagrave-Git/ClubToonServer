from django.dispatch import receiver
from users.models import User, Avatar
from django.db.models.signals import post_save
from knox.models import AuthToken
 
 
# create(user) => create(token)
@receiver(post_save, sender=User)
def create_token(sender, instance, created, **kwargs):
    if created:
        AuthToken.objects.create(user=instance)
        Avatar.objects.create(user=instance)