from django.db import models
from django.conf import settings

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name="orders")
    totalamount = models.DecimalField(default=0, max_digits=7, decimal_places=2)
    placed = models.BooleanField(default=False)
    done = models.BooleanField(default=False)

    def __str__(self):
        orderitems = Orderitem.objects.filter(order=self.id)
        #returnstr = ""
        #for orderitem in orderitems:
        #    returnstr += str(orderitem) + " \n"
        #pizzas = Pizza.objects.filter(order=self.id)
        returnstr = "order for " + str(self.user.username) + ": " + str(len(orderitems)) + " items, total = $ " + str(self.totalamount)
        #for pizza in pizzas:
        #    returnstr += str(pizza) + " \n"
        return returnstr


class Orderitem(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="orderitems")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, related_name="orderitems")


class Pizzatype(models.Model):
    name = models.CharField(max_length=64)
     
    def __str__(self):
        return f"{self.name}"

class Size(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}"

class Topping(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}"

class Pizza(Orderitem):
    pizzatype = models.ForeignKey(Pizzatype, on_delete=models.CASCADE, related_name="pizzas")
    pizzasize = models.ForeignKey(Size, on_delete=models.CASCADE, related_name="pizzas")    
    toppings = models.ManyToManyField(Topping, blank=True, related_name="pizzas")
    price = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        toppingsself = self.toppings.all()        
        returnstr = ""
        for toppingself in toppingsself:
            returnstr += " " + str(toppingself)
        return f"{self.pizzatype} {self.pizzasize} {returnstr}"


class Maxtopping(models.Model):
    name = models.CharField(max_length=64)
    number = models.SmallIntegerField()

    def __str__(self):
        return f"{self.name}"

class Pizzaprice(models.Model):
    pizzatype = models.ForeignKey(Pizzatype, on_delete=models.CASCADE, related_name="pizzaprices")
    pizzasize = models.ForeignKey(Size, on_delete=models.CASCADE, related_name="pizzaprices")
    maxtoppings = models.ForeignKey(Maxtopping, on_delete=models.CASCADE, related_name="pizzaprices")
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.pizzatype} {self.pizzasize} {self.maxtoppings} ${self.price}"

class Pasta(Orderitem):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.name} ${self.price}"

class Pastaprice(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.name} ${self.price}"

class Salad(Orderitem):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return f"{self.name} ${self.price}"

class Saladprice(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return f"{self.name} ${self.price}"

class Subname(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

class Sub(Orderitem):
    name = models.ForeignKey(Subname, on_delete=models.CASCADE, related_name="subs")
    size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name="subs")
    extramushrooms = models.BooleanField(default=False)
    extragreenpeppers = models.BooleanField(default=False)
    extraunions = models.BooleanField(default=False)
    extracheese = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} {self.size}"


class Subprice(models.Model):
    subname = models.ForeignKey(Subname, on_delete=models.CASCADE, related_name="subprices")
    subsize = models.ForeignKey(Size, on_delete=models.CASCADE, related_name="subprices")
    price = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return f"Sub {self.subname} {self.subsize} ${self.price}"

class Extrassubprice(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return f"{self.name} ${self.price}"

class Dinnerplattername(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"Dinner Platter {self.name}"

class Dinnerplatter(Orderitem):
    name = models.ForeignKey(Dinnerplattername, on_delete=models.CASCADE, related_name="dinnerplatters")
    size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name="dinnerplatters")
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.name} {self.size} ${self.price}" 
        
class Dinnerplatterprice(models.Model):
    name = models.ForeignKey(Dinnerplattername, on_delete=models.CASCADE, related_name="dinnerplatterprices")
    size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name="dinnerplatterprices")
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.name} {self.size} ${self.price}"
