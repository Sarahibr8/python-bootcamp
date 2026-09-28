from django.shortcuts import render


products = [
    {
        "id": 1,
        "name": "Laptop",
        "category": "electronics",
        "price": 3500,
        "rating": 4.8,
        "description": "Powerful laptop for work and study.",
    },
    {
        "id": 2,
        "name": "Wireless Headphones",
        "category": "electronics",
        "price": 450,
        "rating": 4.5,
        "description": "Comfortable wireless headphones.",
    },
    {
        "id": 3,
        "name": "Python Book",
        "category": "books",
        "price": 120,
        "rating": 4.7,
        "description": "A practical book for learning Python.",
    },
    {
        "id": 4,
        "name": "Desk Lamp",
        "category": "home",
        "price": 180,
        "rating": 4.2,
        "description": "Modern desk lamp for your workspace.",
    },
    {
        "id": 5,
        "name": "Mechanical Keyboard",
        "category": "electronics",
        "price": 320,
        "rating": 4.6,
        "description": "Responsive mechanical keyboard for work and gaming.",
    },
    {
        "id": 6,
        "name": "Python Programming Book",
        "category": "books",
        "price": 150,
        "rating": 4.8,
        "description": "A practical guide to Python programming.",
    },
    {
        "id": 7,
        "name": "Coffee Maker",
        "category": "home",
        "price": 280,
        "rating": 4.4,
        "description": "Compact coffee maker for your home.",
    },
    {
        "id": 8,
        "name": "Wireless Mouse",
        "category": "electronics",
        "price": 120,
        "rating": 4.5,
        "description": "Comfortable wireless mouse for everyday use.",
    },
]


def product_list(request):
    category = request.GET.get("category", "")
    min_price = request.GET.get("min_price", "")
    q = request.GET.get("q", "")
    sort = request.GET.get("sort", "name")
    page = request.GET.get("page", "1")

    filtered_products = products

    if category:
        filtered_products = [
            product for product in filtered_products
            if product["category"] == category
        ]

    if min_price:
        try:
            min_price = float(min_price)

            filtered_products = [
                product for product in filtered_products
                if product["price"] >= min_price
            ]

        except ValueError:
            min_price = ""

    if q:
        filtered_products = [
            product for product in filtered_products
            if q.lower() in product["name"].lower()
        ]

    allowed_sort = ["price", "rating", "name"]

    if sort not in allowed_sort:
        sort = "name"

    filtered_products = sorted(
        filtered_products,
        key=lambda product: product[sort]
    )

    try:
        page = int(page)
    except ValueError:
        page = 1

    per_page = 4

    total_pages = (
        len(filtered_products) + per_page - 1
    ) // per_page

    if page < 1:
        page = 1

    if total_pages and page > total_pages:
        page = total_pages

    start = (page - 1) * per_page
    end = start + per_page

    paginated_products = filtered_products[start:end]

    return render(request, "products/product_list.html", {
        "products": paginated_products,
        "category": category,
        "min_price": min_price,
        "q": q,
        "sort": sort,
        "page": page,
        "total_pages": total_pages,
    })


def product_detail(request, id):
    product = next(
        (product for product in products if product["id"] == id),
        None
    )

    if product is None:
        return render(
            request,
            "products/404.html",
            status=404
        )

    tab = request.GET.get("tab", "details")

    allowed_tabs = ["details", "reviews", "shipping"]

    if tab not in allowed_tabs:
        tab = "details"

    return render(request, "products/product_detail.html", {
        "product": product,
        "tab": tab,
    })