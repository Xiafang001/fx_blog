from django import forms
from .models import SayHello


class SayHelloForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Message'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    website = forms.URLField(widget=forms.TextInput(attrs={'placeholder': 'URL'}))
    
    class Meta:
        model = SayHello
        fields = ('name', 'message',  'email', 'website')
    
    def clean_message(self):
        data = self.cleaned_data['message']
        if len(data) < 20:
            raise forms.ValidationError("Your message is too short")
        return data
