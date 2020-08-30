from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def login(request):
    
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect(admine)
        else:
             return redirect(home)
    
    
    elif request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
          if username == "admin" and password=='admin':
                auth.login(request,user)
                return redirect(admine)
          else:
                auth.login(request,user)
                return redirect(home)
        else:
            messages.info(request,'**invalid credentions')
            return HttpResponseRedirect(request.path_info)
    else:
        return render(request,'login.html')

@login_required(login_url='/')
def admine(request):
    user=User.objects.filter(is_superuser=False)
    return render(request,'admin.html',{'user':user})
@login_required(login_url='/')
def home(request):
    return render(request,'home.html')

def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        dicti = {"first_name":first_name,"last_name":last_name,"username":username,"email":email}
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already taken')
                return render(request, "register.html", dicti)
            elif User.objects.filter(email=email).exists():
                 messages.info(request,'email already taken')
                 return render(request, "register.html", dicti)

            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
                user.save();
                return redirect(login)
        else:
             messages.info(request,'password  incorrect')
             return render(request, "register.html", dicti)


    else:
        return render(request,'register.html')
        

def logout(request):
    auth.logout(request)
    return redirect(login)


def delete(request,id):
     
     user=User.objects.get(id=id)
     user.delete()
     return redirect(admine)

def update(request,id):
    user=User.objects.get(id=id)
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        user.first_name=first_name
        user.last_name=last_name
        user.email=email
        user.save();
        return redirect(admine)


    else:
        return render(request,'update.html',{'user':user})


def search (request):
    if request.method=='POST':
        username=request.POST['username']
        if User.objects.filter(username= username).exists():
            user=User.objects.get(username=username)
            return render(request,'search.html',{'user':user})
        else:
            messages.info(request,'NO SUCH A USERNAME ')
            return render(request,'nosearch.html')
    messages.info(request,'PLEASE put something ')      
    return render(request,'search.html')


def addusr(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        dicti = {"first_name":first_name,"last_name":last_name,"username":username,"email":email}
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already taken',dicti)
                return HttpResponseRedirect(request.path_info)
            elif User.objects.filter(email=email).exists():
                 messages.info(request,'email already taken',dicti)
                 return HttpResponseRedirect(request.path_info)

            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
                user.save();
                return redirect(admine)
        else:
             messages.info(request,'password  incorrect')
             return render(request, "addusr.html",dicti)
    else:
        return render(request,'addusr.html')
