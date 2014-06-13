from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'sales/index.html')

def save(request):
    return HttpResponse("salvar")

def edit(request):
    return HttpResponse("editar")

def delete(request):
    return HttpResponse("deletar")