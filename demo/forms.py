from django import forms


class AddNewUserForm(forms.Form):
    guid = forms.CharField()
