# WEEK 08 --- DAY 05 \| DJANGO MODELS & FIELD TYPES

> **Define the structure first. Let Django turn that structure into
> database-ready models.**

------------------------------------------------------------------------

## 🎯 Mission of the Day

Today focused on understanding how Django models describe data using
Python classes and model fields.

The day moved from **theory → field selection → model structure → field
options → controlled values → primary keys → practical exercises**.

By the end of the day, the `Product` model was built and then improved
with optional fields, uniqueness, indexing, `TextChoices`, and Django's
automatic primary-key behavior.

------------------------------------------------------------------------

## 🧭 The Journey

  -------------------------------------------------------------------------
  Stage                   Focus                   What Was Practiced
  ----------------------- ----------------------- -------------------------
  01                      Django Model Mental     Model class, field,
                          Model                   instance, and stored
                                                  attribute value

  02                      First Django Model      Defining a model class
                                                  and choosing fields

  03                      Model → Relational      Understanding how fields
                          Table                   map to database columns
                                                  and rows

  04                      Text Fields             `CharField`, `TextField`,
                                                  `SlugField`,
                                                  `EmailField`, `URLField`

  05                      Numeric Fields          `IntegerField`,
                                                  `PositiveIntegerField`,
                                                  `DecimalField`,
                                                  `FloatField`

  06                      Boolean & Date Fields   `BooleanField`,
                                                  `DateField`,
                                                  `DateTimeField`,
                                                  timestamps

  07                      Practical Field Types   `UUIDField`, `JSONField`,
                                                  `ImageField`, `FileField`

  08                      Field Options           `max_length`, `default`,
                                                  `unique`, `db_index`,
                                                  `editable`

  09                      Controlled Values       `TextChoices`, stored
                                                  values, display labels,
                                                  defaults

  10                      Primary Keys            Automatic `id`, `pk`, and
                                                  when a custom primary key
                                                  is justified

  11                      Optional Values         `blank=True` vs
                                                  `null=True`

  12                      Exercise 1              Build the complete
                                                  `Product` model

  13                      Exercise 2              Improve the model with
                                                  additional rules and
                                                  choices
  -------------------------------------------------------------------------

------------------------------------------------------------------------

# 📘 01 --- The Django Model Mental Model

A Django model describes the structure of data using Python classes and
field objects.

### The core mapping

**Model class → Table definition**

**Model field → Database column**

**Model instance → One table row**

**Attribute value → One stored cell**

For example:

``` python
class Product(models.Model):
    name = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=8, decimal_places=2)
```

This describes a `Product` entity with `name` and `price` fields.

### 🔴 MUST UNDERSTAND

The model describes the **structure**. A migration is what later applies
that structure to the database.

Django normally uses the pattern:

``` text
app_label_modelname
```

for the database table name and creates an automatic primary key when
one is not defined manually.

------------------------------------------------------------------------

# 📘 02 --- Creating a Django Model

A model inherits from `models.Model`:

``` python
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=120)
```

### Why?

`models.Model` provides Django's model behavior.

Each class attribute assigned a model field becomes part of the model's
database structure.

### 🔎 Important idea

A model definition comes **before** the database table structure is
applied.

------------------------------------------------------------------------

# 📘 03 --- Text Field Types

The correct field depends on the meaning and expected size of the value.

  Field          Purpose
  -------------- --------------------------------------------
  `CharField`    Short or limited text
  `TextField`    Long content such as descriptions or notes
  `SlugField`    URL-friendly text
  `EmailField`   Email values with validation support
  `URLField`     URL values with validation support

Examples:

``` python
name = models.CharField(max_length=120)

description = models.TextField(blank=True)

slug = models.SlugField(unique=True)

email = models.EmailField()

website = models.URLField(blank=True)
```

### 🔴 MUST UNDERSTAND

`CharField` is for bounded short text, while `TextField` is intended for
longer content.

### ⚠️ Important validation note

An `EmailField` provides validation support, but validation does **not**
automatically run every time `save()` is called.

------------------------------------------------------------------------

# 📘 04 --- Numeric Field Types

Numeric fields should match the meaning and permitted range of the data.

  Field                    Purpose
  ------------------------ ---------------------------------------------
  `IntegerField`           Whole numbers, positive or negative
  `PositiveIntegerField`   Non-negative whole numbers
  `DecimalField`           Fixed decimal precision; suitable for money
  `FloatField`             Approximate floating-point values

Examples:

``` python
quantity = models.IntegerField()

stock = models.PositiveIntegerField(default=0)

price = models.DecimalField(
    max_digits=8,
    decimal_places=2
)

measurement = models.FloatField()
```

### 🔴 MUST UNDERSTAND

For money, the day's material used `DecimalField` because it provides
fixed decimal precision.

For a value such as stock where negative values do not make sense,
`PositiveIntegerField` fits the requirement.

------------------------------------------------------------------------

# 📘 05 --- Boolean and Date Fields

These fields represent state and time directly instead of storing
ambiguous text values.

``` python
is_active = models.BooleanField(default=True)

start_date = models.DateField()

starts_at = models.DateTimeField()
```

### Automatic timestamps

``` python
created_at = models.DateTimeField(auto_now_add=True)

updated_at = models.DateTimeField(auto_now=True)
```

  Option                Meaning
  --------------------- -------------------------------------------------
  `auto_now_add=True`   Records the creation time
  `auto_now=True`       Updates the value each time the object is saved

### 🔴 MUST UNDERSTAND

`DateField` stores a date.

`DateTimeField` stores a date and time.

------------------------------------------------------------------------

# 📘 06 --- Other Practical Field Types

Some data needs a field with a specific storage or structure
requirement.

### `UUIDField`

Used for UUID values, often as public identifiers.

``` python
import uuid

public_id = models.UUIDField(
    default=uuid.uuid4,
    editable=False,
    unique=True
)
```

### `JSONField`

Used for structured JSON data when fixed columns do not fit the data.

``` python
metadata = models.JSONField(default=dict)
```

### `ImageField`

Used for uploaded images and provides image validation support.

``` python
image = models.ImageField(upload_to="products/")
```

The day's material also noted that `ImageField` requires Pillow.

### `FileField`

Used for uploaded files.

``` python
attachment = models.FileField(upload_to="files/")
```

A `FileField` normally stores a file name or storage reference in the
database while the storage system holds the file contents.

------------------------------------------------------------------------

# 📘 07 --- Common Field Options

Field options add rules and behavior to a selected data type.

  -----------------------------------------------------------------------------
  Option                  Meaning                 Example
  ----------------------- ----------------------- -----------------------------
  `max_length`            Maximum character       `CharField(max_length=120)`
                          length                  

  `default`               Value used when none is `IntegerField(default=0)`
                          supplied                

  `unique`                Database uniqueness     `CharField(unique=True)`
                          rule                    

  `db_index`              Index for frequent      `CharField(db_index=True)`
                          lookups or ordering     

  `editable`              Controls inclusion in   `UUIDField(editable=False)`
                          forms such as ModelForm 
  -----------------------------------------------------------------------------

### 🔴 MUST UNDERSTAND

A field type answers **what kind of data is this?**

A field option adds **rules or behavior for that data**.

For example:

``` python
sku = models.CharField(
    max_length=30,
    unique=True
)
```

`CharField` defines the type, while `max_length` and `unique` define
additional rules.

------------------------------------------------------------------------

# 📘 08 --- Controlled Values with `TextChoices`

`TextChoices` gives a field a fixed set of meaningful values.

Example:

``` python
class Category(models.TextChoices):
    LAPTOP = "laptop", "Laptop"
    PHONE = "phone", "Phone"
    ACCESSORY = "accessory", "Accessory"
```

Then:

``` python
category = models.CharField(
    max_length=20,
    choices=Category.choices,
    default=Category.ACCESSORY
)
```

### Three things to remember

  Part            Example             Meaning
  --------------- ------------------- -------------------------------------
  Stored value    `"laptop"`          Value stored in the database
  Display label   `"Laptop"`          Human-readable label shown by forms
  Code constant   `Category.LAPTOP`   Python constant used in code

### 🔴 MUST UNDERSTAND

For:

``` python
LAPTOP = "laptop", "Laptop"
```

the database stores:

``` text
laptop
```

not:

``` text
Laptop
```

`choices` guides validation and forms. It does **not** create a separate
related entity/table.

------------------------------------------------------------------------

# 📘 09 --- Automatic Primary Keys

If a model does not define a primary key, Django creates one
automatically.

``` python
class Product(models.Model):
    name = models.CharField(max_length=120)
```

Django supplies an `id` field automatically.

### `id` vs `pk`

``` text
product.id
product.pk
```

Both refer to the model's primary key when Django generated the default
`id` field.

`pk` is a generic alias for the primary key, regardless of the actual
primary-key field name.

### 🔴 MUST UNDERSTAND

Do not define an `id` field manually when Django's automatic primary key
is sufficient.

A different primary key should only be defined when the domain and
design justify it.

------------------------------------------------------------------------

# 📘 10 --- `blank=True` vs `null=True`

These options answer different questions.

### `null`

`null` controls **database storage**.

Question:

> May the database column store SQL `NULL`?

``` python
null=False
```

is the default.

Use:

``` python
null=True
```

when the absence of a value has a real meaning, especially for optional
dates or relationships.

### `blank`

`blank` controls **validation**.

Question:

> May forms and model validation accept an empty value?

``` python
blank=False
```

is the default.

Use:

``` python
blank=True
```

when the user may leave the field empty.

### Example from the day's material

``` python
bio = models.TextField(blank=True)

published_at = models.DateTimeField(
    null=True,
    blank=True
)
```

### 🔴 MUST UNDERSTAND

``` text
null  → database storage
blank → validation/forms
```

They are related to optional data, but they are **not the same
setting**.

------------------------------------------------------------------------

# 🧪 EXERCISE 1 --- BUILD THE PRODUCT MODEL

## Goal

Choose the correct Django field type for each Product attribute and
build the complete model.

### Requirements

  -------------------------------------------------------------------------------------------------------
  \#                Attribute          Requirement       Field
  ----------------- ------------------ ----------------- ------------------------------------------------
  1                 `name`             Short text,       `CharField(max_length=120)`
                                       maximum 120       
                                       characters        

  2                 `description`      Long text         `TextField()`

  3                 `price`            Money, 6 digits   `DecimalField(max_digits=8, decimal_places=2)`
                                       before and 2      
                                       after the decimal 

  4                 `stock`            Non-negative      `PositiveIntegerField(default=0)`
                                       whole number,     
                                       default 0         

  5                 `is_active`        True/False,       `BooleanField(default=True)`
                                       default True      

  6                 `available_from`   Date only         `DateField()`

  7                 `created_at`       Set once when the `DateTimeField(auto_now_add=True)`
                                       product is        
                                       created           

  8                 `product_image`    Uploaded image    `ImageField(upload_to="products/")`
  -------------------------------------------------------------------------------------------------------

### Model structure

``` python
class Product(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    available_from = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    product_image = models.ImageField(upload_to="products/")

    def __str__(self):
        return self.name
```

### Why `__str__()`?

It makes Product instances readable in places such as the Django Admin
instead of showing the generic object representation.

### Practical result

The Product model was connected to the Django project, migrated,
registered in the Admin, and verified by creating a sample **Keyboard**
product.

------------------------------------------------------------------------

# 🧪 EXERCISE 2 --- IMPROVE THE PRODUCT MODEL

Exercise 2 continued with the **same Product model** and added more
rules.

## Requirements

1.  `description`: optional, without storing `NULL`.
2.  `available_from`: optional in validation and database.
3.  `sku`: maximum 30 characters and unique.
4.  `category`: `TextChoices` for Laptop, Phone, Accessory.
5.  Default category: Accessory. Add `db_index=True` to `name`.
6.  Let Django create `id`; do not define it manually.
7.  Explain `blank=True` versus `null=True`.
8.  Explain `product.pk` and the stored value for `LAPTOP`.

## Final Product model

``` python
class Product(models.Model):

    class Category(models.TextChoices):
        LAPTOP = "laptop", "Laptop"
        PHONE = "phone", "Phone"
        ACCESSORY = "accessory", "Accessory"

    name = models.CharField(
        max_length=120,
        db_index=True
    )

    description = models.TextField(
        blank=True
    )

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    stock = models.PositiveIntegerField(
        default=0
    )

    is_active = models.BooleanField(
        default=True
    )

    available_from = models.DateField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    product_image = models.ImageField(
        upload_to="products/"
    )

    sku = models.CharField(
        max_length=30,
        unique=True
    )

    category = models.CharField(
        max_length=20,
        choices=Category.choices,
        default=Category.ACCESSORY
    )

    def __str__(self):
        return self.name
```

------------------------------------------------------------------------

# 🔎 EXERCISE 2 --- KEY CONCEPTS

### Optional `description`

``` python
description = models.TextField(blank=True)
```

This allows an empty value during validation without requiring database
`NULL`.

### Optional `available_from`

``` python
available_from = models.DateField(
    null=True,
    blank=True
)
```

Both validation and database storage allow the value to be absent.

### Unique SKU

``` python
sku = models.CharField(
    max_length=30,
    unique=True
)
```

The SKU must not be duplicated.

### Indexed name

``` python
name = models.CharField(
    max_length=120,
    db_index=True
)
```

The database can use an index to support frequent lookups or ordering.

### Category

``` python
class Category(models.TextChoices):
    LAPTOP = "laptop", "Laptop"
    PHONE = "phone", "Phone"
    ACCESSORY = "accessory", "Accessory"
```

The stored value for:

``` python
Category.LAPTOP
```

is:

``` text
laptop
```

The human-readable label is:

``` text
Laptop
```

### Primary key

No manual `id` was added.

Django creates the primary key automatically, and:

``` python
product.pk
```

refers to that primary-key value.

------------------------------------------------------------------------

# 🛠️ MIGRATIONS & VERIFICATION

Changes to the model were followed by Django's migration process.

The completed work included:

-   Creating the initial Product model migration.
-   Creating the additional migration for the Exercise 2 model changes.
-   Applying migrations successfully.
-   Running Django's system check successfully.
-   Verifying the model through Django Admin.
-   Creating and viewing a Product entry.

The migration step is important because changing `models.py` alone does
not automatically change the database structure.

------------------------------------------------------------------------

# 🧠 THEORY → PRACTICE

  Theory                   Where It Appeared in Practice
  ------------------------ ----------------------------------------
  `CharField`              Product name and SKU
  `TextField`              Product description
  `DecimalField`           Product price
  `PositiveIntegerField`   Product stock
  `BooleanField`           Product active state
  `DateField`              Product availability date
  `DateTimeField`          Product creation timestamp
  `ImageField`             Product image upload
  `blank=True`             Optional description
  `null=True`              Optional availability date in database
  `unique=True`            Unique SKU
  `db_index=True`          Indexed product name
  `TextChoices`            Product category
  `default`                Stock and category defaults
  Automatic primary key    Django-generated `id`
  `__str__()`              Readable Product names in Admin

------------------------------------------------------------------------

# 🚨 Common Mistakes to Avoid

### 1. Confusing `blank` and `null`

Remember:

``` text
blank → validation/forms
null  → database storage
```

### 2. Storing the display label for `TextChoices`

For:

``` python
LAPTOP = "laptop", "Laptop"
```

the stored value is:

``` text
laptop
```

### 3. Defining `id` unnecessarily

If Django's automatic primary key is enough, do not create another `id`
field manually.

### 4. Using the wrong numeric field

A money value should match the required precision. A stock count should
not allow negative values when the domain does not permit them.

### 5. Forgetting field options

The type alone may not satisfy the requirement.

For example:

``` python
sku = models.CharField(max_length=30, unique=True)
```

needs both the length limit and uniqueness rule.

------------------------------------------------------------------------

# ✅ Day 05 Completion Checklist

-   [x] Understand the Django model mental model.
-   [x] Understand model → table and field → column mapping.
-   [x] Understand the main text field types.
-   [x] Understand numeric field types and precision.
-   [x] Understand Boolean and date/time fields.
-   [x] Understand UUID, JSON, image, and file fields.
-   [x] Understand common field options.
-   [x] Understand `TextChoices`.
-   [x] Understand stored values vs display labels.
-   [x] Understand Django's automatic primary key.
-   [x] Understand `product.pk`.
-   [x] Understand `blank=True` vs `null=True`.
-   [x] Complete Exercise 1.
-   [x] Complete Exercise 2.
-   [x] Apply and verify migrations.
-   [x] Verify the Product model through Django Admin.

------------------------------------------------------------------------

# 🎯 Quick Review

### The five ideas to remember

**1. Model**

``` python
class Product(models.Model):
```

Defines the data structure.

**2. Field**

``` python
name = models.CharField(max_length=120)
```

Defines one piece of data and its rules.

**3. `TextChoices`**

``` python
LAPTOP = "laptop", "Laptop"
```

Separates the stored value from the display label.

**4. Optional values**

``` text
blank → validation
null  → database
```

**5. Primary key**

Django creates `id` automatically when no primary key is defined, and
`pk` is the generic way to access the primary key.

------------------------------------------------------------------------

> **Day 05 takeaway:** Good Django models start by choosing the right
> field for the meaning of the data, then adding only the rules the data
> actually needs.
