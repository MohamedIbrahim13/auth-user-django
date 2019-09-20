from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
from django_countries.fields import CountryField
from django.contrib.auth import get_user_model

class User(AbstractUser):
    types = models.BooleanField(verbose_name='Sign up as', choices=[(True, 'Worker'), (False, 'Employer')])
    sex = models.BooleanField(verbose_name='Gender', choices=[(True, 'Male'), (False, 'Female')])
    location=CountryField()
    image=models.ImageField(default='default.jpg', upload_to='Profile_Pics')
    bio=models.TextField(default='',blank=True,max_length=500)

    def save(self, force_insert=False, force_update=False, using=None,update_fields=None):
        super().save()
        img=Image.open(self.image.path)
        if img.height > 175 or img.width > 175:
            output_size=(175,175)
            img.thumbnail(output_size)
            img.save(self.image.path)

