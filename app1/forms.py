from django import forms
from app1.models import employee_model
class employee_form(forms.ModelForm):
    class Meta:
     model = employee_model
     fields='__all__'