from django.shortcuts import render,redirect
from django.contrib import messages
from app.models import ProductModel,UserModel

def showIndex(request):
    result= ProductModel.objects.all()
    return render(request,"index.html",{"data":result})
def admin_home(request):
    return render(request,'admin_home.html')
def admin_login_check(request):
    un = request.POST.get("t1")
    pa = request.POST.get("t2")

    if un == "Losan" and pa == "lulu":
        return redirect('admin_home')
    else:
        messages.error(request, "Invalid User")
        return redirect('admin_login')
def admin_products(request):
    result = ProductModel.objects.order_by("-no")
    return render(request, "admin_products.html", {"data": result})
def save_product(request):
    na = request.POST.get("p1")
    pr = request.POST.get("p2")
    qty = request.POST.get("p3")
    img = request.FILES["p4"]
    status = "active"
    ProductModel(name=na, price=pr, quantity=qty, photo=img, status=status).save()
    return redirect('admin_products')
def admin_login(request):
    return render(request,"admin_login.html")
def save_user(request):
    name=request.POST.get("u1")
    cno = request.POST.get("u2")
    email = request.POST.get("u3")
    password = request.POST.get("u4")
    status="pending"
    UserModel(name=name,contact=cno,email=email,password=password,status=status).save()
    return redirect('user_register')
def user_register(request):
    return render(request,'user_register.html')
def user_data(request):
    res=UserModel.objects.filter(status="pending")
    result=UserModel.objects.filter(status="active")
    return render(request,"user_data.html",{"newdata":res,"olddata":result})
def update(request):
    no=request.GET.get("no")
    UserModel.objects.filter(no=no).update(status="active")
    return redirect('user_data')
def delete(request):
    no=request.GET.get("no")
    UserModel.objects.filter(no=no).delete()
    return redirect('user_data')
def user_login(request):
    return render(request,"user_login.html")
def user_login_check(request):
    un = request.POST.get("t1")
    pa = request.POST.get("t2")
    global rec
    rec = UserModel.objects.get(email=un)
    if rec:
        if rec.status== "active":
            if rec.password==pa:
                return render(request,'user_detail.html',{"rec":rec})
            else:
                messages.error(request, "Invalid Password")
                return redirect('user_login')
        else:
            messages.error(request, "Admin approval required.")
            return redirect('user_login')
    else:
        messages.error(request, "Invalid User. You need to register.")
        return redirect('user_login')
def user_detail(request):
    return render(request,"user_detail.html",{"rec":rec})
def user_home(request):
    result = ProductModel.objects.all()
    return render(request, "user_home.html", {"data": result})

# Create your views here.
