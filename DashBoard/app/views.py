from django.shortcuts import render,redirect
from .models import Manager
from .models import JobList
# Create your views here.

def Login(request):
    #global LoginEmail
    if request.method=="POST":
        #print(request.POST.get("Email"))
        users =Manager.objects.all()
        print(users)
        for user in users:
            if user.Email==request.POST.get("Email") and user.Password== request.POST.get("Password"):
                #LoginEmail=user.Email
                return redirect("/Home/")
            
        else:
            wrong="Email Id or Password is wrong. Try again!"
            return render(request,"Login.html",{"wrong":wrong})

    return render(request,"Login.html")
def Home(request):
    #print(LoginEmail)
    if True: #LoginEmail:
        alljob=JobList.objects.all()
        return render(request,"Home.html",{"alljob":alljob})
    else:
        return redirect("/Login/")


def Apply(request,id):
    print(id)
    job=JobList.objects.get(id=id)
    return render(request,"Apply.html",{"job":job} )

def Success(request):
    return render(request,"Success.html")
    