from django import forms
from  .models import UserAccounts
from django.contrib.auth.forms import UserCreationForm
class Create_new_user(UserCreationForm):
    class Meta:
        model = UserAccounts
        fields = ['email','phone']