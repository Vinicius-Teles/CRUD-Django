from django.contrib import admin

# Register your models here.
from sales.models import Sale

class SaleAdmin(admin.ModelAdmin):
	list_display=('__str__','user','listProductsString','date','value','note','trace_code')

admin.site.register(Sale, SaleAdmin)