from django.forms import ModelForm
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model



class CustomUserChangeForm(UserChangeForm):

    class Meta:
      model = get_user_model()
      fields = ("username", "email",)

class CustomUserCreationForm(UserCreationForm):
      model = get_user_model()
      fields = ("email", "username")
