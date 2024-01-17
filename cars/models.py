from django.db import models
from django.urls import reverse
# Create your models here.
class Car(models.Model):
    title = models.CharField(max_length=255, verbose_name='Full title')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True)
    brand = models.TextField(blank=True)
    model = models.TextField(blank=True)
    # color = models.CharField(max_length=30)
    version = models.CharField(max_length=30, null=True)
    power = models.CharField(max_length=30, null=True)
    drive = models.CharField(max_length=30, null=True)
    acceleration = models.CharField(max_length=30, null=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Category')



    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Cars'
        verbose_name_plural = 'Cars'
        ordering = ['time_create', 'title'] #сортировка

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория" )
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['id']