from django.shortcuts import render, redirect, HttpResponse
from datetime import datetime,timedelta,date
# Create your views here.

from .models import isbn, roll, Transfer
from .models import transaction, issuedetails
from .forms import BookForm #, TransactionForm
from . import models, forms

from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
import PyPDF2
from PyPDF2 import PdfFileMerger
#import fitz

def venue_pdf(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize = letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)
    
    lines = []
    venues = models.Book.objects.all().last()
    """
    for venue in venues:
        lines.append(venue.name)
        lines.append(venue.isbn)
        lines.append(venue.author)
        lines.append(venue.category)
        lines.append(venue.count)
        """
    lines.append(venues.name)
    lines.append(venues.isbn)
    lines.append(venues.author)
    lines.append(venues.category)
    lines.append(venues.count)     
    
    for line in lines:
        textob.textLine(str(line)+"---")
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename="venue.pdf") 


def book_pdf(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize = letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)
    
    lines = [[]]
    venues = models.Book.objects.all().last()
    """
    for venue in venues:
        lines.append(venue.name)
        lines.append(venue.isbn)
        lines.append(venue.author)
        lines.append(venue.category)
        lines.append(venue.count)
    lines.append(venues.name)
    lines.append(venues.isbn)
    lines.append(venues.author)
    lines.append(venues.category)
    lines.append(venues.count)     
    """
    
    lines = [
             ['book name', venues.name],
             ['book ISBN', venues.isbn],
             ['author name', venues.author],
             ['book category', venues.category],
             ['copies available', venues.count],
             ]   
    
    
    textob.textLine("details of the latest book added to the library:-")
    for line in lines:
        textob.textLine(str(line))
    c.drawText(textob)
    c.showPage()
    c.setTitle('Book Reports')
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename="book.pdf")

def student_pdf(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize = letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)
    
    lines = [[]]
    venues = models.Student.objects.all().last()
    """
    for venue in venues:
        lines.append(venue.name)
        lines.append(venue.isbn)
        lines.append(venue.author)
        lines.append(venue.category)
        lines.append(venue.count)

    lines.append(venues.name)
    lines.append(venues.enrollment)
    lines.append(venues.branch)
    """
    
    lines = [
             ['student name', venues.name],
             ['enrollment no', venues.enrollment],
             ['department', venues.branch],
             ]   
    
    textob.textLine("details of the latest student added to the library:-")
    for line in lines:
        textob.textLine(str(line))
    c.drawText(textob)
    c.showPage()
    c.setTitle('Student Reports')
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename="student.pdf")

def issuedbook_pdf(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize = letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)
    
    lines = [[]]
    venues = models.IssuedBook.objects.all().last()
    """
    for venue in venues:
        lines.append(venue.name)
        lines.append(venue.isbn)
        lines.append(venue.author)
        lines.append(venue.category)
        lines.append(venue.count)
        """
        
    lines = [
             ['student enrollment no', venues.enrollment],
             ['ISBN', venues.isbn],
             ['issuedate', venues.issuedate],
             ['returndate', venues.expirydate],
             ]   
    #lines.append(venues.enrollment)
    #lines.append(venues.isbn)
    #lines.append(venues.issuedate)
    #lines.append(venues.expirydate)
    
    textob.textLine("details of the latest book issued from the library:-")
    for line in lines:
        textob.textLine(str(line))
    c.drawText(textob)
    c.showPage()
    c.setTitle('Issued Book Reports')
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename="issuedbook.pdf") 


def monthlyissuedbook_pdf(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize = letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)
    
    lines = [[]]
    for obj in models.IssuedBook.objects.filter(issuedate='2022-6-3'):
        lines.append(obj.enrollment)
        lines.append(obj.isbn)
        lines.append(obj.expirydate)
        lines.append(' ')
        
    #venues = models.IssuedBook.objects.all().filter(issuedate='2022-6-3')
    """
    for venue in venues:
        lines.append(venue.name)
        lines.append(venue.isbn)
        lines.append(venue.author)
        lines.append(venue.category)
        lines.append(venue.count)
        """
    """    
    lines = [
             ['student enrollment no', venues.enrollment],
             ['ISBN', venues.isbn],
             ['issuedate', venues.issuedate],
             ['returndate', venues.expirydate],
             ] 
    """
    #lines.append(venues.enrollment)
    #lines.append(venues.isbn)
    #lines.append(venues.issuedate)
    #lines.append(venues.expirydate)
    
    textob.textLine("details of the latest book issued from the library by month:-")
    #for line in lines:
        #textob.textLine(str(line))
        
    # importing required modules


# creating a pdf file object
    pdfFileObj = open('pdfs/test.pdf', 'rb')

# creating a pdf reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# printing number of pages in pdf file
    print(pdfReader.numPages)

# creating a page object
    pageObj = pdfReader.getPage(0)

# extracting text from page
    add = pageObj.extractText()
    print(pageObj.extractText())
    lines.append(add)
# closing the pdf file object
    pdfFileObj.close()
    
    for line in lines:
        textob.textLine(str(line))
    c.drawText(textob)
    c.showPage()
    c.setTitle('Issued Book Reports by month')
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename="monthlyissuedbook.pdf") 

 
objm = issuedetails()

def index(request):

    #form = EntryForm()

    #context = {'form' : form}

    #return render(request, 'index.html', context)
    return render(request, 'index.html')

    
def addbook(request):
    form=forms.BookForm()
    if request.method=='POST':
        #now this form have data from html
        form=forms.BookForm(request.POST)
        if form.is_valid():
            user=form.save()

            
            #obj2=models.issuedetails()
            objm.book=user.name
            objm.save()
            
            return render(request,'bookadded.html')
    return render(request,'addbook.html',{'form':form})

def addstudent(request):
    form=forms.StudentForm()
    if request.method=='POST':
        #now this form have data from html
        form=forms.StudentForm(request.POST)
        if form.is_valid():
            user=form.save()
            
            #obj2=models.issuedetails()
            objm.stname=user.name
            objm.save()
            
            return render(request,'studentadded.html')
    return render(request,'addstudent.html',{'form':form})

def viewbook(request):
    books=models.Book.objects.all()
    return render(request,'viewbook.html',{'books':books})

def viewstudent(request):
    students=models.Student.objects.all()
    return render(request,'viewstudent.html',{'students':students})

def issuebook(request):
    form=forms.IssuedBookForm()
    if request.method=='POST':
        #now this form have data from html
        form=forms.IssuedBookForm(request.POST)
        if form.is_valid():
            obj=models.IssuedBook()
            obj.enrollment=request.POST.get('enrollment2')
            obj.isbn=request.POST.get('isbn2')
            obj.save()
            
            books = models.Book.objects.filter(isbn=obj.isbn)    
            for book in books:
                book.count-=1
                book.save()
            print("hellloooooo") 
            
            #transfers = models.transaction.objects.all()
            #form=forms.TransactionForm()
            #if form.is_valid():
            
            obj2=models.transaction()
            obj2.isbn=obj.isbn
            obj2.enrollment=obj.enrollment
            obj2.save()
            
            return render(request,'bookissued.html')
    return render(request,'issuebook.html',{'form':form})

def viewissuedbook(request):
    issuedbooks=models.IssuedBook.objects.all()
    li=[]
    for ib in issuedbooks:
        issdate=str(ib.issuedate.day)+'-'+str(ib.issuedate.month)+'-'+str(ib.issuedate.year)
        expdate=str(ib.expirydate.day)+'-'+str(ib.expirydate.month)+'-'+str(ib.expirydate.year)
        #fine calculation
        days=(date.today()-ib.issuedate)
        print(date.today())
        d=days.days
        """
        fine=0
        if d>15:
            day=d-15
            fine=day*10
        """

        books=list(models.Book.objects.filter(isbn=ib.isbn))
        students=list(models.Student.objects.filter(enrollment=ib.enrollment))
        i=0
        for l in books:
            t=(students[i].name,students[i].enrollment,books[i].name,books[i].author,issdate,expdate)
            i=i+1
            li.append(t)
    """        
    books = models.Book.objects.filter(isbn=50)    
    for book in books:
        book.name="newww one"
        book.save()
    print("heyyy")  
    """
    return render(request,'viewissuedbook.html',{'li':li})


def deletebook(request):
    bookname = request.GET['name']
    obj = models.Book.objects.filter(name=bookname).delete()
    return redirect('index')

def searchbook(request):
    authorname = request.GET['name']
    obj = models.Book.objects.all().filter(author=authorname)
    context = {'obj' : obj, 'authorname':authorname}
    return render(request, 'searchbooks.html', context)

def searchstudent(request):
    isbn = request.GET['name']
    obj = models.IssuedBook.objects.all().filter(isbn=isbn)
    print(obj)
    context = {'obj' : obj, 'isbn':isbn}
    #return redirect('index')
    return render(request, 'searchstudent.html', context)

def deletestudent(request):
    stname = request.GET['name']
    obj = models.Student.objects.filter(name=stname).delete()
    return redirect('index')


def findcopies(request):
    book = request.GET['name']
    obj = models.Book.objects.all().filter(name=book)
    #print(obj[1])
    context = {'obj' : obj, 'book':book}
    return render(request, 'showuser.html', context)

def BookUploadView(request):
    if request.method == 'POST':
        form = forms.UploadBookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('The file is saved')
    else:
        form = forms.UploadBookForm()
        context = {
            'form':form,
        }
    return render(request, 'UploadBook.html', context)