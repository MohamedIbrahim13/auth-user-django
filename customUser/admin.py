from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .forms import UserCreationForm,UserChangeForm

class UserAdmin(UserAdmin):
    add_form=UserCreationForm
    form=UserChangeForm
    model=User
    list_display=['username','email','types']


admin.site.register(User,UserAdmin)
