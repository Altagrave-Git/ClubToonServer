from django.dispatch import receiver
from users.models import User
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
 
 
# create(user) => create(jwt)
@receiver(post_save, sender=User)
def create_token(sender, instance, created, **kwargs):
    if created:
        token = Token.objects.create(user=instance)
        token.save()