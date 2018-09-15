from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import Contact
from .forms import ContactForm



#def index(request):
#    context = {}
#    return render(request, 'Contacts/index.html')

def index(request):
    Contact_list = Contact.objects.order_by('first')

    form = ContactForm()

    context = {'Contact_list' : Contact_list, 'form' : form}
    return render(request, 'Contacts/index.html', context)

@require_POST
def addContact(request):
    form = ContactForm(request.POST)

    print(request.POST['title'])

    if form.is_valid():
        new_contact = Contact(first_name=request.POST['first'], last_name=request.POST['last'],
                                phone_number=request.POST['phone'], email=require_POST['email'])
        new_contact.save()

    return redirect('index')

def completeContact(request, Contact_id):
    contact = Contact.objects.get(pk=Contact_id)
    contact.delete()

    return redirect('index')

def deleteAll(request):
    Contact.objects.all().delete()

    return redirect('index')