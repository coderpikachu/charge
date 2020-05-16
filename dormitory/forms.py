from django import forms  
from .models import Dormitory
class DormitoryForm(forms.ModelForm):  
    class Meta:  
        model = Dormitory  
        fields = "__all__"  
    # def clean_peopleNum(self,*args,**kwargs):
    # 	peopleNum=self.cleaned_data.get('peopleNum')
    # 	print(22)
    # 	if peopleNum <= 0:
    # 		print(44)
    # 		raise forms.ValidationError('invalid peopleNum')
    # 	return peopleNum
    def clean_dId(self):
        dId= self.clean().get('dId')
        if len(dId)>100: 
            self.add_error('dId', "The dId has more than 100 digits")
        return dId
    def clean_accommodationCharge(self):
        accommodationCharge= self.clean().get('accommodationCharge')
        if accommodationCharge<0: 
            self.add_error('accommodationCharge', "The accommodationCharge is invalid")
        return accommodationCharge
    def clean_telephone(self):
        telephone= self.clean().get('telephone')
        if len(telephone)!=11: 
            self.add_error('telephone', "The valid telephone has 11 numbers")
        return telephone