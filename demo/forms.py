from django import forms


class AddNewCompanyForm(forms.Form):
    company_id = forms.CharField()
