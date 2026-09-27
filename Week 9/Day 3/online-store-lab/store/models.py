from django.db import models
class Category(models.Model):
    name = models.CharField(max_length=100)

    parent = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="children"
    )