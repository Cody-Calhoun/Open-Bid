from django.shortcuts import render, redirect
from .models import Customer, Specialty, Contractor, Bid, Review, Project
import bcrypt
from django.contrib import messages

def index(request):
    return render(request, 'login.html')

def con_reg_form(request):
    return render(request, 'contractor_reg.html')

def con_register(request):
    errors = Contractor.objects.con_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(con_reg_form)
    
    password = request.POST['password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    con = Contractor.objects.create(
        bname = request.POST['bname'],
        alias = request.POST['alias'],
        email = request.POST['email'],
        city = request.POST['city'],
        state = request.POST['state'],
        zipcode = request.POST['zipcode'],
        password = pw_hash,
    )
    spec = Specialty.objects.create(
        title = request.POST['specialty'],
    )
    spec.contractors.add(con)
    request.session['id'] = con.id
    return redirect(con_home)

def con_login(request):
    user_db = Contractor.objects.filter(email=request.POST['email'])
    if user_db:
        log_user = user_db[0]

        if bcrypt.checkpw(request.POST['password'].encode(), log_user.password.encode()):
            request.session['id'] = log_user.id
            return redirect(con_home)

    messages.error(request, 'Incorrect email or password.')
    return redirect(con_reg_form)

def con_home(request):
    con = Contractor.objects.get(id=request.session['id'])
    context = {
        'contractor': con
    }
    return render(request, 'contractor-home.html', context)










def cus_reg_form(request):
    return render(request, 'customer_reg.html')

def cus_register(request):
    errors = Customer.objects.cus_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(cus_reg_form)
    
    password = request.POST['password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    cus = Customer.objects.create(
        fname = request.POST['fname'],
        lname = request.POST['lname'],
        email = request.POST['email'],
        city = request.POST['city'],
        state = request.POST['state'],
        zipcode = request.POST['zipcode'],
        password = pw_hash,
    )
    
    request.session['id'] = cus.id
    return redirect('/cus_home')

def cus_login(request):
    user_db = Customer.objects.filter(email=request.POST['email'])
    if user_db:
        log_user = user_db[0]

        if bcrypt.checkpw(request.POST['password'].encode(), log_user.password.encode()):
            request.session['id'] = log_user.id
            return redirect(cus_home)

    messages.error(request, 'Incorrect email or password.')
    return redirect(cus_reg_form)

def cus_home(request):
    cus = Customer.objects.get(id=request.session['id'])
    context = {
        'customer': cus
    }
    return render(request, 'customer-home.html', context)