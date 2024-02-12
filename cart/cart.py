from store.models import Painting


class Cart:
    def __init__(self, request):
        self.session = request.session

        # Get the session key if exist
        cart = self.session.get('session_key')

        # If the user is new, no session key, create one
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        # Make sure cart is available on all pages site
        self.cart = cart

    def add(self, product):
        product_id = str(product.id)

        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'price': str(product.price)}

        self.session.modified = True

    def __len__(self):
        return len(self.cart)

    def get_products(self):
        # Get ids from cart
        product_ids = self.cart.keys()

        # Use products to lookup  in DDBB
        products = Painting.objects.filter(id__in=product_ids)

        return products

    def delete(self, product):
        product_id = str(product)
        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified = True

    def cart_total(self):
        product_ids = self.cart.keys()
        products = Painting.objects.filter(id__in=product_ids)
        quantities = self.cart
        total = 0
        for key, value in quantities.items():
            key = int(key)
            for product in products:
                if product.id == key:
                    total += product.price

        return total
