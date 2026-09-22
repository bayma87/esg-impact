from django import forms

from .models import ContactMessage


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Seu nome',
                'class': 'field-input',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'seu@email.com',
                'class': 'field-input',
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Escreva sua mensagem...',
                'class': 'field-input field-textarea',
                'rows': 5,
            }),
        }
