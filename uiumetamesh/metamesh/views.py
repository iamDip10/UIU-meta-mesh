from django.shortcuts import render, redirect
from .models import *
from django.core import signing
from datetime import datetime
# Create your views here.

key = '011201171'
def indexPage(req):
    return render(req, "index.html") 

def signupPage(req):
    return render(req, "signup.html")

def post_sign(req):
    if req.method == "POST":
        s_id = req.POST['mail']
        fname = req.POST['fname']
        lname = req.POST['lname']
        password = req.POST['pass']
        dept = req.POST['dept']
        batch = req.POST['batch']
        phn = req.POST['phn']
        student = students(stu_id = s_id, firstName = fname, lastName = lname, password = password, batch = batch, dept = dept, phone_number = phn)

        student.save()

        return redirect('login')
    return render("signup")

def validate_user (req) :
    if req.method == "POST":
        __id = req.POST['email']
        __pass = req.POST['pass']

        objj = students.objects.get(stu_id = __id) 
        print(objj)
        if (objj and objj.password == __pass):
            encrp = signing.dumps(objj.stu_id, key=key)
            return redirect('dashb', user=encrp)

        return render(req, "index.html")

def dashboard(req, user):
    decrp = signing.loads(user, key=key) 
    __obj = students.objects.get(stu_id = decrp)
    _post = posts.objects.all()

    data = {
        'user': __obj,
        'enp':user,
        'post':_post,
    }

    return render(req, 'dashboard.html', data)
        
def postText(req, user):
    encrp = signing.loads(user, key=key)

    _obj = students.objects.get(stu_id = encrp)

    if req.method == "POST":
        text = req.POST['post']
        stu = _obj
        cat = req.POST['cat']
        idd = _obj.stu_id + "-" + datetime.now().strftime("%d-%m-%Y-%H-%M-%S")

        object = posts(text = text, student = stu, category = cat, _id = idd)

        object.save()

    return redirect('dashb', user=user)

def likeit(req):

    if req.method == 'POST':
        print(req.POST.get('post_id'))
        post_obj = posts.objects.get(iid = req.POST.get('post_id'))
        post_obj.upvote = int(post_obj.upvote) + 1 
        post_obj.save()

    print(post_obj)
    return redirect('login')