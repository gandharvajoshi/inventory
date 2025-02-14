from django.shortcuts import render
from django.urls import reverse
from .models import Inventory  # Import the InventoryItem model
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
@login_required
def delete_item(request, item_id):
    item = get_object_or_404(Inventory, id=item_id)  # Get the item or return 404
    if request.method == 'POST':
        item.delete()  # Delete the item
        return redirect(reverse(mainpage))  # Redirect to the inventory list
    return render(request, 'inventor/confirm_delete.html', {'item': item})

@login_required
def mainpage(request):
    # Fetch all inventory items from the database
    items = Inventory.objects.all()
    
    # Pass the items to the template
    context = {
        'items': items,
    }
    return render(request, 'main/mainpage.html', context)