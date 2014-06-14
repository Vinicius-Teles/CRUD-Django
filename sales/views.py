from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from sales.forms import SaleForm
from sales.models import Sale

# Create your views here.

def index(request):
	if request.method == 'POST':
		form = SaleForm(request.POST)
		if not form.data['id']:
			form.save()
		else:
			edit = get_object_or_404(Sale, pk=form.data['id'])
			formEdit = SaleForm(request.POST or None, instance=edit)
			formEdit.save();
	return render(request,'sales/index.html',{
    	'form': SaleForm(),
    	'sales': Sale.objects.all()
    })
	
def edit(request,sale_id):
	sale = Sale.objects.get(pk=sale_id)
	form = SaleForm(instance=sale)
	return render(request,'sales/index.html',{
    	'form': form,
    	'sales': Sale.objects.all(),
    	'id': sale_id
    })

def delete(request,sale_id):
	sale = Sale.objects.get(pk=sale_id)
	sale.delete();
	return redirect('/')

def search(request):
	search = request.POST['search']
	sales = ""
	if type( search ) == int:
		sales = Sale.objects.filter(id=int(search))
	return render(request, 'sales/index.html',{
		'form' : SaleForm(),
		'sales' : sales
	})