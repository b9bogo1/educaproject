from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, \
    PasswordChangeForm, PasswordResetForm, SetPasswordForm
from .models import Profile

class UserAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(UserAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['username'].widget.attrs.update({'placeholder': 'Username'})
        self.fields['username'].label = ""

        self.fields['password'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Password'})
        self.fields['password'].label = ""

class UserPasswordChange(PasswordChangeForm):
    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')

    def __init__(self, *args, **kwargs):
        super(UserPasswordChange, self).__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update({'class': 'form-control'})
        self.fields['old_password'].widget.attrs.update({'placeholder': 'Old password'})
        self.fields['old_password'].label = ""

        self.fields['new_password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['new_password1'].widget.attrs.update({'placeholder': 'New password'})
        self.fields['new_password1'].label = ""
        self.fields['new_password1'].help_text = "<ul class='small'><li>Your password can't be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can't be a commonly used password.</li><li>Your password can't be entirely numeric.</li></ul>"

        self.fields['new_password2'].widget.attrs.update({'class': 'form-control'})
        self.fields['new_password2'].widget.attrs.update({'placeholder': 'Confirm new password'})
        self.fields['new_password2'].label = ""

class UserPasswordReset(PasswordResetForm):
    class Meta:
        model = User
        fields = ('email',)

    def __init__(self, *args, **kwargs):
        super(UserPasswordReset, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Email Address'})
        self.fields['email'].label = ""


class UserSetPassword(SetPasswordForm):
    class Meta:
        model = User
        fields = ('new_password1', 'new_password2')

    def __init__(self, *args, **kwargs):
        super(UserSetPassword, self).__init__(*args, **kwargs)
        self.fields['new_password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['new_password1'].widget.attrs.update({'placeholder': 'New password'})
        self.fields['new_password1'].label = ""
        self.fields['new_password1'].help_text = "<ul class='small'><li>Your password can't be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can't be a commonly used password.</li><li>Your password can't be entirely numeric.</li></ul>"

        self.fields['new_password2'].widget.attrs.update({'class': 'form-control'})
        self.fields['new_password2'].widget.attrs.update({'placeholder': 'Confirm new password'})
        self.fields['new_password2'].label = ""

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['username'].widget.attrs.update({'placeholder': 'Username'})
        self.fields['username'].label = ""
        self.fields['username'].help_text = "<small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small>"

        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['first_name'].widget.attrs.update({'placeholder': 'First name'})
        self.fields['first_name'].label = ""

        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Last name'})
        self.fields['last_name'].label = ""

        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Email Address'})
        self.fields['email'].label = ""

        self.fields['password'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Password'})
        self.fields['password'].label = ""

        self.fields['password2'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm password'})
        self.fields['password2'].label = ""

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
    
    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['first_name'].widget.attrs.update({'placeholder': 'First name'})
        self.fields['first_name'].label = ""

        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'First name'})
        self.fields['last_name'].label = ""

        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Email Address'})
        self.fields['email'].label = ""
            
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')

    def __init__(self, *args, **kwargs):
        super(ProfileEditForm, self).__init__(*args, **kwargs)
        self.fields['date_of_birth'].widget.attrs.update({'class': 'form-control'})
        self.fields['date_of_birth'].widget.attrs.update({'placeholder': 'Date of birth (YYYY-MM-DD)'})
        self.fields['date_of_birth'].label = ""

        self.fields['photo'].widget.attrs.update({'class': 'form-control'})
        self.fields['photo'].label = "Profile picture"