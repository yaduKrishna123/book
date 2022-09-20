from django  import forms
from .models import book

class bookForm(forms.ModelForm):
    class Meta:
        model=book
        fields=['name','dec','year','img']
