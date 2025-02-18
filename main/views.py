from django.shortcuts import render
from django.urls import reverse
from .models import Inventory  # Import the InventoryItem model
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from .forms import InventoryItemForm

@login_required(login_url='login_view')
def delete_item(request, item_id):
    item = get_object_or_404(Inventory, id=item_id)  # Get the item or return 404
    if request.method == 'POST':
        item.delete()  # Delete the item
        return redirect(reverse(mainpage))  # Redirect to the inventory list
    return render(request, 'inventor/confirm_delete.html', {'item': item})

@login_required(login_url='/login/')
def mainpage(request):
    # Fetch all inventory items from the database
    items = Inventory.objects.filter(user=request.user)
    
    # Pass the items to the template
    context = {
        'items': items,
    }
    return render(request, 'main/mainpage.html', context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login_view'))

def update_item(request, item_id):
    # Get the item to be updated or return a 404 error if not found
    item = get_object_or_404(Inventory, id=item_id)

def update_item(request, item_id):
    item = get_object_or_404(Inventory, id=item_id)
    if request.method == 'POST':
        form = InventoryItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('mainpage')
    else:
        form = InventoryItemForm(instance=item)
    return render(request, 'main/update_item.html', {'form': form})