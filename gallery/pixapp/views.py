from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt

# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to PixWall')



def show_date(request):
    date = dt.date.today()

    # FUNCTION TO CONVERT DATE OBJECT TO FIND EXACT DAY

    html = f'''
        <html>
            <body>
                <h1>News for KEPHA</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)
