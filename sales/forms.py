from django.forms import ModelForm
from sales.models import Sale

class SaleForm(ModelForm):
    class Meta:
        model = Sale
        fields = ['id','user','products','trace_code','note']