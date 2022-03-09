# from django.shortcuts import render, redirect  
# from bai5.forms import *
# from bai5.models import * 
# # Create your views here.  
# def create_author(request):  
#     if request.method == "POST":  
#         form = AuthorForm(request.POST)  
#         if form.is_valid():  
#             try:  
#                 form.save()  
#                 return redirect('/author/show')  
#             except:  
#                 pass  
#     else:  
#         form = AuthorForm()  
#     return render(request,'author/index.html',{'form':form})  

# def show_author(request):  
#     authors = Author.objects.all()  
#     return render(request,"author/show.html",{'authors':authors})  

# def edit_author(request, id):  
#     author = Author.objects.get(id=id)  
#     return render(request,'author/edit.html', {'author':author})

# def update_author(request, id):  
#     author = author.objects.get(id=id)  
#     form = AuthorForm(request.POST, instance = author)  
#     if form.is_valid():  
#         form.save()  
#         return redirect("/author/show")  
#     return render(request, 'author/edit.html', {'author': author}) 

# def delete_author(request, id):  
#     author = Author.objects.get(id=id)  
#     author.delete()  
#     return redirect("/author/show") 

# def create_publisher(request):  
#     if request.method == "POST":  
#         form = PublisherForm(request.POST)  
#         if form.is_valid():  
#             try:  
#                 form.save()  
#                 return redirect('/publisher/show')  
#             except:  
#                 pass  
#     else:  
#         form = PublisherForm()  
#     return render(request,'publisher/index.html',{'form':form})  

# def show_publisher(request):  
#     publishers = Publisher.objects.all()  
#     return render(request,"publisher/show.html",{'publishers':publishers})  

# def edit_publisher(request, id):  
#     publisher = Publisher.objects.get(id=id)  
#     return render(request,'publisher/edit.html', {'publisher':publisher})

# def update_publisher(request, id):  
#     publisher = publisher.objects.get(id=id)  
#     form = PublisherForm(request.POST, instance = publisher)  
#     if form.is_valid():  
#         form.save()  
#         return redirect("/publisher/show")  
#     return render(request, 'publisher/edit.html', {'publisher': publisher}) 

# def delete_publisher(request, id): 
#     publisher = Publisher.objects.get(id=id)  
#     publisher.delete()  
#     return redirect("/publisher/show")   