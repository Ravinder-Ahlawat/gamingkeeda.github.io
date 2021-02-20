from django.shortcuts import render, redirect
from .models import Match, Join, Links, Contact
from django.contrib import messages
from datetime import date
from django.views.decorators.csrf import csrf_exempt
from paytm import Checksum
MERCHANT_KEY = 'hK&NOEIFjVOpAfes'

from accounts.models import UserDetail

# Create your views here.


#Views for home page
def index(request):
    matches = Match.objects.all()
    no_of_cards = len(matches)
    abc = matches
    link = Links.objects.all()
    today = date.today()
    params = {'match': abc, 'range':range(0, no_of_cards), 'link':link, 'today':today}
    return render(request, 'index.html', params)




#for form submition
def sub2(request):
    uid = request.POST['id']
    path2 = request.POST['path2']
    return redirect(path2)


#for match view page
def mdview(request, myid):
    # fetching the matches using id
    match = Match.objects.filter(id=myid)
    joins = Join.objects.filter(Match_id=myid, payment=True)
    joined = len(joins)
    # request paytm to transfer the amount to your account after payment by user
    return render(request, 'mdview.html', {'match':match[0],'myid':myid, 'join':joins, 'joined':joined})


#for terms and conditions page
def tandc(request):
    return render(request, 'terms.html')


def csoon(request):
    return render(request, 'comingsoon.html')


def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        country = request.POST.get('country', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, country=country, desc=desc)
        contact.save()
    return render(request, 'contact.html')



# for join in a match
def joinnow(request):
    
    username = request.POST['username']
    pubg_id = request.POST['pubg_id']
    Match_id = request.POST['match_id']
    match_name = request.POST['match_name']
    amount = request.POST['amount']
    Email = request.POST['email']
    uid = request.POST['uid']
    order = str(pubg_id)+str(Match_id)+str(uid)
    order_id = order[-5:]
    Join.objects.filter(payment=False).delete()
    if Join.objects.filter(username=username, Match_id=Match_id).exists():
         messages.info(request, 'Already joined the match')
         a = '/mdview/' + str(Match_id)
         return redirect(a)


    else: 
        if amount == '0':
            join = Join(username=username, pubg_id=pubg_id, Match_id=Match_id, match_name=match_name, Email=Email, amount=amount, user_id=uid, payment=True)
            join.save();
            return redirect('/')
        else:
            join = Join(username=username, pubg_id=pubg_id, Match_id=Match_id, match_name=match_name, Email=Email, amount=amount, user_id=uid, payment=False)
            param_dict = {

                'MID': 'SsZmkq52163353024521',
                'ORDER_ID': order_id,
                'TXN_AMOUNT': amount,
                'CUST_ID': Email,
                'INDUSTRY_TYPE_ID': 'Retail',
                'WEBSITE': 'DEFAULT',
                'CHANNEL_ID': 'WEB',
                'CALLBACK_URL':'http://www.gamingkeeda.in/handlerequest/',

            }
            param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
            join.save();
            return render(request, 'paytm.html', {'param_dict': param_dict})
        
            
    return redirect('/')




# User profile page
def asd(request):
    return render(request, 'login.html')


# Paytm request hanling function
@csrf_exempt
def handlerequest(request):
    # paytm will send you post request here
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    return render(request, 'paymentstatus.html', {'response': response_dict})


def delforpay(request):
    uid = request.POST['uid']
    mid = request.POST['mid']
    a = '/mdview/' + str(mid)
    Join.objects.filter(user_id=uid, Match_id=mid).update(payment=True)
    messages.info(request, 'Joined Match Successfully..')
    return redirect(a)


def loginpage(request):
    return render(request, 'loginpage.html')