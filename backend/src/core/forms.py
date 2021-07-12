from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from core.models import Profile


class ProfileCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )

    class Meta:
        model = Profile
        fields = ["email", "name"]

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(ProfileCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class ProfileChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin"s
    password hash display field.
    """

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Profile
        fields = ["email", "password", "name", "is_active", "is_admin"]

    def clean_password(self):
        return self.initial["password"]
