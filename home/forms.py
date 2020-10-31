from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class RegisterForm(forms.Form):
    first_name = forms.CharField(label="First name" ,max_length=50)
    last_name = forms.CharField(label="Last name" ,max_length=50)
    username = forms.CharField(label="Username", max_length=30)
    password1 = forms.CharField(label="Password", max_length=20, widget=forms.PasswordInput)
    password2 = forms.CharField(label="re-password", max_length=20, widget=forms.PasswordInput)
    email = forms.EmailField(label="Email address")

    #check password 1 and password 2
    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2 and password1:
                return password2
        raise forms.ValidationError("password not match")

    #check username
    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):#kiểm tra user có ký tự đặc biệt
            raise forms.ValidationError("username not specified")
        try:#kiểm tra username có trùng không
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError("username already exists")
    #hàm lưu lại user
    def save_user(self):
        User.objects.create_user(
            first_name = self.cleaned_data['first_name'],
            last_name = self.cleaned_data['last_name'],
            username = self.cleaned_data['username'],
            password = self.cleaned_data['password2'],
            email = self.cleaned_data['email']
            )

