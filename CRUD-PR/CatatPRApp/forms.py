from django import forms
from .models import PR, StatusPR

class PRForm(forms.ModelForm):
    class Meta:
        model = PR
        fields = [
            'tgl_pr', 
            'partnumber', 
            'partname', 
            'qty', 
            'deskripsi',
            'status',
            #'tgl_terima'
            ]
        widgets = {
            'tgl_pr': forms.DateInput(attrs={'type': 'date'}),
            'partnumber': forms.TextInput(attrs={'class': 'form-control'}),
            'partname': forms.TextInput(attrs={'class': 'form-control'}),
            'qty': forms.NumberInput(attrs={'class': 'form-control'}),
            'deskripsi': forms.TextInput(attrs={'class': 'form-control'}),            
            'status': forms.Select(attrs={'class': 'form-control'}),
            #'tgl_terima': forms.DateInput(attrs={'type': 'date'}),            
        }

    """def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['status'].queryset = StatusPR.objects.order_by('status')  # Replace `name` with the field you want to sort by"""

class StatusPRForm(forms.ModelForm):
    class Meta:
        model = StatusPR
        fields = ['status']
        widgets = {
            'status': forms.TextInput(attrs={'class': 'form-control'}),
        }
