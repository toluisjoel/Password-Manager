from tkinter import Widget
from django import forms
from .models import Website, SiteDetail


class AddPasswordForm(forms.ModelForm):
    
    class Meta:
        model = SiteDetail
        fields = ('username', 'password')
            


class AddSiteForm(forms.ModelForm):
    
    class Meta:
        model = Website
        fields = ('link',)
        
        widgets = {
            'link': forms.TextInput(),
        }