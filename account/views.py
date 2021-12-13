from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def login_request(request):
    if request.user.is_authenticated:
        return redirect("home")
        
    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request,username = username,password = password)

        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            context = {
                "error":"Username yada Password Yanlış.."
            }
            return render(request,"account/login.html",context)

    return render (request,"account/login.html")




def register_request(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        
        if password == repassword:
            if User.objects.filter(username=username).exists():
                context = {
                    "error":"Username Kullanılıyor!",
                    "username":username,
                    "email":email,
                    "firstname":firstname,
                    "lastname":lastname,
                }
                return render (request,"account/register.html",context)
            else:
                if User.objects.filter(email=email).exists():
                    context = {
                    "error":"Email Kullanılıyor!",
                    "username":username,
                    "email":email,
                    "firstname":firstname,
                    "lastname":lastname,
                }
                    return render (request,"account/register.html",context)
                else:
                    user = User.objects.create_user(username = username,email=email,password=password,first_name=firstname,last_name=lastname)
                    user.save()
                    return redirect("login")
        else:
            context = {
                    "error":"Parolalar Eşleşmiyor!",
                    "username":username,
                    "email":email,
                    "firstname":firstname,
                    "lastname":lastname,
                }
            return render (request,"account/register.html",context)


    return render (request,"account/register.html")



def logout_request(request):

    logout(request)
    return redirect ("login")
