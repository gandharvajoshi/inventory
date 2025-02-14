# inventory/forms.py
from django import forms
from main.models import Inventory

class InventoryItemForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['name', 'price', 'quantity']