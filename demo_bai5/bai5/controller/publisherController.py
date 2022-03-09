from django.shortcuts import render, redirect  
from bai5.forms import *
from bai5.models import * 

class PublisherController():
    def create_publisher(request):  
        if request.method == "POST":  
            form = PublisherForm(request.POST)  
            if form.is_valid():  
                try:  
                    form.save()  
                    return redirect('/publisher/show')  
                except:  
                    pass  
        else:  
            form = PublisherForm()  
        return render(request,'publisher/index.html',{'form':form})  

    def show_publisher(request):  
        publishers = Publisher.objects.all()  
        return render(request,"publisher/show.html",{'publishers':publishers})  

    def edit_publisher(request, id):  
        publisher = Publisher.objects.get(id=id)  
        return render(request,'publisher/edit.html', {'publisher':publisher})

    def update_publisher(request, id):  
        publisher = publisher.objects.get(id=id)  
        form = PublisherForm(request.POST, instance = publisher)  
        if form.is_valid():  
            form.save()  
            return redirect("/publisher/show")  
        return render(request, 'publisher/edit.html', {'publisher': publisher}) 

    def delete_publisher(request, id): 
        publisher = Publisher.objects.get(id=id)  
        bookPublishers = BookAuthor.objects.filter(publisherId = id)
        book = Book.objects.filter(id__in = bookPublishers)
        bookPublishers.delete()
        book.delete()
        publisher.delete()  
        return redirect("/publisher/show")   