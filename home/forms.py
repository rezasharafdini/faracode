from django import forms


class SendEmailForm(forms.Form):
    name = forms.CharField(max_length=20, widget=forms.TextInput({'placeholder': 'نام...'}))
    email = forms.EmailField(widget=forms.EmailInput({'placeholder':'ایمیل...'}))
    subject = forms.CharField(max_length=50, widget=forms.TextInput({'placeholder': 'موضوع...'}))
    message = forms.CharField(widget=forms.Textarea({'placeholder':'پیام...'}))

