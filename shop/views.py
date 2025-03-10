from django.shortcuts import render,get_object_or_404
from .models import Product, Category
from cart.forms import CartAddProductForm
from django.contrib.auth.decorators import login_required


def homepage(request):
    categories = Category.objects.all()
    giveaway = Product.objects.filter(category__name="Smartphones").order_by("-price").first()
    prod = Product.objects.filter(avaliable=True).first()
    best_seller = Product.objects.order_by("-price")[:4]
    return render(request, 'index.html',{'categories': categories,'giveaway':giveaway,'prod':prod, 'best_seller':best_seller})
    
@login_required
def product(request, category_slug = None):
    category = None
    categories = Category.objects.all()
    cart_product_form = CartAddProductForm()
    
    products = Product.objects.filter(avaliable=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'product.html',{
        'category':category,
        'categories':categories,
        'products':products,
        'cart_product_form':cart_product_form,
        
    })

@login_required
def product_detail(request, product_id, category_slug = None):
    category = None
    product = get_object_or_404(Product, id=product_id )
    cart_product_form = CartAddProductForm()
    categories = Category.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        product = product.filter(category=category)
    return render(
        request,
        'product_detail.html',
        {'product':product,'category': category, 'categories':categories,'cart_product_form':cart_product_form}
    )
    