from django import forms  
from .models import Charges
class ChargeForm(forms.ModelForm):  
    class Meta:  
        model = Charges
        fields = "__all__"  