# Week 8 — Day 2: Cookies, Sessions & Django Forms

## 📚 Overview
Day 1 covered:
- Cookies & Sessions in Django
- Django Forms and validation
- Practical testing through two Django labs

## 🎯 Key Concepts

### Cookies
Cookies store small values in the browser.

```python
theme = request.COOKIES.get("theme", "light")

response.set_cookie(
    "theme",
    theme,
    max_age=60 * 60 * 24 * 30
)
```

### Sessions
Sessions store application state server-side while the browser carries a session identifier.

```python
cart = request.session.get("cart", [])
request.session["cart"] = cart
request.session.pop("cart", None)
```

### Cookie vs Session
| Cookie | Session |
|---|---|
| Browser-side value | Server-side state |
| Preferences | Temporary trusted app state |
| Example: theme | Example: cart |

### Django Forms
Forms provide fields, validation, cleaning and errors.

```python
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    rating = forms.IntegerField(required=False)
```

Custom validation:

```python
def clean_message(self):
    message = self.cleaned_data["message"]

    if len(message) < 20:
        raise forms.ValidationError("Message is too short.")

    return message
```

### GET / POST Flow

```text
GET → empty form
POST → ContactForm(request.POST)
     → is_valid()
        ├─ False → render errors
        └─ True → redirect
```

`cleaned_data` should only be used after `is_valid()` succeeds.

### CSRF
For POST forms:

```html
<form method="post">
    {% csrf_token %}
    {{ form }}
    <button type="submit">Submit</button>
</form>
```

CSRF protects the request; form validation checks the submitted values.

---

# 🧪 Lab 1 — Preferences & Cart

### Goal
Practice cookies, cookie validation, sessions, adding to a cart and clearing session data.

### Routes
- `/` — home/current theme
- `/theme/light/` — set light theme
- `/theme/dark/` — set dark theme
- `/cart/` — view cart
- `/cart/add/` — add product 101
- `/cart/clear/` — clear cart

### Main code

```python
def home(request):
    theme = request.COOKIES.get("theme", "light")

    return render(request, "shop/home.html", {
        "theme": theme
    })
```

```python
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
```

```python
def cart(request):
    cart = request.session.get("cart", [])

    return render(request, "shop/message.html", {
        "title": "Shopping Cart",
        "message": f"Your cart: {cart}"
    })
```

```python
def add_to_cart(request):
    cart = request.session.get("cart", [])

    cart.append(101)
    request.session["cart"] = cart
    request.session.modified = True

    return render(request, "shop/message.html", {
        "title": "Product Added",
        "message": f"Product 101 added to your cart. Current cart: {cart}"
    })
```

```python
def clear_cart(request):
    request.session.pop("cart", None)

    return render(request, "shop/message.html", {
        "title": "Cart Cleared",
        "message": "Your shopping cart has been cleared."
    })
```

### Testing completed
- ✅ Theme saved and persisted
- ✅ Cart started empty
- ✅ Product 101 added
- ✅ Cart persisted after refresh/new tab
- ✅ Cart cleared successfully
- ✅ Invalid theme rejected
- ✅ Missing `django_session` table fixed with `python manage.py migrate`
- ✅ `python manage.py check` passed

---

# 🧪 Lab 2 — Feedback Form

### Goal
Build a Django form with validation and a success page.

### View pattern

```python
if request.method == "POST":
    form = ContactForm(request.POST)

    if form.is_valid():
        return redirect("thank_you")
else:
    form = ContactForm()
```

### Testing completed
- ✅ Short message showed `Message is too short.`
- ✅ Error stayed on the same page
- ✅ Valid submission reached Thank You page
- ✅ CSRF included
- ✅ Styling completed
- ✅ `python manage.py check` passed

---

# 🔴 MUST UNDERSTAND

- **Cookie = browser value**
- **Session = server-side application state**
- **Form = validation contract**
- `request.POST` = raw submitted data
- `form.cleaned_data` = validated data
- `clean_<field>()` = one-field custom validation
- `clean()` = cross-field validation
- Invalid form → render again with errors
- Valid POST → redirect (PRG pattern)

# 🟡 IMPORTANT

- `max_age` is measured in seconds.
- `request.session.get("cart", [])` gives a safe default.
- `session.pop("cart", None)` safely removes a key.
- `{% csrf_token %}` protects POST forms.
- If `django_session` is missing, run:

```bash
python manage.py migrate
```

# ⚠️ Common Mistakes

Wrong:
```python
form = ContactForm()
```

for a POST request.

Correct:
```python
form = ContactForm(request.POST)
```

Do not read `cleaned_data` before `is_valid()`.

Do not redirect an invalid form because that loses the bound form errors.

# 🚫 Don't Confuse

```text
Cookie → browser
Session → server

Field → data type + validation
Widget → HTML representation

CSRF → request protection
Validation → submitted-value checking
```

# 🗺️ Mental Map

```text
Django Day 1
│
├── Cookies
│   └── Theme → browser
│
├── Sessions
│   └── Cart → server-side state
│
└── Forms
    ├── Fields
    ├── Validation
    ├── cleaned_data
    ├── CSRF
    └── POST → validate → redirect
```

# ✅ Completion

- [x] Lab 1 — Preferences & Cart
- [x] Lab 2 — Feedback Form
- [x] Functional tests
- [x] Error-case tests
- [x] `python manage.py check`

**Week 8 — Day 2 Labs Complete 🎉**
