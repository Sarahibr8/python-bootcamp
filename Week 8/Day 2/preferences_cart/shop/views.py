from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    theme = request.COOKIES.get("theme", "light")

    return render(request, "shop/home.html", {
        "theme": theme
    })

def set_theme(request, theme):
    if theme not in ["light", "dark"]:
        return render(request, "shop/message.html", {
            "title": "Invalid Theme",
            "message": "Please choose a valid theme: light or dark."
        }, status=400)

    response = render(request, "shop/message.html", {
        "title": "Theme Updated",
        "message": f"Your theme has been set to {theme}."
    })

    response.set_cookie(
        "theme",
        theme,
        max_age=60 * 60 * 24 * 30
    )
    return response

def cart(request):
    cart = request.session.get("cart", [])
    return render(request, "shop/message.html", {
        "title": "Shopping Cart",
        "message": f"Your cart: {cart}"
    })

def add_to_cart(request):
    cart = request.session.get("cart", [])

    cart.append(101)
    request.session["cart"] = cart
    request.session.modified = True
    return render(request, "shop/message.html", {
        "title": "Product Added",
        "message": f"Product 101 added to your cart. Current cart: {cart}"
    })

def clear_cart(request):
    request.session.pop("cart", None)
    return render(request, "shop/message.html", {
        "title": "Cart Cleared",
        "message": "Your shopping cart has been cleared."
    })