from django import forms
from .models import Todo_List

class Todo_Item_Form(forms.ModelForm):
    class Meta:
        model = Todo_List
        fields = ['title', 'description']

    
