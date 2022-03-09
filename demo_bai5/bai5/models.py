from django.db import models

class Author(models.Model):  
    id = models.AutoField(primary_key='true') 
    name = models.CharField(max_length=255)  
    biography = models.CharField(max_length=255)  
    class Meta:  
        db_table = "author"  

class CategoryBook(models.Model):  
    id = models.AutoField(primary_key='true') 
    name = models.CharField(max_length=255)   
    class Meta:  
        db_table = "categorybook"

class Publisher(models.Model):  
    id = models.AutoField(primary_key='true') 
    name = models.CharField(max_length=255)  
    address = models.CharField(max_length=255)    
    class Meta:  
        db_table = "publisher"

class Book(models.Model):  
    id = models.AutoField(primary_key='true') 
    title = models.CharField(max_length=255)  
    language = models.CharField(max_length=255)
    numberOfPage = models.IntegerField()
    publicationDate = models.DateField()
    categoryBookId = models.ForeignKey(CategoryBook,on_delete=models.CASCADE)
    publisherId = models.ForeignKey(Publisher,on_delete=models.CASCADE)
    author = models.ManyToManyField(Author)
    class Meta:  
        db_table = "book"

