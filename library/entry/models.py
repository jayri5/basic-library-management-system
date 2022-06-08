from django.db import models
from datetime import datetime,timedelta

class EBooksModel(models.Model):
 
    title = models.CharField(max_length = 80)
    pdf = models.FileField(upload_to='pdfs/')
 
    class Meta:
        ordering = ['title']
     
    def __str__(self):
        return f"{self.title}"
    
class Book(models.Model):
    catchoice= [
        ('education', 'Education'),
        ('entertainment', 'Entertainment'),
        ('comics', 'Comics'),
        ('biography', 'Biography'),
        ('history', 'History'),
        ('novel', 'Novel'),
        ('fantasy', 'Fantasy'),
        ('thriller', 'Thriller'),
        ('romance', 'Romance'),
        ('scifi','Sci-Fi')
        ]
    name=models.CharField(max_length=30)
    isbn=models.PositiveIntegerField()
    author=models.CharField(max_length=40)
    category=models.CharField(max_length=30,choices=catchoice,default='education')
    count=models.IntegerField(default=0)
    def __str__(self):
        return str(self.name)+"["+str(self.isbn)+']'    

class Student(models.Model):
    name = models.CharField(max_length=60)
    enrollment = models.CharField(max_length=40)
    branch = models.CharField(max_length=40)
    #used in issue book
    def __str__(self):
        return self.name+'['+str(self.enrollment)+']'
    
def get_expiry():
    return datetime.today() + timedelta(days=365)    
class IssuedBook(models.Model):
    enrollment=models.CharField(max_length=30)
    isbn=models.CharField(max_length=30)
    issuedate=models.DateField(auto_now=True)
    expirydate=models.DateField(default=get_expiry)
    def __str__(self):
        return self.enrollment


class issuedetails(models.Model):
    book = models.CharField(max_length=50)
    stname = models.CharField(max_length=50)
    
    def __str__(self):
        return self.book + "-" + self.stname
    
class transaction(models.Model): 
     isbn = models.CharField(max_length=30)
     enrollment = models.CharField(max_length=30)
     
     def __str__(self):
         return self.isbn + '-' + str(self.enrollment)
     
    
class isbn(models.Model):
    isbn = models.CharField(max_length=200)
    def __str__(self):
        return self.isbn
    
class Booknew(models.Model):
    isbn = models.OneToOneField(isbn, on_delete=models.CASCADE, primary_key = True)
    name = models.CharField(max_length = 50)
    count =  models.IntegerField(default=0)
    def __str__(self):
        return str(self.isbn)

class roll(models.Model):
    roll = models.CharField(max_length=200)
    def __str__(self):
        return self.roll 
    
class Transfer(models.Model):
    tid = models.CharField(max_length=10, primary_key = True)
    isbn = models.ForeignKey(isbn, on_delete=models.CASCADE)
    sr = models.ForeignKey(roll, on_delete=models.CASCADE)
    
