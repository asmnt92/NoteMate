from django import forms
from notes.models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model=Notes
        fields='__all__'
        
        widgets={
            'title':forms.TextInput(attrs={
                'class':'w-full border-2 rounded-md p-2 focus:ring-2 focus:ring-blue-400 outline-none',
                'placeholder':'Write Title',
                'name':'title',
            }),
            'note':forms.Textarea(attrs={
                'class':'w-full border-2 rounded-md p-2 focus:ring-2 focus:ring-blue-400 outline-none',
                'placeholder':'Write Node',
                'name':'note',
                'rows':4,
            })

        }

  


    
