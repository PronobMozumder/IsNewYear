from django.shortcuts import render
import datetime
def index(request):
    now = datetime.datetime.now()
    if now.day is True and now.month is True:
    # if now.day == 18 and now.month == 6:
        newyear = True
    else:
        newyear = False
    return render(request, 'index.html', {'newyear': newyear , 'now': now})