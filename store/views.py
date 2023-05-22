from django.shortcuts import render, get_object_or_404

from store.models import Item


def item_list(request, category_slug):
    # cart = Cart(request)
    items = Item.objects.filter(category=category_slug, available=True)
    return render(request, 'list.html', {'items': items})


def item_detail(request, id, slug):
    item = get_object_or_404(Item, id=id, slug=slug, available=True)
    return render(request,
                  'item_detail.html',
                  {'item': Item}
                  )