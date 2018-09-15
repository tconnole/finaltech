from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import Contact
from .forms import ContactForm



#def index(request):
#    contex = {}
#    return render(request, 'Contacts/index.html')

def index(request):
    reminder_list = Contact.objects.order_by('id')

    form = ContactForm()

    context = {'reminder_list' : reminder_list, 'form' : form}
    return render(request, 'Contacts/index.html', context)

@require_POST
def addContact(request):
    form = ContactForm(request.POST)

    print(request.POST['title'])

    if form.is_valid():
        new_reminder = Contact(title_text=request.POST['title'], due_date=request.POST['due'],
                                Contact_description=request.POST['desc'])
        new_reminder.save()

    return redirect('index')

def completeContact(request, Contact_id):
    reminder = Contact.objects.get(pk=Contact_id)
    reminder.delete()

    return redirect('index')

def deleteAll(request):
    Contact.objects.all().delete()

    return redirect('index')