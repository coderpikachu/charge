from django import forms  
from .models import User
class UserForm(forms.ModelForm):  
    class Meta:  
        model = User  
        fields = "__all__"  

    def clean_uId(self):
        uId= self.clean().get('uId')
        if len(uId)>100: 
            self.add_error('uId', "The uId has more than 100 digits")
        return uId