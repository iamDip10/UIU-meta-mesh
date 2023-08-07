from django.shortcuts import render, redirect
from .models import *
from django.core import signing
from datetime import datetime
import json
from django.db.models import Q
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
            objj.active = "true"
            objj.save()
            req.session['validate'] = True
            encrp = signing.dumps(objj.stu_id, key=key)
            return redirect('dashb', user=encrp)

        return render(req, "index.html")

def logout(req, user):
    if 'validate' in req.session:
        obj = students.objects.get(stu_id = user)
        obj.active = 'false'
        obj.save()
        del req.session['validate']

    return redirect('login')
        

def dashboard(req, user):
    if 'validate' in req.session:
        decrp = signing.loads(user, key=key) 
        __obj = students.objects.get(stu_id = decrp)
        _post = posts.objects.all().order_by('upvote').reverse()
        _likes = likes.objects.filter(user = __obj)
        _like = json.dumps(list(_likes.values()))
        postJS = json.dumps(list(_post.values()))
        noti = notification.objects.filter(to = __obj)
        active = students.objects.filter(active = 'true')
        data = {
            'user': __obj,
            'enp':user,
            'post':_post,
            'likes' : _like,
            'postJS':postJS,
            'noti': noti,
            'activ': active,
        }

        return render(req, 'dashboard.html', data)
    else:
        return redirect('login')
        
def postText(req, user):
    if 'validate' in req.session:
        encrp = signing.loads(user, key=key)

        _obj = students.objects.get(stu_id = encrp)

        if req.method == "POST":
            text = req.POST['post']
            stu = _obj
            cat = req.POST['cat']
            idd = _obj.stu_id + "-" + datetime.now().strftime("%d-%m-%Y-%H-%M-%S")

            object = posts(text = text, student = stu, category = cat, iid = idd)

            object.save()

        return redirect('dashb', user=user)
    else:
        return redirect('login')

def likeit(req):
    if 'validate' in req.session:
        if req.method == 'POST':
            print(req.POST.get('post_id'))
            user = students.objects.get(stu_id = req.POST.get('user'))
            post_obj = posts.objects.get(iid = req.POST.get('post_id'))
            post_obj.upvote = int(post_obj.upvote) + 1 
            post_obj.save()
            like = likes(counter = post_obj.upvote, post = post_obj, user = students.objects.get(stu_id = req.POST.get('user')))
            like.save()
            message = user.firstName + " " + user.lastName + " has upvoted your post."
            notificat = notification(message = message, to=post_obj.student)
            notificat.save()

        print("Hello" + post_obj)
        return redirect('dashb', user=req.POST.get('enpp'))
    else:
        return redirect('login') 

def club(req, user):
    dercp = signing.loads(user, key=key)
    obj = students.objects.get(stu_id = dercp)
    clubss = clubs.objects.all()
    sortclub = json.dumps(list(clubApproval.objects.filter(studentss = obj).values()))
    data = {
        'obj': obj,
        'enp': user,
        'club':clubss,
        'sort': sortclub,
    }
    return render(req, "club.html", data)

def createClub(req, user):
    derc = signing.loads(user, key=key)
    obj = students.objects.get(stu_id = derc)

    if req.method == "POST":
        cname = req.POST['cname']
        ctype = req.POST['ctype']
        purpose = req.POST['purpose']
        rules = req.POST['rules']
        admin = req.POST['admin']
        print(admin)
        if admin == 'Admin':
            a_name = obj.firstName + " " + obj.lastName
            a_obj = obj
        else:
            a_name = req.POST['adminname']
            a_obj = students.objects.get(stu_id = req.POST['adminmail'])

        clu = clubs(clubname = cname, clubtype = ctype, purpose = purpose, rules = rules, adminname = a_name, adminid = a_obj)
        
        clu.save()
    
    return redirect('club', user)

def clubApprove(req, user, club):
    clubd = clubs.objects.get(clubname = club)
    student = students.objects.get(stu_id = signing.loads(user, key=key))
    admin = clubd.adminid
    if admin == student:
        status = "Enter"
    else:
        status = "Pending"

    clubapprv = clubApproval(clubid = clubd, studentss = student, status = status, admin = admin)
    clubapprv.save()

    return redirect('club', user=user) 

def clubDash (req, user, club):

    decrp = signing.loads(user, key=key)
    obj = students.objects.get(stu_id = decrp)
    clubb = clubs.objects.get(clubname = club)
    data = {
        'obj':obj ,
        'enp': user,
        'clb':clubb,
    }
    return render(req, 'clubdashboard.html', data)

def posthandling(req, user, club):
    if req.method == "POST":
        texts = req.POST['texts']
        studnt = students.objects.get(stu_id = signing.loads(user, key=key))
        clubb = clubs.objects.get(clubname = club)
        iid = clubb.clubname + " " + datetime.now()

        clubposts = clubpost(texts = texts, clubid = clubb, student = studnt, iid = iid)
        clubposts.save()

    return redirect('cdash', user=user, club=club)

    
        
