from django.shortcuts import render

def index(request):
    contex = {}
    return render(request, 'Contacts/index.html')
