from django import forms  
from .models import Flat
class FlatForm(forms.ModelForm):  
    class Meta:  
        model = Flat  
        fields = "__all__"  