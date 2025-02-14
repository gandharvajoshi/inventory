# inventory/views.py
from django.shortcuts import render
from main.models import Inventory
from django.urls import reverse
from .forms import forms
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
# View to list all inventory items
def inventory_list(request):
    items = Inventory.objects.all()
    return render(request, 'inventory/inventory_list.html', {'items': items})

# View to add a new inventory item
@login_required
def add_item(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    if request.method == 'POST':
        form = InventoryForm(request.POST)
        if form.is_valid():
            form.save()
            
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

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['name', 'price', 'quantity']

# Create your views here.
