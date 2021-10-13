from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Welcome, {username}!")
            return redirect('adoption-index')
        else:
            form = UserRegistrationForm()
        data = {'form': form}
        return render(request, 'registration.html', data)