from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=225)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=225)
    slug = models.SlugField(max_length=225)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="products", blank=True, null=True)

    def __str__(self):
        return f"Product Name: {self.name} Product Category: {self.category}"

    def get_absolute_url(self):
        return reverse(
            "products:product_detail", kwargs={"pk": self.pk, "slug": self.slug}
        )
