from django import forms
from django.forms import ModelForm
from .models import Book
from .models import Message

RATING_CHOICES = [(str(i), str(i)) for i in range(1, 6)]

class BookForm(ModelForm):
    rating = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = Book
        fields = ['name', 'web', 'price', 'picture', 'comments', 'rating']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'web': forms.URLInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'picture': forms.FileInput(attrs={'class': 'form-control-file'}),
            'comments': forms.Textarea(attrs={'class': 'form-control'}),
            'rating': forms.Select(attrs={'class': 'form-control'}),
        }

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = [
            'message','user',
            ]
