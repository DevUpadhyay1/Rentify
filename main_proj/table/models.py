from django.db import models
from accounts.models import CustomeUser
from django.utils.html import mark_safe
# Create your models here.

STATUS_CHOICE = (
    ("process","processing"),
    ("confirmed","confirmed")
)

STATUS = (
    ("in_review","In Review"),
    ("rejected","Rejected"),   
)

RATING = (
    ("1","★☆☆☆☆"),
    ("2","★★☆☆☆"),
    ("3","★★★☆☆"),
    ("4","★★★★☆"),
    ("5","★★★★★")
)

def user_directory_path(instance,filename):
    return 'user_{0}/{1}'.format(instance.user.id,filename)

class Category(models.Model):
    # cid = ShortUUIDField(unique=True,length=10,max_length=30,prefix="cat",alphabet="abcdefghijk1234")
    cid = models.AutoField(primary_key=True)
    
    user = models.ForeignKey(CustomeUser,on_delete=models.SET_NULL,null=True)

    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="category")

    class Meta:
        verbose_name_plural = "Categories"

    def category_image(self):
        return mark_safe('<img srs = "%s" />' % (self.image.url))
    
    def __str__(self):
        return self.title

class Tags(models.Model):
    pass

class Renter(models.Model):
    # rid  = ShortUUIDField(unique=True,length=10,max_length=30,prefix="ven",alphabet="abcdefghijk1234")
    rid = models.AutoField(primary_key=True)

    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to=user_directory_path)
    descrption = models.TextField(null=True,blank=True)

    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)

    user = models.ForeignKey(CustomeUser,on_delete=models.SET_NULL,null=True)

    class Meta:
        verbose_name_plural = "Renter"

    def renter_image(self):
        return mark_safe('<img srs = "%s" />' % (self.image.url))
    
    def __str__(self):
        return self.title

class Product(models.Model):
    # pid = ShortUUIDField(unique=True,length=10,max_length=30,alphabet="abcdefghijk1234")
    pid = models.AutoField(primary_key=True)

    user = models.ForeignKey(CustomeUser,on_delete=models.SET_NULL,null=True)
    Category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)

    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to=user_directory_path)
    descrption = models.TextField(null=True,blank=True,default="This is a product")

    price = models.DecimalField(max_digits=10,decimal_places=2)

    specification =  models.TextField(null=True,blank=True)
    tags = models.ForeignKey(Tags,on_delete=models.SET_NULL,null=True)

    product_status = models.CharField(choices=STATUS,max_length=10)

    status = models.BooleanField(default=True)

    sdate = models.DateField(auto_now_add=True)
    edate = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Product"

    def Product_image(self):
        return mark_safe('<img srs = "%s" />' % (self.image.url))
    
    def __str__(self):
        return self.title
    
class ProductImages(models.Model):
    images = models.ImageField(upload_to="prduct-images")
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    Category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Product_images"


class ProductReview(models.Model):
    user = models.ForeignKey(CustomeUser,on_delete=models.SET_NULL,null=True)
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    review = models.TextField()
    Rating = models.IntegerField(choices=RATING,default=None)
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Product Review"

    def __str__(self):
        return self.product.title
    
    def get_rating(self):
        return self.Rating
    
class Product_availibility(models.Model):
    # aid = ShortUUIDField(unique=True,length=10,max_length=30,alphabet="abcdefghijk1234")
    
    renter = models.ForeignKey(Renter,on_delete=models.SET_NULL,null=True)
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)

    availibility = models.BooleanField(default =False)

    sdate = models.DateField(auto_now_add=True)
    edate = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Product Avilibility"


class wishlist(models.Model):
    user = models.ForeignKey(CustomeUser,on_delete=models.SET_NULL,null=True)
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "wishlists"

    def __str__(self):
        return self.product.title
    
class Address(models.Model):
    user = models.ForeignKey(CustomeUser,on_delete=models.SET_NULL,null=True)
    address = models.CharField(max_length=100,null=True)
    status = models.BooleanField(default = False)

    class Meta:
        verbose_name_plural = "Address"

