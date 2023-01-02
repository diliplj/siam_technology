from unicodedata import category
from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
DATAMODE_CHOICES = (("A", "ACTIVE"), ("IN", "Inactive"),("D","Deleted"))
class Category(models.Model):
    category_name = models.CharField(max_length=200,null=True)
    slug = models.CharField(max_length=255,null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=15)
    updated_by = models.CharField(max_length=15)
    datamode = models.CharField(max_length=8, default='A', choices=DATAMODE_CHOICES, db_index=True)

    def __str__(self):
        return self.category_name

    def save(self, *args, **kwargs):
        super(Category, self).save(*args, **kwargs)
        if self.category_name:
            self.slug = slugify(self.category_name)
            super(Category, self).save()    

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200, null=True)
    slug = models.CharField(max_length=255,null=True)
    product_model = models.CharField(blank=True, null=True, max_length=15)
    product_price = models.IntegerField(blank=True, null=True)
    product_offer = models.CharField(max_length=10, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=10)
    updated_by = models.CharField(max_length=10)
    datamode = models.CharField(max_length=8, default='A', choices=DATAMODE_CHOICES, db_index=True)

    def __str__(self):
        return self.product_name +"  "+ str(self.product_price)

    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)
        if self.product_name:
            self.slug = slugify(self.product_name)
            super(Product, self).save()       