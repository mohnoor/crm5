from django import forms  
from .models import custumer  
class EmployeeForm(forms.ModelForm):  
    class Meta:  
        model = custumer  
        fields = "__all__"  