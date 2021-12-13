from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class Categories(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(null=False,unique=True,db_index=True,editable=False,blank=True)

    def save(self,*args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.name



class Blog(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to ="blogs")
    description = RichTextField()
    is_active = models.BooleanField(default=False)
    is_home = models.BooleanField(default=False)
    slug = models.SlugField(null=False,blank=True,unique=True,db_index=True,editable=False)
    categories = models.ManyToManyField(Categories,blank=True)
    #ADMİN PANEL TİTLE GÖSTERMEK İÇİN , AYRICA ADMİN.PY'da ayarlamalıyız
    def __str__(self):
        return self.title
    #SLUG FUNC
    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

