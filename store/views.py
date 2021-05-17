from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from cart.models import CartItem
from cart.views import _cart_id
from category.models import Category
from subcategory.models import SubCategory
from products.models import Product


# Create your views here.


def store(request, category_slug=None, subcategory_slug=None):
    categories = None
    subcategories = None
    products = None

    if category_slug is not None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        paginator = Paginator(products, 3)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
        if subcategory_slug is not None:
            subcategories = get_object_or_404(SubCategory, slug=subcategory_slug)
            products = Product.objects.filter(subcategory=subcategories, is_available=True)
            product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True).order_by('id')
        paginator = Paginator(products, 6)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()

    context = {
        'products': paged_products,
        'product_count': product_count,
    }

    return render(request, template_name='store/store.html', context=context)


def product_detail(request, category_slug, subcategory_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug,
                                             subcategory__slug=subcategory_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product)
    except Exception as e:
        raise e

    context = {
        'single_product': single_product,
        'in_cart': in_cart,
    }
    return render(request, template_name='store/product_detail.html', context=context)


def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
            product_count = products.count()

    context = {
        'products': products,
        'product_count': product_count,
    }
    return render(request, template_name='store/store.html', context=context)
