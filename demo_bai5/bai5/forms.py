from dataclasses import field
from django import forms  
from bai5.models import *
class AuthorForm(forms.ModelForm):  
    class Meta:  
        model = Author
        fields = "__all__" 

class CategoryBookForm(forms.ModelForm):
    class Meta:
        model = CategoryBook
        fields = "__all__" 

class PublisherForm(forms.ModelForm):  
    class Meta:  
        model = Publisher
        fields = "__all__" 

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__" 