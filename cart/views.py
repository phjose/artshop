from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from store.models import Painting

from .cart import Cart


def cart_summary(request):

    cart = Cart(request)
    cart_products = cart.get_products()
    cart_total = cart.cart_total()
    context = {'cart_products': cart_products, 'cart_total': cart_total, }
    return render(request, 'cart_summary.html', context)


def cart_add(request):

    cart = Cart(request)

    # tests for POST
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product = get_object_or_404(Painting, id=product_id)

        # marca el producto como no disponible
        product.available = False
        product.save()

        # Save a session
        cart.add(product=product)

        # Return cart Quantity
        cart_quantity = cart.__len__()

        # Return a response
        # Response = JsonResponse({'Painting name: ': painting.name})
        response = JsonResponse({'qty': cart_quantity})
        return response


def cart_delete(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product = get_object_or_404(Painting, id=product_id)

        cart.delete(product=product_id)

        # marca el producto como disponible
        product.available = True
        product.save()

        response = JsonResponse({'product': product_id})
        return response


def cart_update(request):
    context = {}
    return render(request, 'cart_summary.html', context)
