from django import forms  
from .models import Charges
class ChargeForm(forms.ModelForm):  
    class Meta:  
        model = Charges
        fields = "__all__"  
    def clean_cId(self):
        cId= self.clean().get('cId')
        if len(cId)>100: 
            self.add_error('cId', "The cId has more than 100 digits")
        return cId
    def clean_money(self):
        money= self.clean().get('money')
        if len(money)>100: 
            self.add_error('money', "The money is invalid")
        return money