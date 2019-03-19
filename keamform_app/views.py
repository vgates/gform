from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection

# Create your views here.
def index(request):
    #return HttpResponse("Hello World")    
    with connection.cursor() as cursor:
        #cursor.execute("SELECT * FROM registrations WHERE id = 1")
        #row = cursor.fetchone()
        cursor.execute("SELECT * FROM registrations")
        rows = cursor.fetchall()
    # return HttpResponse( mydict )
    return render(request, 'keamform_app/index.html', context={'rows':rows})
