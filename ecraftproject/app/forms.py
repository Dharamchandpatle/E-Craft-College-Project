from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'gender', 'email', 'address', 'mobile_no']