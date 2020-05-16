from django import forms  
from .models import Student
class StudentForm(forms.ModelForm):  
    class Meta:  
        model = Student  
        fields = "__all__"  

    def clean_sId(self):
        sId= self.clean().get('sId')
        if len(sId)>100: 
            self.add_error('sId', "The sId has more than 100 digits")
        return sId

    def clean_telephone(self):
        telephone= self.clean().get('telephone')
        if len(telephone)!=11: 
            self.add_error('telephone', "The valid telephone has 11 numbers")
        return telephone