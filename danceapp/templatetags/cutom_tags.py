from django import template
from danceapp.models import Registration

register = template.Library()

@register.simple_tag
def pendingbook(data, data2):
    new = Registration.objects.filter(status='New')
    return new

@register.filter(name='findreportyear')
def findreportyear(year):
    data = Registration.objects.filter(creationdate__year=year)
    total = 0
    for i in data:
        total += int(i.classname.cost)
    return total

@register.filter(name='findreportmonth')
def findreportmonth(month):
    data = Registration.objects.filter(creationdate__month=month)
    total = 0
    for i in data:
        total += int(i.classname.cost)
    return total

@register.filter(name='findmonth')
def findmonth(month):
    li = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    return li[month-1]