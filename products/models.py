from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=50)
    friendly_name = models.CharField(max_length=50, null=True, blank=True)
    is_active = models.BooleanField(null=False, blank=False)

    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    has_size_s = models.BooleanField(default=False,null=True, blank=True)
    has_size_m = models.BooleanField(default=False,null=True, blank=True)
    has_size_l = models.BooleanField(default=False,null=True, blank=True)
    has_size_xl = models.BooleanField(default=False,null=True, blank=True)
    has_size_96 = models.BooleanField(default=False,null=True, blank=True)
    has_size_120 = models.BooleanField(default=False,null=True, blank=True)
    has_size_140 = models.BooleanField(default=False,null=True, blank=True)
    color = models.CharField(max_length=20, default=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    line_model = models.CharField(max_length=20, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    is_active = models.BooleanField(null=False, blank=False, default=True)

    def __str__(self):
        return self.name
