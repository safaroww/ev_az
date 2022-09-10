from django.shortcuts import render, redirect
from .forms import ContactForm

# Create your views here.
def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sale:home')
    return render(request, 'info/contact.html', context={'form': form})