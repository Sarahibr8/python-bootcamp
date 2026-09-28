from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=120)
    sku = models.CharField(max_length=30, unique=True)
    description = models.TextField(blank=True)

    class Category(models.TextChoices):
        ELECTRONICS = "electronics", "Electronics"
        FOOD = "food", "Food"
        ACCESSORY = "accessory", "Accessory"

    category = models.CharField(
        max_length=20,
        choices=Category.choices,
        default=Category.ACCESSORY
    )

    stock = models.PositiveIntegerField(default=0)

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.sku})"

    def is_available(self):
        return self.is_active and self.stock > 0

    def inventory_value(self):
        return self.price * self.stock
        
    class Meta:
        ordering = ["category", "name"]
        verbose_name = "Product"
        verbose_name_plural = "Products"

        indexes = [
            models.Index(
                fields=["category", "is_active"],
                name="product_cat_active_idx",
            )
        ]

        constraints = [
            models.CheckConstraint(
                condition=models.Q(price__gte=0),
                name="product_price_gte_0",
            ),
            models.CheckConstraint(
                condition=models.Q(stock__gte=0),
                name="product_stock_gte_0",
            ),
        ]