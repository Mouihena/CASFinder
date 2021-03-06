from django.forms import ModelForm
from django import forms
from models import uploadImage


class smilesForm(forms.Form):
    smiles = forms.CharField(label = 'INPUT SMILES  ',)
    
class uploadFileForm(forms.Form):
    MOL = 'MOL'
    CDX = 'CDX'
    # SDF = 'SDF'
    UPLOAD_FILE_TYPE = (
        (MOL,'MDL Molfile'),
        (CDX,'CDX File'),
        # (SDF,'SD File')
    )
    file = forms.FileField()
    upload_file_type = forms.ChoiceField(label = 'File Type:', choices = UPLOAD_FILE_TYPE) 
    name = forms.CharField(max_length=50)
    
class uploadImageForm(ModelForm):  
    class Meta:
        model = uploadImage  
        fields = ['upload_file',]
    
    