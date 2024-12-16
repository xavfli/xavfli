from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q

from .models import Product, Comment, Cart
from app_users.models import Customer
from django.contrib.auth.decorators import login_required

def home_page(request):
    query = request.GET.get('q')
    search = request.GET.get('search', '')

    products = Product.objects.filter(name__icontains=search)

    if query:
        if query == 'expensive':
            products = products.order_by('-new_price')
        elif query == 'cheap':
            products = products.order_by('new_price')
        elif query == 'rating':
            products = products.order_by('-rating')
        elif query == 'new-arrivals':
            products = products.order_by('-created')

    # Savatchadagi mahsulotlar sonini hisoblash
    if request.user.is_authenticated:
        cart_products_quantity = request.user.cart_set.count()
    else:
        cart_products_quantity = 0

    context = {
        'products': products,
        'search': search,
        'is_home_page': True,
        'cart_products_quantity': cart_products_quantity,  
    }

    return render(request, 'index.html', context)

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        comment = request.POST.get('comment')
        
        if comment and len(comment.strip()) >= 10:
            new_comment = Comment.objects.create(
                owner=request.user,
                product=product,
                body=comment
            )
            new_comment.save()
            return redirect(f'/detail/{product_id}#comments-section')

    context = {
        'product': product,
        'last_3_comments': product.comment_set.all()[::-1][:3]
    }

    return render(request, 'detail.html', context)


@login_required(login_url = 'login')
def add_to_cart(request, product_id):

    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = request.POST.get('quantity')
        
        try:
            cart =  Cart.objects.create(
                product = get_object_or_404(Product, id=product_id),
                user = get_object_or_404 (Customer, id=request.user.id),
                quantity = quantity
            )
            cart.save()
        except:
           product = request.user.cart_set.all().get(product__id=product_id)
           product.quantity += int(quantity)
           product.save()
             

       
    return redirect('detail', product_id = product_id)