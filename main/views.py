from django.shortcuts import render

from django.shortcuts import render

def mainpage(request):
    # Example inventory data (replace this with your actual data)
    inventory = [
        "Item 1: Laptop"
        "Item 2: Mouse",
        "Item 3: Keyboard",
        "Item 4: Monitor",
        "Item 5: Printer",
    ]
    
    # Pass the inventory list as context
    context = {
        'inventory': inventory,
    }
    return render(request, 'main/mainpage.html', context)