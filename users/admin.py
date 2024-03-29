from django.contrib import admin
from django.contrib.auth import get_user_model
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin


CustomUser = get_user_model()

class CustomAdmin(UserAdmin):
  add_form = CustomUserCreationForm
  form = CustomUserChangeForm
  model = CustomUser
  list_display = ['email', 'username']


admin.site.register(CustomUser, CustomAdmin)