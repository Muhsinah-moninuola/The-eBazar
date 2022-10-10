from django.contrib import admin
from MarketPlace.models import *
# Register your models here.

admin.site.register(userRegister)
admin.site.register(VendorRegister)
admin.site.register(ProductCategory)
admin.site.register(product)
admin.site.register(Reviews)



