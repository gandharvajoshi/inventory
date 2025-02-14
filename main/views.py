from django.shortcuts import render
from .models import Inventory  # Import the InventoryItem model

def mainpage(request):
    # Fetch all inventory items from the database
    items = Inventory.objects.all()
    
    # Pass the items to the template
    context = {
        'items': items,
    }
    return render(request, 'main/mainpage.html', context)