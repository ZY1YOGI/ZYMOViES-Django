from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.text import slugify
# Create your models here.

class Profile(models.Model):
    user   = models.OneToOneField(User, on_delete=models.CASCADE)
    image  = models.ImageField(default='default.png', upload_to='profile/')
    slug   = models.SlugField()


    def save(self, *args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.user)

        super(Profile, self).save(*args, **kwargs)


    def __str__(self):
        return str(self.user)





def create_profile(sender,**kwargs):
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)