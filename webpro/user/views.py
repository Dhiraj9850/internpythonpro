from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages 
from django.contrib.auth.models import User 
from django.contrib.auth  import authenticate,login,logout

# Create your views here.
def index(request):
    return render(request, 'user/index.html')

def handleSignup(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        monum = request.POST['monum']
        password = request.POST['password']
        dob = request.POST['dob']
        

      
        # create the user
        myuser = User.objects.create_user(email,password)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.dob = dob
        myuser.save()
        messages.success(request,f"Congratulations, {myuser} your Morzilo account is created successfully!")
        return redirect('/')
    else:
        return HttpResponse('404-page not found')

def handleLogin(request):
    if request.method =='POST':
        # Get the post parameters
        loginemail=request.POST['loginemail']
        loginpassword=request.POST['loginpassword']

        user=authenticate(email= loginemail, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, f"{user} ,Successfully Logged In")
            return redirect('/')
        else:
            messages.error(request, "Invalid user! Please try again after some time")
            return redirect('/')

    return HttpResponse("404- Not found")
   

    return HttpResponse("login")
def handlelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/')

 