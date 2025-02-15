# inventory/views.py
from django.shortcuts import render
from main.models import Inventory
from django.urls import reverse
from .forms import forms
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User


@login_required(login_url='/login/')
def add_item(request):
    if request.method == 'POST':
        form = InventoryForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
    else:
        form = InventoryForm()
    return render(request, 'action/add_item.html', {'form': form})

# View to delete an inventory item

from django import forms
from django import forms
from main.models import Inventory

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['name', 'price', 'quantity']


# Create your views here.
