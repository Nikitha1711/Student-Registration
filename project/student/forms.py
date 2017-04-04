from django import forms

class UserForm(forms.Form):
    username = forms.CharField(max_length=15)

    name = forms.CharField(max_length=25)
    # to store the email of the user
    dob = forms.CharField(max_length=10)
    email = forms.EmailField(max_length=25)
    # to store the password of the user
    roll = forms.CharField(max_length=10)
    phone = forms.CharField(max_length=12)
    department = forms.CharField(max_length=25)

    password = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=13, render_value=False)))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=13, render_value=False)))





