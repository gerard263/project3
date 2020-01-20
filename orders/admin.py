from django.contrib import admin

from .models import Pizza,Pizzaprice,Size,Topping,Pizzatype,Pastaprice,Category,Orderitem,Order,Maxtopping,Saladprice,Subname,Subprice,Sub,Dinnerplattername,Dinnerplatterprice

# Register your models here.

admin.site.register(Pizza)
admin.site.register(Pizzaprice)
admin.site.register(Size)
admin.site.register(Topping)
admin.site.register(Pizzatype)
admin.site.register(Pastaprice)

admin.site.register(Category)
admin.site.register(Orderitem)
admin.site.register(Order)
admin.site.register(Maxtopping)
admin.site.register(Saladprice)
admin.site.register(Subname)
admin.site.register(Subprice)
admin.site.register(Sub)
admin.site.register(Dinnerplattername)
admin.site.register(Dinnerplatterprice)