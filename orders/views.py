from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Size, Topping, Category, Pizzatype, Pastaprice, Saladprice, Dinnerplattername, Dinnerplatterprice, Subname, Subprice, Order, Orderitem, Pizza

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})
    context = {
        "user": request.user,
        "sizes": Size.objects.all(),
        "toppings": Topping.objects.all(),
        "categories": Category.objects.all(),
        "pizzatypes": Pizzatype.objects.all(),
        "pastas": Pastaprice.objects.all(),
        "salads": Saladprice.objects.all(),
        "smalldinnerplatters": Dinnerplatterprice.objects.filter(size__name__exact="Small"),
        "largedinnerplatters": Dinnerplatterprice.objects.filter(size__name__exact="Large"),
        "smallsubs": Subprice.objects.filter(subsize__name__exact="Small"),
        "largesubs": Subprice.objects.filter(subsize__name__exact="Large")
    }
    return render(request, "orders/index.html", context)

def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "orders/login.html", {"message": "Invalid credentials"})
        
def logout_view(request):
    logout(request)
    return render(request, "orders/login.html", {"message": "Logged out."})

def register(request):
    if request.method == 'GET':
        return render(request, "orders/register.html", {"message": None})
    else:
        #try:
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        user = User.objects.create_user(username, email, password)
        user.first_name = firstname
        user.last_name = lastname
        user.save()
        return render(request, "orders/login.html", {"message": "Successfully registered " + username})
        #except:
            #return render(request, "orders/register.html", {"message": "Something went wrong with registering"})

def addtocart(request):
    order = Order.objects.filter(user__username__exact=request.user.username).first()
    if order:
        print('order found', order)
    else:
        print('no order found')
        order = Order(user=request.user)
        print(order)
        order.save()
    category = Category.objects.filter(name__exact=request.POST["categoryName"]).first()
        
    #category = request.POST["categoryName"]
    if request.POST["categoryName"] == 'Pizza':
        size = Size.objects.filter(name__exact=request.POST["firstdiv"]).first()
        pizzatype = Pizzatype.objects.filter(name__exact=request.POST["seconddiv"]).first()
        toppings = request.POST.getlist('thirddiv')
        #print(size, pizzatype, toppings)
        #categoryobject = Category(name=request.POST["categoryName"])
        pizza = Pizza(category=category, order=order, pizzasize=size, pizzatype=pizzatype)  
        pizza.save()
        for topping in toppings:
            toppingobj = Topping.objects.filter(name__exact=topping).first()
            pizza.toppings.add(toppingobj)
        #pizza.save()
        print("Pizza ordered")
        print("size = ", size)
        print("pizzatype = ", pizzatype)
        #print("toppings = ", toppings)
        
    elif request.POST["categoryName"] == 'Pasta':
        pasta = request.POST["firstdiv"]
        pastaprices = Pastaprice.objects.all()
        for pastaprice in pastaprices:
            if str(pastaprice) == pasta:
                bastapasta = pastaprice.price
        pasta = Pasta(category=category, order=order, )
        print(bastapasta)
        print("Pasta ordered")
        print("pasta = ", pasta)
    elif category == 'Sub':
        size = request.POST["firstdiv"]
        sub = request.POST["seconddiv"]
        extras = request.getlist('thirddiv')   
        print("Sub ordered")
        print("size = ", size)
        print("sub = ", sub)
        print("extras = ", extras)
    elif category == 'Salad':
        salad = request.POST["firstdiv"]      
        print("Salad ordered")
        print("salad = ", salad)  
    else:
        size = request.POST["firstdiv"]
        pizzatype = request.POST["seconddiv"]
        toppings = request.POST["thirddiv"]
        print("Pizza ordered")
        print("size = ", size)
        print("pizzatype = ", pizzatype)
        print("toppings = ", request.POST["thirddiv"])
    
    print(request.POST)
    return render(request, "orders/register.html", {"message": None})