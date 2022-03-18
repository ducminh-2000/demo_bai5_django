from MySQLdb import Timestamp
from django.db import models

class Author(models.Model):  
    id = models.AutoField(primary_key='true') 
    name = models.CharField(max_length=255)  
    biography = models.CharField(max_length=255) 

    def __str__(self):
        return self.name
    class Meta:  
        db_table = "author"  

class CategoryBook(models.Model):  
    id = models.AutoField(primary_key='true') 
    name = models.CharField(max_length=255) 
    def __str__(self):
        return self.name  
    class Meta:  
        db_table = "categorybook"

class Publisher(models.Model):  
    id = models.AutoField(primary_key='true') 
    name = models.CharField(max_length=255)  
    address = models.CharField(max_length=255)  
    def __str__(self):
        return self.name   
    class Meta:  
        db_table = "publisher"

class Book(models.Model):  
    id = models.AutoField(primary_key='true') 
    title = models.CharField(max_length=255)  
    language = models.CharField(max_length=255)
    numberOfPage = models.IntegerField()
    publicationDate = models.DateField(auto_created=True)
    categoryBookId = models.ForeignKey(CategoryBook,on_delete=models.CASCADE)
    publisherId = models.ForeignKey(Publisher,on_delete=models.CASCADE)
    author = models.ManyToManyField(Author)
    def __str__(self):
        return self.title
    class Meta:  
        db_table = "book"

class MobilePhone(models.Model):  
    id = models.AutoField(primary_key='true') 
    name = models.CharField(max_length=255)  
    brand = models.CharField(max_length=255)
    ram = models.CharField(max_length=255)  
    cpu = models.CharField(max_length=255)
    screen = models.CharField(max_length=255)  
    rearCamera = models.CharField(max_length=255)
    frontCamera = models.CharField(max_length=255)  
    color = models.CharField(max_length=255)
    ops = models.CharField(max_length=255)  
    battery = models.CharField(max_length=255)
    warranty = models.CharField(max_length=255)  
    size = models.CharField(max_length=255)
    displayType = models.CharField(max_length=255)  
    def __str__(self):
        return self.name
    class Meta:  
        db_table = "mobilephone"

class CPU(models.Model):
    id = models.AutoField(primary_key='true')
    name = models.CharField(max_length=255)  
    techType = models.CharField(max_length=255)
    typeCpu = models.CharField(max_length=255)  
    speed = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)  
    def __str__(self):
        return self.name
    class Meta:
        db_table = "cpu"

class VGA(models.Model):
    id = models.AutoField(primary_key='true')
    name = models.CharField(max_length=255)  
    vram = models.CharField(max_length=255)
    tech = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)  
    def __str__(self):
        return self.name
    class Meta:
        db_table = "vga"

class Laptop(models.Model):
    id = models.AutoField(primary_key='true')
    name = models.CharField(max_length=255)  
    screen = models.CharField(max_length=255)
    battery = models.CharField(max_length=255)  
    weight = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    material = models.CharField(max_length=255)  
    warranty = models.CharField(max_length=255)
    ops = models.CharField(max_length=255)
    size = models.CharField(max_length=255)   
    ram =  models.CharField(max_length=255) 
    vga = models.ForeignKey(VGA, on_delete=models.CASCADE)
    cpu = models.ForeignKey(CPU, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    class Meta:
        db_table = "laptop"

