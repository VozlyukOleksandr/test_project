from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Profil(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    bir_day=models.DateField(null=True)
    country=models.CharField(max_length=10)
    city=models.CharField(max_length=15)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profil.objects.create(user=instance)
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profil.save()



class post(models.Model):
    name=models.CharField(max_length=1000, default='')
    file=models.FileField(default='')
    likes=models.IntegerField(default=0)
    user_name=models.CharField(max_length=20)


