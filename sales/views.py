from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from sales.forms import SaleForm
from sales.models import Sale
from django.db.models import Q
from django.contrib import messages
# Create your views here.

def index(request):
	return render(request,'sales/index.html',{
    	'sales': Sale.objects.all()
    })

def sales(request):
	form = SaleForm(request.POST)
	return render(request,'sales/form.html',{
    	'form': form,
    })

def save(request):
	form = SaleForm(request.POST)
	message = "Venda cadastrada com sucesso"
	sale_id = form.data['id']
	if sale_id:
		message = "Venda editada com sucesso"
		inst = Sale.objects.get(pk=sale_id)
		form = SaleForm(request.POST or None, instance=inst)
	messages.add_message(request, messages.INFO, message, extra_tags='alert-success')
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
	messages.add_message(request, messages.INFO, "Venda deletada com sucesso", extra_tags='alert-success')
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

	