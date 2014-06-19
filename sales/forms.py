from django.forms import ModelForm,Textarea,TextInput,SelectMultiple,Select
from django import forms
from sales.models import Sale

class SaleForm(ModelForm):
    class Meta:
        model = Sale
        fields = ['id','user','products','trace_code','note']
        widgets = {
            'note': Textarea(
            	attrs={
            		'class': 'form-control'
            	},
            ),
            'trace_code': TextInput(
            	attrs={
            		'class': 'form-control'
            	},
            ),
            'user': Select(
            	attrs={
            		'class': 'form-control'
            	},
            ),
            'products': SelectMultiple(
            	attrs={
            		'class': 'form-control'
            	}
            )
        }
        