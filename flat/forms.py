from django import forms  
from .models import Flat
class FlatForm(forms.ModelForm):  
    class Meta:  
        model = Flat  
        fields = "__all__"  
    def clean_fId(self):
        fId= self.clean().get('fId')
        if len(fId)>100: 
            self.add_error('fId', "The fId has more than 100 digits")
        return fId

    def clean_layers(self):
        layers= self.clean().get('layers')
        if layers<=0: 
            self.add_error('layers', "The layers are invalid")
        return layers

    def clean_roomNum(self):
        roomNum= self.clean().get('roomNum')
        if roomNum<=0: 
            self.add_error('roomNum', "The roomNum is invalid")
        return roomNum