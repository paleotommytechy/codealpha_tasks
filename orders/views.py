from django.shortcuts import render
from cart.cart import Cart
from .forms import OrderCreateForm
from .models import OrderItem

def order_create(request):
    cart = Cart(request)
    order = None
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            cart.clear()
            return render(request, 'created.html',{'order':order})
    else:
        form = OrderCreateForm()
    return render(request, 'create.html',{'cart':cart, 'form':form})
