
from django import forms
from . import models



class BookForm(forms.ModelForm):
    class Meta:
        model=models.Book
        fields=['name','isbn','author','category','count']


class StudentForm(forms.ModelForm):
    class Meta:
        model=models.Student
        fields=['name','enrollment','branch']

        
class TransactionForm(forms.ModelForm):
    class Meta:
        model = models.transaction
        fields=['isbn', 'enrollment']
        

class IssuedBookForm(forms.Form):
    #to_field_name value will be stored when form is submitted.....__str__ method of book model will be shown there in html
    isbn2=forms.ModelChoiceField(queryset=models.Book.objects.all(),empty_label="Name and isbn", to_field_name="isbn",label='Name and Isbn')
    enrollment2=forms.ModelChoiceField(queryset=models.Student.objects.all(),empty_label="Name and enrollment",to_field_name='enrollment',label='Name and enrollment')
    
    
class UploadBookForm(forms.ModelForm):
    class Meta:
        model = models.EBooksModel
        fields = ('title', 'pdf',)
    