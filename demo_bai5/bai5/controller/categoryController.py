from django.shortcuts import render, redirect  
from bai5.forms import *
from bai5.models import * 

class CategoryController():
    def create_category(request):  
        if request.method == "POST":  
            form = CategoryBookForm(request.POST)  
            if form.is_valid():  
                try:  
                    form.save()  
                    return redirect('/category/show')  
                except:  
                    pass  
        else:  
            form = CategoryBookForm()  
        return render(request,'category/index.html',{'form':form})  

    def show_category(request):  
        categorys = CategoryBook.objects.all()  
        return render(request,"category/show.html",{'categorys':categorys})  

    def edit_category(request, id):  
        category = CategoryBook.objects.get(id=id)  
        return render(request,'category/edit.html', {'category':category})

    def update_category(request, id):  
        category = CategoryBook.objects.get(id=id)  
        form = CategoryBookForm(request.POST, instance = category)  
        if form.is_valid():  
            form.save()  
            return redirect("/category/show")  
        return render(request, 'category/edit.html', {'category': category}) 

    def delete_category(request, id): 
        category = CategoryBook.objects.get(id=id)  
        book = Book.objects.filter(categoryId = id)
        book.delete()
        category.delete()  
        return redirect("/category/show")   