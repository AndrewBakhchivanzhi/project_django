from django.shortcuts import render

def contact(request):
    return render(request, 'catalog/contacts.html')

def home(request):
    return render(request, 'catalog/home.html')
