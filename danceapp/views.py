from random import randint

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import *

from .models import *

# Create your views here.

def index(request):
    return render(request, "index_home.html")

@login_required(login_url='/login/')
def dashboard(request):
    classname = Class.objects.filter()
    teacher = Teacher.objects.filter()
    total = Registration.objects.filter()
    new = Registration.objects.filter(status="New")
    selected = Registration.objects.filter(status="Selected")
    rejected = Registration.objects.filter(status="Rejected")
    return render(request, "admin_dashboard.html", locals())

def index_class(request):
    data = Class.objects.all()
    d = {'data': data}
    return render(request, "index_class.html", locals())

def index_team(request):
    data = Teacher.objects.all()
    d = {'data': data}
    return render(request, "team.html", locals())

def admin_login(request):
    if request.method == "POST":
        uname = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(username=uname, password=pwd)
        if user:
            if user.is_staff:
                login(request, user)
                messages.success(request, "Login Successful")
                return redirect('dashboard')
            else:
                messages.success(request, "Invalid User")
                return redirect('login')
    return render(request, "admin_login.html")

@login_required(login_url='/admin_login/')
def logout_admin(request):
    logout(request)
    messages.success(request, "logout Successful")
    return redirect('admin_login')

@login_required(login_url='/admin_login/')
def admin_change_password(request):
    user = User.objects.get(username=request.user.username)
    if request.method == "POST":
        n = request.POST['pwd1']
        c = request.POST['pwd2']
        o = request.POST['pwd3']
        if c == n:
            u = User.objects.get(username__exact=request.user.username)
            u.set_password(c)
            u.save()
            messages.success(request, "Password changed successfully")
            return redirect('/')
        else:
            messages.success(request, "New password and confirm password are not same.")
            return redirect('admin_change_password')

    return render(request, 'admin_change_password.html')

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def registration(request, pid=None):
    registration = None
    if pid:
        registration = Registration.objects.get(id=pid)
    if request.method == "POST":
        registration = RegistrationForm(request.POST, request.FILES, instance=registration)
        if registration.is_valid():
            new_registration = registration.save()
        if not pid:
            new_registration.registernumber = random_with_N_digits(10)
        new_registration.register = registration
        new_registration.save()
        if pid:
            messages.success(request, "Update Registration Successful")
            return redirect('registration')
        else:
            messages.success(request, "Add Registration Successful Registration Number   " + str(new_registration.registernumber))
            return redirect('registration')
    myclass = Class.objects.all()
    return render(request, 'registration.html', locals())

@login_required(login_url='/admin_login/')
def registrationlist(request):
    action = request.GET.get('action')
    if action == "New":
        data = Registration.objects.filter(status='New')
    elif action == "Selected":
        data = Registration.objects.filter(status='Selected')
    elif action == "Rejected":
        data = Registration.objects.filter(status='Rejected')
    elif action == "Total":
        data = Registration.objects.filter()
    d = {'data': data}
    return render(request, "admin_registration.html", d)

@login_required(login_url='/admin_login/')
def registration_detail(request, pid):
    data = Registration.objects.get(id=pid)
    if request.method == "POST":
        remark = request.POST['remark']
        status = request.POST['status']
        data.status = status
        data.save()
        Trackinghistory.objects.create(registration=data, remark=remark, status=status)
        messages.success(request, "Action Updated")
        return redirect('registration_detail', pid)
    traking = Trackinghistory.objects.filter(registration=data)
    return render(request, "registration_detail_admin.html", locals())

@login_required(login_url='/admin_login/')
def delete_registration(request, pid):
    data = Registration.objects.get(id=pid)
    data.delete()
    messages.success(request, "Delete Successful")
    return redirect('dashboard')

def invoice(request):
    data = Registration.objects.all()
    d = {'data': data}
    return render(request, "invoice.html", locals())

@login_required(login_url='/admin_login/')
def add_class(request, pid=None):
    classes = None
    if pid:
        classes = Class.objects.get(id=pid)
    if request.method == "POST":
        classes = ClassForm(request.POST, request.FILES, instance=classes)
        if classes.is_valid():
            new_classes = classes.save()
            new_classes.save()
        if pid:
            messages.success(request, "Update Class Successful")
            return redirect('view_class')
        else:
            messages.success(request, "Add Class Successful")
            return redirect('view_class')
    return render(request, 'add_class.html', locals())

@login_required(login_url='/admin_login/')
def view_class(request):
    data = Class.objects.all()
    d = {'data': data}
    return render(request, "view_class.html", d)

@login_required(login_url='/admin_login/')
def delete_class(request, pid):
    data = Class.objects.get(id=pid)
    data.delete()
    messages.success(request, "Delete Successful")
    return redirect('view_class')

@login_required(login_url='/admin_login/')
def add_teacher(request, pid=None):
    teacher = None
    if pid:
        teacher = Teacher.objects.get(id=pid)
    if request.method == "POST":
        teacher = TeacherForm(request.POST, request.FILES, instance=teacher)
        if teacher.is_valid():
            new_teacher = teacher.save()
            new_teacher.save()
        if pid:
            messages.success(request, "Update Teacher Successful")
            return redirect('view_teacher')
        else:
            messages.success(request, "Add Teacher Successful")
            return redirect('view_teacher')
    myclass = Class.objects.all()
    return render(request, 'add_teacher.html', locals())

@login_required(login_url='/admin_login/')
def view_teacher(request):
    data = Teacher.objects.all()
    d = {'data': data}
    return render(request, "view_teacher.html", d)

@login_required(login_url='/admin_login/')
def delete_teacher(request, pid):
    data = Teacher.objects.get(id=pid)
    data.delete()
    messages.success(request, "Delete Successful")
    return redirect('view_teacher')

@login_required(login_url='/admin_login/')
def about(request):
    if request.method == "POST":
        pagetitle = request.POST['pagetitle']
        description = request.POST['description']
        About.objects.filter(id=1).update(pagetitle=pagetitle, description=description)
    data = About.objects.get(id=1)
    return render(request, "about.html", locals())

def index_about(request):
    data = About.objects.all()
    d = {'data': data}
    return render(request, "index_about.html", locals())

@login_required(login_url='/admin_login/')
def contact(request):
    if request.method == "POST":
        pagetitle = request.POST['pagetitle']
        description = request.POST['description']
        email = request.POST['email']
        mobile = request.POST['mobile']
        timing = request.POST['timing']
        Contact.objects.filter(id=1).update(pagetitle=pagetitle, description=description, email=email, timing=timing)
    data = Contact.objects.get(id=1)
    return render(request, "contact.html", locals())

def index_contact(request):
    data = Contact.objects.all()
    d = {'data': data}
    return render(request, "index_contact.html", locals())

@login_required(login_url='/admin_login/')
def admin_report(request):
    data = None
    data2 = None
    if request.method == "POST":
        fromdate = request.POST['fromdate']
        todate = request.POST['todate']

        data = Registration.objects.filter(creationdate__gte=fromdate, creationdate__lte=todate)
        data2 = True
    return render(request, "admin_report.html", locals())

@login_required(login_url='/admin_login/')
def invoice_detail(request, pid):
    data = Registration.objects.get(id=pid)
    if request.method == "POST":
        paymentmode = request.POST['paymentmode']
        payment = request.POST['payment']
        data.payment = payment
        data.save()
        Invoice.objects.create(registration=data, paymentmode=paymentmode, payment=payment)
        messages.success(request, "Payment Updated")
        return redirect('invoice_detail', pid)
    invoice = Invoice.objects.filter(registration=data)
    return render(request, "invoice_detail.html", locals())

@login_required(login_url='/admin_login/')
def search_registration(request):
    data = None
    data2 = None
    if request.method == "POST":
        fromdate = request.POST['fromdate']
        data2 = True
        data = Registration.objects.filter(registernumber__icontains=fromdate)
    return render(request, "admin_search_registration.html", locals())\

@login_required(login_url='/admin_login/')
def search_invoice(request):
    data = None
    data2 = None
    if request.method == "POST":
        fromdate = request.POST['fromdate']
        data2 = True
        data = Registration.objects.filter(registernumber__icontains=fromdate)
    return render(request, "admin_search_invoice.html", locals())

from django.db.models.functions import TruncMonth, TruncYear
from django.db.models import Count, Sum
def report(request):
    data = None
    fromdate = None
    todate = None
    if request.method == "POST":
        fromdate = request.POST['fromdate']
        todate = request.POST['todate']
        req = request.POST.get('reqtype')
        print(fromdate)
        mont1 = int(fromdate.split('-')[1])
        mont2 = int(todate.split('-')[1])
        yer1 = int(fromdate.split('-')[0])
        yer2 = int(todate.split('-')[0])
        monthli = [i for i in range(mont1, mont2+1)]
        yearli = [i for i in range(yer1, yer2+1)]

    return render(request, "sales_report.html",locals())

@login_required(login_url='/admin_login/')
def admin_change_password(request):
    user = User.objects.get(username=request.user.username)
    if request.method == "POST":
        n = request.POST['pwd1']
        c = request.POST['pwd2']
        o = request.POST['pwd3']
        if c == n:
            u = User.objects.get(username__exact=request.user.username)
            u.set_password(c)
            u.save()
            messages.success(request, "Password changed successfully")
            return redirect('/')
        else:
            messages.success(request, "New password and confirm password are not same.")
            return redirect('admin_change_password')

    return render(request, 'admin_change_password.html')