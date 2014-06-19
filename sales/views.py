from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from sales.forms import SaleForm
from sales.models import Sale
from django.db.models import Q

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

def sales(request):
	form = SaleForm(request.POST)
	return render(request,'sales/form.html',{
    	'form': form,
    	'sales': Sale.objects.all()
    })

def save(request):
	form = SaleForm(request.POST)
	message = "Venda cadastrada com sucesso"
	if form.data['id']:
		edit = get_object_or_404(Sale, pk=form.data['id'])
		form = SaleForm(request.POST or None, instance=edit)
	form.save()
	return redirect('/')
	
def edit(request,sale_id):
	sale = Sale.objects.get(pk=sale_id)
	form = SaleForm(instance=sale)
	return render(request,'sales/form.html',{
    	'form': form,
    	'id': sale_id
    })

def delete(request,sale_id):
	sale = Sale.objects.get(pk=sale_id)
	sale.delete();
	return redirect('/')

def search(request):
	search = request.POST['search']
	query = Q(user__name__icontains=search) | Q(products__name__icontains=search ) | Q(trace_code__icontains=search) | Q(note=search)
	sales = Sale.objects.filter(query).distinct()
	return render(request, 'sales/index.html',{
		'form' : SaleForm(),
		'sales' : sales,
		'search' : search
	})

	