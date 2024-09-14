from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.cache import never_cache

from bookstore.models import Author, City, Category, Book


# Create your views here.
@never_cache
def home_fun(request):
    return render(request, 'home.html')
@login_required
@never_cache
def add_author(request):
    if request.method == 'GET':
        cities = City.objects.all()
        data = {"cities": cities}
        return render(request, 'addauthor.html', data)

    else:
        a = Author()
        a.authorname = request.POST['auth_name']
        a.authordob = request.POST['auth_dob']
        a.authorgender = request.POST['ddlgender']
        a.authoremail = request.POST['auth_email']
        a.authorphone = request.POST['auth_phone']
        a.authorcity = City.objects.get(cityname=request.POST['ddlcity'])
        a.save()
        return redirect('displayauthor')

@never_cache
def display_author(request):
    authors = Author.objects.all()
    data1 = {"authors": authors}
    return render(request, "displayauthor.html", data1)

@never_cache
def del_author(request, id):
    a = Author.objects.get(id=id)
    a.delete()
    return redirect('displayauthor')

@login_required
def edit_author(request, id):
    a1 = Author.objects.get(id=id)
    a2 = City.objects.all()
    if request.method == "GET":
        data3 = {'author': a1, 'city': a2}
        return render(request, 'edit_author.html', data3)
    else:
        a1.authorname = request.POST['auth_name']
        a1.authordob = request.POST['auth_dob']
        a1.authorgender = request.POST['ddlgender']
        a1.authoremail = request.POST['auth_email']
        a1.authorphone = request.POST['auth_phone']
        a1.authorcity = City.objects.get(cityname=request.POST['ddlcity'])
        a1.save()
        return redirect('displayauthor')
@never_cache
@login_required
def add_book(request):
    if request.method == 'GET':
        authors = Author.objects.all()
        categories = Category.objects.all()
        data = {"authors": authors,'categories':categories}
        return render(request, 'addbook.html', data)

    else:
        b = Book()
        b.bookname = request.POST['book_name']
        b.bookdescription = request.POST['book_descp']
        b.bookpublishedon = request.POST['bookpub']
        b.bookprice = request.POST['book_price']
        b.bookauthor = Author.objects.get(authorname=request.POST['book_author'])
        b.bookcategory = Category.objects.get(categoryname=request.POST['book_category'])
        b.save()
        return redirect('displaybook')

@never_cache
def display_book(request):
    book = Book.objects.all()
    data = {'book':book}
    return render(request,'displaybook.html',data)

@login_required
def edit_book(request,id):
    book = Book.objects.get(id=id)
    author = Author.objects.all()
    category = Category.objects.all()
    data = {"book":book, "author":author, "category":category}
    if request.method == "GET":
        return render(request, 'editbook.html', data)

    else:
        b2 = Book()
        b2.bookname = request.POST['book_name']
        b2.bookdescription = request.POST['book_descp']
        b2.bookpublishedon = request.POST['bookpub']
        b2.bookprice = request.POST['book_price']
        b2.bookauthor = Author.objects.all(authorname=request.POST['book_author'])
        b2.bookcategory = Category.objects.all(categoryname=request.POST['book_category'])
        b2.save()
        return redirect('displaybook')

@login_required
def del_book(request, id):
    a = Book.objects.get(id=id)
    a.delete()
    return redirect('displaybook')

@never_cache
def login_fun(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        uname = request.POST['tbusername']
        pword = request.POST['tbpass1']
        user = authenticate(username=uname,password=pword)
        if user is not None:
            login(request,user)
            request.session['name'] = user.username
            return redirect('home')
        else:
            return redirect('login')

@never_cache
def register_fun(request):
    if request.method == 'GET':
     return render(request,'register.html')
    else:
        p1 = request.POST['tbpass1']
        p2 = request.POST['tbpass2']
        un = request.POST['tbusername']
        em = request.POST['tbemail']
        if p1 == p2:
            u = User.objects.create_superuser(un,em,p1)
            u.save()
            return redirect('login')
        else:
            return redirect('register')

@never_cache
def logout_fun(request):
    del request.session['name']
    logout(request)
    return redirect('login')