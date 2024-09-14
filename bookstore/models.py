from django.db import models

# Create your models here.

class Category(models.Model):
    categoryname = models.CharField(max_length=40)

    def __str__(self):
        return self.categoryname

class City(models.Model):
    cityname = models.CharField(max_length=40)

    def __str__(self):
        return self.cityname


class Author(models.Model):
    authorname = models.CharField(max_length=50)
    authordob = models.DateField()
    authorgender = models.CharField(max_length=20)
    authoremail = models.CharField(max_length=50)
    authorphone = models.CharField(max_length=10)
    authorcity = models.ForeignKey(City,on_delete=models.CASCADE)

    def __str__(self):
        return self.authorname
class Book(models.Model):
    bookname = models.CharField(max_length=50)
    bookdescription = models.CharField(max_length=500)
    bookpublishedon = models.DateField()
    bookprice = models.IntegerField(default=0)
    bookauthor = models.ForeignKey(Author,on_delete=models.CASCADE)
    bookcategory = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.bookname



