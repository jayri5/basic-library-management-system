
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('findcopies', views.findcopies),
    path('addbook', views.addbook),
    path('viewbook', views.viewbook),
    path('addstudent', views.addstudent),
    path('viewstudent', views.viewstudent),
    path('issuebook', views.issuebook),
    path('deletebook', views.deletebook),
    path('deletestudent', views.deletestudent),
    path('viewissuedbook', views.viewissuedbook),
    #path('sendmail', views.sendmail),
    path('searchbook', views.searchbook),
    path('searchstudent', views.searchstudent),
    path('venue_pdf', views.venue_pdf, name='venue_pdf'),
    path('book_pdf', views.book_pdf, name='book_pdf'),
    path('student_pdf', views.student_pdf, name='student_pdf'),
    path('issuedbook_pdf', views.issuedbook_pdf, name='issuedbook_pdf'),
    path('monthlyissuedbook_pdf', views.monthlyissuedbook_pdf, name='monthlyissuedbook_pdf'),
    path('book/upload', views.BookUploadView, name ='BookUploadView'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

