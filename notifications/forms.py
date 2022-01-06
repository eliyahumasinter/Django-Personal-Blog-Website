from django import forms
from .models import Email


class EmailUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Email
        fields = ['email']


class SendEmailForm(forms.Form):
    subject = forms.CharField(max_length=100, empty_value="hello")
    message = forms.CharField(widget=forms.Textarea)
