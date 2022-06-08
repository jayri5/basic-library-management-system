from django.contrib import admin

from entry.models import Book, Student, IssuedBook, transaction, isbn, issuedetails, EBooksModel


#admin.site.register(Entry)
admin.site.register(Book)
admin.site.register(Student)
admin.site.register(IssuedBook)
admin.site.register(transaction)
admin.site.register(issuedetails)
admin.site.register(EBooksModel)
