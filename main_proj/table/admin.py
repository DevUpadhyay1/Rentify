from django.contrib import admin
from table.models import *
# Register your models here.

class ProductImageAdmin(admin.TabularInline):
    model = ProductImages

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]
    list_display = ['user','title','Product_image','price','product_status']

class CategoryAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]
    list_display = ['user','title','category_image']

class RenterAdmin(admin.ModelAdmin):
    list_display = ['title','renter_image']

class availibilityAdmin(admin.ModelAdmin):
    list_display = ['renter','availibility','sdate','edate']

class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['user','product','review','Rating']

class wishlistAdmin(admin.ModelAdmin):
    list_display = ['user','product','date']

class AddressAdmin(admin.ModelAdmin):
    list_display = ['user','address','status']

admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Renter,RenterAdmin)
admin.site.register(Product_availibility,availibilityAdmin)
admin.site.register(ProductReview,ProductReviewAdmin)
admin.site.register(wishlist,wishlistAdmin)
admin.site.register(Address,AddressAdmin)