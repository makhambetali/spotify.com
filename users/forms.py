from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewUserForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'main-input', 'placeholder':'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'main-input', 'placeholder':'Last Name'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'main-input', 'placeholder':'Email Address'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'main-input', 'placeholder':'Username'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'main-input', 'placeholder':'Create Password'}), min_length=8)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'main-input', 'placeholder':'Confirm Password'}), min_length=8)
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name',"username", "email", "password1", "password2")
        # fields = ('username')    
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user