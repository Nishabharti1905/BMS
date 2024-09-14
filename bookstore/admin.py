from django.contrib import admin

from bookstore.models import Category, Book, City, Author

# Register your models here.
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(City)
admin.site.register(Book)