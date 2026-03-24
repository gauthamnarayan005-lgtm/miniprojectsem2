# accounts/forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import User, CustomerProfile

class CustomerSignUpForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=False)
    address = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3}), 
        required=False
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'phone_number')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = "" 

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_customer = True
        user.phone_number = self.cleaned_data.get('phone_number')
        
        if commit:
            user.save()
            CustomerProfile.objects.get_or_create(
                user=user, 
                defaults={'address': self.cleaned_data.get('address')}
            )
        return user

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Username", 
        max_length=254,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Username'})
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'})
    )