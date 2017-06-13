from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import auth
# Create your views here.






def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('blog:index')
        else:
            return redirect('auth:login')
    else:
        return render(request, 'loginsys/login.html')



def logout(request):
    auth.logout(request)
    return redirect('auth:login')