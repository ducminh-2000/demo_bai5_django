"""demo_bai5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bai5.controller.authorController import AuthorController 
from bai5.controller.publisherController import PublisherController 
from bai5.controller.categoryController import CategoryController 
from bai5.controller.bookController import BookController 



urlpatterns = [
    path('admin/', admin.site.urls),
    path('author/create', AuthorController.create_author),  
    path('author/show', AuthorController.show_author),  
    path('author/edit/<int:id>', AuthorController.edit_author),  
    path('author/update/<int:id>', AuthorController.update_author),  
    path('author/delete/<int:id>', AuthorController.delete_author),  
    path('publisher/create', PublisherController .create_publisher),  
    path('publisher/show',PublisherController .show_publisher),  
    path('publisher/edit/<int:id>', PublisherController .edit_publisher),  
    path('publisher/update/<int:id>', PublisherController .update_publisher),  
    path('publisher/delete/<int:id>', PublisherController .delete_publisher), 
    path('category/create', CategoryController .create_category),  
    path('category/show',CategoryController .show_category),  
    path('category/edit/<int:id>', CategoryController .edit_category),  
    path('category/update/<int:id>', CategoryController .update_category),  
    path('category/delete/<int:id>', CategoryController .delete_category), 
    path('book/create', BookController .create_book),  
    path('book/show',BookController .show_book),  
    path('book/edit/<int:id>',BookController .edit_book),  
    path('book/update/<int:id>', BookController .update_book),  
    path('book/delete/<int:id>', BookController .delete_book), 
]
