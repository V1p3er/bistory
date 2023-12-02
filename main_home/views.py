from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .models import CartItem, Product
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home/index.html')
@login_required(login_url='/accounts/login/')
def add_to_cart(request, product_id):
    user = request.user
    product = Product.objects.get(id=product_id)

    if user.is_authenticated:
        # Assuming you have a cart model related to the user
        cart, created = Cart.objects.get_or_create(user=user)

        # Get the cart item, or create one if it doesn't exist
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

        if created:
            cart_item.quantity = 1
        else:
            cart_item.quantity += 1
        
        cart_item.save()
        
        # Redirect to cart page or wherever is appropriate
        return redirect('cart_detail_url')
def menu(request):
    return render(request, 'home/other/menu.html')
def logout_p(request):
    logout(request)
    return redirect('home')
def cart(request): 
    return redirect('../users/')