from django import forms

class ContactForm(forms.Form):
    first = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    phone = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))
    email = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
