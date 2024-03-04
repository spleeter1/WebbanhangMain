from django.db import models
from django.urls import reverse
from django.conf import settings

# Create your models here.
'''
from django.db import models
from django.conf import settings
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.title
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
'''
class Category(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    slug = models.SlugField(unique=True, max_length=100, db_index=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_absolute_path(self):
        return reverse('store:product_list') + f'?category={self.id}'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=100, null=False, blank=False)
    slug = models.SlugField(unique_for_date='created')
    price = models.IntegerField(null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True,blank=True)
    #image = models.ImageField(upload_to='media/products/%Y/%m/%d/', blank=True)
    availibility = models.BooleanField(null=False, default=True) #xem san pham còn hàng hay đã hết hàng
    #det=models.TextField(null=False, blank=True)
    description = models.TextField(null=True,blank=True)
    characteristic1 = models.TextField(null=False,blank=True)
    characteristic2 = models.TextField(null=False,blank=True)
    characteristic3 = models.TextField(null=False,blank=True)
    material =  models.TextField(null=False,blank=True)
    branch= models.TextField(null=False,blank=True)
    detail=models.TextField(null=False,blank=True)
    class Meta:
        index_together = ('id', 'slug')
        ordering = ('-created',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('store:product_details', kwargs={'slug': self.slug})
