from django.shortcuts import render, redirect, reverse
from .forms import MessageForm
# Create your views here.
def index_page(request):
    return render(request, 'index.html')

def about_page(request):
    return render(request, 'about.html')

def services_page(request):
    return render(request, 'services.html')

def skills_page(request):
    return render(request, 'skills.html')
    
def contact_page(request):

    return render(request, 'contact.html', {"message_form" : MessageForm, "status": "new"})


def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact.html', {"message_form" : MessageForm, "status": "submitted"})
    else:
        return render(request, 'contact.html', {"message_form" : MessageForm, "status": "wrong"})
    return render(request, 'contact.html', {"message_form" : MessageForm, "status": "new"})
