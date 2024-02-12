from .cart import Cart


# Create context processors so our cart can work on all pages
def cart(request):
    # Return de default data from our cart
    return {'cart': Cart(request)}
