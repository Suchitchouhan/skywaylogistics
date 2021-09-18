from django.shortcuts import render
from .models import *


def check_blank_or_null(data):
    status = True
    for x in data:
        if x == "" and x == None:
            status = True
        else:
            pass
    return status

def check_blank(data):
    status = True
    for x in data:
        if x == None:
            status = True
        else:
            pass
    return status      
# Create your views here.
def index(request):
	context = {}
	if request.method == "POST":
		firstname = request.POST.get("firstname")
		lastname = request.POST.get("lastname")
		email= request.POST.get("email")
		des = request.POST.get("des")
		if firstname!=None and firstname!="" and lastname!=None and lastname!="" and email!="" and email!=None and des!=None and des!="":
			c=contact.objects.create(fullname=firstname+" "+lastname,email=email,des=des)
			c.save()
			context['status'] = "your query is successfully sent"
		else:
			context['status'] = "Please fill all Filled"
		context['slider'] = slider.objects.all()
	else:	
		context['slider'] = slider.objects.all()
		context['home']='active'
	return render(request,"package/index.html",context)


def about_us(request):
	context={}
	context['about_us']='active'
	return render(request,'package/about.html',context)


def view_core_service(request):
	context={}
	context['view_core_service']='active'
	return render(request,'package/view_core_service.html',context)


def intustry_service(request):
	context={}
	context['intustry_service']='active'
	return render(request,'package/intustry_service.html',context)


def Specialized_Logistic(request):
	context={}
	context['Specialized_Logistic']='active'
	return render(request,'package/Specialized_Logistic.html',context)




def feight_Quote(request):
	context={}
	context['feight_Quote']='active'
	if request.method=="POST":
		name=request.POST.get("name")
		address=request.POST.get("address")
		city=request.POST.get("city")
		state=request.POST.get("state")
		country=request.POST.get("country")
		commodity=request.POST.get("commodity")
		phone=request.POST.get("phone")
		cargo_file=request.FILES["file"]
		verification=request.POST.get("verification")
		if check_blank_or_null([name,address,city,state,country,commodity,phone,cargo_file,verification]) == True:
			feightO=feight.objects.create()
			feightO.name=name
			feightO.address=address
			feightO.city=city
			feightO.state=state
			feightO.country=country
			feightO.commodity=commodity
			feightO.phone=phone
			feightO.cargo_file=cargo_file
			feightO.verification=verification
			feightO.save()
			context['status'] = "successfully Sent"
		else:
			context['status'] = "unsuccessfull"	
		return render(request,'package/feight_Quote.html',{})
	else:
		return render(request,'package/feight_Quote.html',{})


def track(request):
	context={}
	context['track']='active'
	if request.method=="POST":
		num=request.POST.get("num")
		if check_blank_or_null([num]):
			if consignment.objects.filter(uid=num).exists():
				c=consignment.objects.get(uid=num)
				context['consignment']=c
				if pof.objects.filter(consignment=c).exists():
					context['pof']=pof.objects.get(consignment=c).proof_of_delivery.url
				context['shippment']=shippment_history.objects.filter(consignment=c)	
			else:
				context['status']="consignment is not exists"
		else:
			context['status']="consignment is not exists"
		return render(request,'package/track.html',context)
	else:		
		return render(request,'package/track.html',context)


def add_feedback(request):
	context={}
	context['add_feedback']='active'
	if request.method == 'POST':
		email=request.POST.get('email')
		mobile=request.POST.get('mobile')
		fullname=request.POST.get('fullname')
		about=request.POST.get('about')
		description=request.POST.get('description')
		if check_blank([email,mobile,fullname,about,description]):
			feed=feedback.objects.create()
			feed.email=email
			feed.mobile=mobile
			feed.fullname=fullname
			feed.about=about
			feed.description=description
			feed.save()
			context['status']='Your Feedback has been successfully sent ,Your Feedback is very valuable to us'
		else:
			context['status']='Worng Input format'
		return render(request,'package/add_feedback.html',context)
	else:
		return render(request,'package/add_feedback.html',context)
					






