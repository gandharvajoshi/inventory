from django import forms
from main.models import Inventory

class InventoryItemForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['name', 'price', 'quantity']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})