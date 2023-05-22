from django.shortcuts import render, get_object_or_404

from store.models import Product


def product_list(request, category_slug):
    # cart = Cart(request)
    products = Product.objects.filter(category=category_slug, available=True)
    return render(request, 'list.html', {'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request,
                  'product_detail.html',
                  {'product': product}
                  )
