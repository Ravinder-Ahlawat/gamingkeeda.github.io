from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import UserDetail
from django.urls import resolve
   
# Create your views here.


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']


        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('Register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('Register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save();
                messages.info(request, 'User created')
                return redirect('register2')
            
        else:
            messages.info(request, 'pass not matching...')
            return redirect('Register')
        return redirect('/')
        
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        pathe = request.POST['path1']
        user = auth.authenticate(username=username, password=password)
        print(pathe)

        if user is not None:
            auth.login(request, user)
            return redirect(pathe)

        else:
            messages.info(request, 'no data found plz create account')
            return redirect('Register')

    else:
        messages.info(request, 'no data found plz create account')
        return redirect('Register')


def logout(request):
    auth.logout(request)
    return redirect('/')





# def aj(request):
#     if request.method == 'POST':
#         pubg_id = request.POST['pubg_id']
#         pubg_name = request.POST['pubg_name']
#         mobile = request.POST['mobile']
#         clan_name = request.POST['clan_name']
#         info = Profile(pubg_id=pubg_id, pubg_name=pubg_name, mobile=mobile, clan_name=clan_name)
#         info.save()
#         messages.info(request, 'profile updated')
#         return render(request, 'login.html')
        
#     else:
#         infos = Profile.objects.all()
#         print(infos[0])
#         return render(request, 'login.html', {'infos':infos[0]})
    

def register2(request):
    return render(request, 'register2.html')


def pubgin(request):
    if request.method == 'POST':
        user = request.POST['user']
        user_id = request.POST['id']
        phone = request.POST['phone']
        pubg_name = request.POST['pubg_name']
        pubg_id = request.POST['pubg_id']
        pubginfo = UserDetail(user_id=user_id, phone=phone, pubg_name=pubg_name, pubg_id=pubg_id, user=user)
        pubginfo.save()
        return redirect('/')



# def asd(request, myid):
#     detail = UserDetails.objects.filter(user_id=myid)
#     print(detail)
#     return render(request, 'login.html', {'data':detail[0]})