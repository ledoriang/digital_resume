from django import forms

from .models import ContactProfile


class ContactForm(forms.ModelForm):
    name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}))

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'})
        max_length=100)
        
    message = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Message','rows':5}),
        max_length=1000)
    
    class Meta:
        model = ContactProfile
        fields = ('name','email','message')
        
        