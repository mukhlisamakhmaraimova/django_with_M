from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomerUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomerUser
        fields = ("username", "first_name", "last_name", "email", "age")

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomerUser
        fields = ("username", "first_name", "last_name", "email", "age")