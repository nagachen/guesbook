from django import forms
from . models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['user','subject','content']
        widgets = {
            'user':forms.TextInput(attrs={'class':'form-control'}),
            'subject':forms.TextInput(attrs={'class':'form-control'}),
            'content':forms.Textarea(attrs={'class':'form-control'}),          
        }