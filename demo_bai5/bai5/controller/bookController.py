from django.shortcuts import render, redirect  
from bai5.forms import *
from bai5.models import * 

class BookController():
    def create_book(request):  
        categories = CategoryBook.objects.all()
        publishers = Publisher.objects.all()
        authors = Author.objects.all()
        if request.method == "POST":  
            form = BookForm(request.POST)  
            if form.is_valid():  
                try: 
                    form.save()
                    # book = Book.objects.create(
                    #     title=form.cleaned_data['title'],
                    #     language=form.cleaned_data['language'],
                    #     categoryID=form.cleaned_data['categoryId'],
                    #     numberOfPage=form.cleaned_data['numberOfPage'],
                    #     publicationDate=form.cleaned_data['publicationDate'],
                    #     publisherId=form.cleaned_data['publisherId'],
                    #     author=form.cleaned_data['author']
                    # ) 
                    return redirect('/book/show')  
                except:  
                    pass  
        else: 
            form = BookForm() 
 
        return render(request,'book/index.html',
        {
            'form':form,
            'categories':categories,
            'publishers':publishers,
            'authors':authors
        })  

    def show_book(request):
        books = Book.objects.select_related('categoryBookId', 'publisherId')
        authors = Author.objects.all()
        return render(request,"book/show.html",
        {
            'books':books,
            'authors':authors
        })  

    def edit_book(request, id):  
        book = Book.objects.select_related('categoryBookId', 'publisherId').filter(id = id)
        return render(request,'book/edit.html', 
        {
            'book':book,
        })

    def update_book(request, id):  
        book = Book.objects.get(id=id)  
        form = BookForm(request.POST, instance = book)  
        if form.is_valid():  
            form.save()  
            return redirect("/book/show")  
        return render(request, 'book/edit.html', {'book': book}) 

    def delete_book(request, id): 
        book = Book.objects.get(id=id)  
        book.delete()  
        return redirect("/book/show")   
    