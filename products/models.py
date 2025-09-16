from django.db import models
import uuid


class ProductManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_delete=False)


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255)
    shop = models.CharField(max_length=255)
    price = models.IntegerField()
    sku = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100)
    discount = models.IntegerField(default=0)
    category = models.CharField(max_length=100)
    stock = models.PositiveIntegerField(default=0)
    is_available = models.BooleanField(default=True)
    picture = models.URLField(max_length=500, blank=True, null=True)
    is_delete = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ProductManager()
    all_objects = models.Manager()

    def delete(self, using=None, keep_parents=False):
        self.is_delete = True
        self.save()
