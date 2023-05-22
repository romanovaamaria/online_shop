from django.shortcuts import render

from category.models import Category


def category_list(request):
    # cart = Cart(request)
    categories = Category.objects.filter()
    return render(request, 'list.html', {'categories': categories})
