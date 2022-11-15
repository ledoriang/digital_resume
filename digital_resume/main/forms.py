from django import forms

from .models import ContactProfile


class ContactForm(forms.ModelForm):
    name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder':'Name'}))

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder':'Email'}),
        max_length=100)
        
    message = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'placeholder':'Message','rows':6}),
        max_length=1000)
    
    class Meta:
        model = ContactProfile
        fields = ('name','email','message')
        
        