from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"


class Orderitem(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="orderitems")

class Order(models.Model):
    orderitems = models.ManyToManyField(Orderitem, blank=True, related_name="orderitems")
    totalamount = models.IntegerField()

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

    def __str__(self):
        return f"{self.pizzatype} {self.pizzasize}"

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

class Pastaprice(Orderitem):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.name} ${self.price}"

class Saladprice(Orderitem):
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

    def __str__(self):
        return f"{self.name} {self.size}"


class Subprice(models.Model):
    subname = models.ForeignKey(Subname, on_delete=models.CASCADE, related_name="subprices")
    subsize = models.ForeignKey(Size, on_delete=models.CASCADE, related_name="subprices")
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.subname} {self.subsize} ${self.price}"
        
class Dinnerplattername(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

class Dinnerplatterprice(models.Model):
    name = models.ForeignKey(Dinnerplattername, on_delete=models.CASCADE, related_name="dinnerplatters")
    size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name="dinnerplatters")
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.name} {self.size}"
