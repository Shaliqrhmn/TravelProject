from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        re_pass = request.POST['re_pass']
        if password == re_pass:
            if User.objects.filter(username=username).exists:
                messages.info(request, 'Username Exist')
            elif User.objects.filter(email=email).exists:
                messages.info(request, 'Email Exist')
            else:
                user = User.objects.create_user(username=username, first_name=fname, last_name=lname, email=email, password=password,)
                user.save()
        else:
            return redirect('/')
    return render(request, 'register.html')
