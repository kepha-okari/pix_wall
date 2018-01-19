from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt

# # Create your views here.
# def welcome(request):
#     return HttpResponse('Welcome to PixWall')

def welcome(request):
    return render(request, 'welcome.html')

def show_date(request):
    date = dt.date.today()

    # FUNCTION TO CONVERT DATE OBJECT TO FIND EXACT DAY
    day = convert_dates(date)
    html = f'''
        <html>
            <body>
                <h1>{day} {date.day}-{date.month}-{date.year}</h1>
                <p
            </body>
        </html>
            '''
    return HttpResponse(html)
def convert_dates(dates):
    #funticon that gets the weekday number for the dates
    day_number = dt.date.weekday(dates)
    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

    #rReturning the actual date of the weekday
    day = days[day_number]
    return day
