from django.contrib import admin

from .models import CPU, VGA, Author, Book, CategoryBook, Laptop, MobilePhone, Publisher

# Register your models here.
admin.site.register(Book)
admin.site.register(CategoryBook)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Laptop)
admin.site.register(MobilePhone)
admin.site.register(CPU)
admin.site.register(VGA)
