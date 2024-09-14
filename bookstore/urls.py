from django.urls import path

from bookstore import views

urlpatterns = [
    path('', views.home_fun, name='home'),
    path('addauthor', views.add_author, name='addauthor'),
    path('disauthor', views.display_author, name='displayauthor'),
    path('delauthor/<int:id>', views.del_author, name='deleteauthor'),
    path('editauthor/<int:id>', views.edit_author, name='editauthor'),
    path('addbook', views.add_book, name='addbook'),
    path('disbook', views.display_book, name='displaybook'),
    path('editbook/<int:id>', views.edit_book, name='editbook'),
    path('delbook/<int:id>', views.del_book, name='deletebook'),
    path('login', views.login_fun, name='login'),
    path('register', views.register_fun, name='register'),
    path('logout', views.logout_fun, name='logout')

]
