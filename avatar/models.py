from django.db import models
from users.models import User


class AvatarComponent(models.Model):
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=1)
    colors = models.CharField(max_length=100, null=True, blank=True)


class Skin(AvatarComponent): pass

class Hair(AvatarComponent): pass

class Eyes(AvatarComponent): pass

class Mouth(AvatarComponent): pass

class Torso(AvatarComponent): pass

class Hands(AvatarComponent): pass

class Legs(AvatarComponent): pass

class Feet(AvatarComponent): pass


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='avatar')

    skin = models.ForeignKey(Skin, on_delete=models.SET_NULL, null=True, blank=True)
    hair = models.ForeignKey(Hair, on_delete=models.SET_NULL, null=True, blank=True)
    eyes = models.ForeignKey(Eyes, on_delete=models.SET_NULL, null=True, blank=True)
    mouth = models.ForeignKey(Mouth, on_delete=models.SET_NULL, null=True, blank=True)
    torso = models.ForeignKey(Torso, on_delete=models.SET_NULL, null=True, blank=True)
    hands = models.ForeignKey(Hands, on_delete=models.SET_NULL, null=True, blank=True)
    legs = models.ForeignKey(Legs, on_delete=models.SET_NULL, null=True, blank=True)
    feet = models.ForeignKey(Feet, on_delete=models.SET_NULL, null=True, blank=True)


class Owned(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned')

    skin = models.ManyToManyField(Skin, blank=True)
    hair = models.ManyToManyField(Hair, blank=True)
    eyes = models.ManyToManyField(Eyes, blank=True)
    mouth = models.ManyToManyField(Mouth, blank=True)
    torso = models.ManyToManyField(Torso, blank=True)
    hands = models.ManyToManyField(Hands, blank=True)
    legs = models.ManyToManyField(Legs, blank=True)
    feet = models.ManyToManyField(Feet, blank=True)

    def delete(self, *args, **kwargs):
        self.skin.all().delete()
        self.hair.all().delete()
        self.eyes.all().delete()
        self.mouth.all().delete()
        self.torso.all().delete()
        self.hands.all().delete()
        self.legs.all().delete()
        self.feet.all().delete()

        return super().delete(*args, **kwargs)