from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache


# Create your views here.
@never_cache
def home(request):
    try:
        a = request.session['name']
        data = {'a':a}
        return render(request,'account/home.html',data)
    except Exception:
        return render(request,'account/home.html')


# def login_fun(request):
#     if request.method == 'GET':
#         return render(request,'account/login.html')
#     else:
#         uname = request.POST['tbusername']
#         pword = request.POST['tbpass1']
#         user = authenticate(username=uname,password=pword)
#         if user is not None:
#             login(request,user)
#             request.session['name'] = user.username
#             return redirect('home')
#         else:
#             return redirect('login')



# def register_fun(request):
#     if request.method == 'GET':
#      return render(request,'account/register.html')
#     else:
#         p1 = request.POST['tbpass1']
#         p2 = request.POST['tbpass2']
#         un = request.POST['tbusername']
#         em = request.POST['tbemail']
#         if p1 == p2:
#             u = User.objects.create_superuser(un,em,p1)
#             u.save()
#             return redirect('login')
#         else:
#             return redirect('register')


# def logout_fun(request):
#     del request.session['name']
#     logout(request)
#     return redirect('login')