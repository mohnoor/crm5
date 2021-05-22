from django import forms  
from .models import custumer  
class n(forms.ModelForm):  
	class meta:
		model=custumer
		fields = ['username', 'fname']
			
