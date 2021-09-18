from django.shortcuts import render
from package.models import *
from django.shortcuts import render,redirect
from django.utils.crypto import get_random_string
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import os
# Create your views here.


def check_blank_or_null(data):
    status = True
    for x in data:
        if x == None:
            status = True
        else:
            pass
    return status  



@login_required()
def logout_view(request):
    logout(request)
    return redirect("/")


def login_view(request):
	context={}
	if request.method=="POST":
		username=request.POST.get("username")
		password=request.POST.get("password")
		user=authenticate(username=username,password=password)
		if user is not None:
			login(request, user)
			return redirect("/panel")
		else:
			context['status']="email and password is not exists" 
		return render(request,"cmr/login.html",context)
	else:
		return render(request,"cmr/login.html",context) 


@login_required()
def panel(request):
	context={}
	if request.method=="GET":
		context['username']=request.user.username
		return render(request,"cmr/index.html",context)

login_required()
def view_feedback(request):
	context={}
	c=feedback.objects.all()
	page = request.GET.get('page', 1)
	paginator = Paginator(c, 100)
	try:
		con = paginator.page(page)
	except PageNotAnInteger:
		con = paginator.page(1)
	except EmptyPage:
		con = paginator.page(paginator.num_pages)
	context['contact']=con
	return render(request,"cmr/view_feedback.html",context)




@login_required()
def view_contact_us(request):
	context={}
	c=contact.objects.all()
	page = request.GET.get('page', 1)
	paginator = Paginator(c, 100)
	try:
		con = paginator.page(page)
	except PageNotAnInteger:
		con = paginator.page(1)
	except EmptyPage:
		con = paginator.page(paginator.num_pages)
	context['contact']=con
	return render(request,"cmr/view_contact_us.html",context)



@login_required()
def view_feight(request):
	context={}
	c=feight.objects.all()
	page = request.GET.get('page', 1)
	paginator = Paginator(c, 50)
	try:
		con = paginator.page(page)
	except PageNotAnInteger:
		con = paginator.page(1)
	except EmptyPage:
		con = paginator.page(paginator.num_pages)
	context['contact']=con
	return render(request,"cmr/view_feight.html",context)



@login_required()
def add_consignment(request):
	context={}
	if request.method=="POST":
		csvO=request.FILES['csv']
		print(csvO)
		if str(csvO).split(".")[-1]=="csv":
			count=1
			length=0
			for x in csvO:
				if count==1:
					count+=1
					length=len(x.decode("utf-8").split(","))
				else:
					if length==len(x.decode("utf-8").split(",")):
						data=x.decode("utf-8").split(",")
						con,__=consignment.objects.get_or_create(uid=data[0])
						con.shipping_address=data[1]
						con.reciving_address=data[2]
						con.shipper_name=data[3]
						con.reciver_name=data[4]
						con.type_of_shipment=data[5]
						con.invoice_number=data[6]
						con.mode=data[7]
						con.carrier=data[8]
						con.origin=data[9]
						con.destination=data[10]
						con.pickupdate=data[11]
						con.pickuptime=data[12]
						con.Expected_Delivery_date=data[13]
						con.qty=data[14]
						con.piece_type=data[15]
						con.weight=data[16]
						con.ch_weight=data[17]
						con.length=data[18]
						con.width=data[19]
						con.height=data[20]
						date=data[21].split('|')
						time=data[22].split('|')
						location=data[23].split('|')
						status=data[24].split('|')
						update_by=data[25].split('|')
						remarks=data[26].split('|')
						p_len=len(date)
						if len(date) == p_len and len(time) == p_len and len(location) == p_len and len(status) == p_len and len(update_by) == p_len and len(remarks) == p_len:
							for a,b,c,d,e,f in zip(date,time,location,status,update_by,remarks):
								sh_history,__=shippment_history.objects.get_or_create(consignment=con,date=a,time=b)
								sh_history.location=c
								sh_history.status=d
								sh_history.update_by=e
								sh_history.remarks=f
								sh_history.save()
							con.save()
							context['status']='consignment csv has been uploaded successfully'
						else:
							context['status']='file has been uploaded successfully'
					else:
						context['status']='data is not in right format'
		return render(request,'cmr/add_consignment.html',context)
	else:
		return render(request,'cmr/add_consignment.html',context)

@login_required()
def add_pof(request,pk):
	context={}
	if request.method == "POST":
		file=request.FILES['file']
		if check_blank_or_null([file]):
			if consignment.objects.filter(pk=pk).exists():
				con=consignment.objects.get(pk=pk)
				p,__=pof.objects.get_or_create(consignment=con)
				p.file=file
				p.save()
				context['status']='Proof of delivery added'
			else:
				context['status']="consignment Id is not exist"
		else:
			context['status']='file is not exists'					
	else:
		context['pk']=pk
	return render(request,'cmr/add_pof.html',context)		


@login_required()
def view_consignment(request):
	context={}
	if request.method == 'POST':
		uid=request.POST.get("uid")
		if check_blank_or_null([uid]):
			con=consignment.objects.filter(uid=uid)
			page = request.GET.get('page', 1)
			paginator = Paginator(con, 100)
			try:
				consign = paginator.page(page)
			except PageNotAnInteger:
				consign = paginator.page(1)
			except EmptyPage:
				consign = paginator.page(paginator.num_pages)
			context['consignment']=consign 	        
		else:
			context['status']='consignment id is not exists'    
	else:
		con=consignment.objects.all()
		page = request.GET.get('page', 1)
		paginator = Paginator(con, 100)
		try:
			consign = paginator.page(page)
		except PageNotAnInteger:
			consign = paginator.page(1)
		except EmptyPage:
			consign = paginator.page(paginator.num_pages)
		context['consignment']=consign
		print(context)
	return render(request,'cmr/view_consignment.html',context) 


@login_required()
def add_single_consignment(request):
	context={}
	if request.method=="POST":
		uid=request.POST.get("uid")
		shipping_address=request.POST.get("shipping_address")
		reciving_address=request.POST.get("reciving_address")
		shipper_name=request.POST.get("shipper_name")
		reciver_name=request.POST.get("reciver_name")
		type_of_shipment=request.POST.get("type_of_shipment")
		invoice_number=request.POST.get("invoice_number")
		mode=request.POST.get("mode")
		carrier=request.POST.get("carrier")
		origin=request.POST.get("origin")
		destination=request.POST.get("destination")
		pickupdate=request.POST.get("pickupdate")
		pickuptime=request.POST.get("pickuptime")
		Expected_Delivery_date=request.POST.get("Expected_Delivery_date")
		qty=request.POST.get("qty")
		piece_type=request.POST.get("piece_type")
		weight=request.POST.get("weight")
		ch_weight=request.POST.get("ch_weight")
		length=request.POST.get("length")
		width=request.POST.get("width")
		height=request.POST.get("height")
		gh=[uid,shipping_address,reciving_address,shipper_name,reciver_name,type_of_shipment,invoice_number,mode,carrier,
		origin,destination,pickuptime,pickuptime,Expected_Delivery_date,qty,piece_type,weight,ch_weight,length,width,height]
		if check_blank_or_null([gh]):
			con,__=consignment.objects.get_or_create(uid=uid)
			con.shipping_address=shipping_address
			con.reciving_address=reciving_address
			con.shipper_name=shipper_name
			con.reciver_name=reciver_name
			con.type_of_shipment=type_of_shipment
			con.invoice_number=invoice_number
			con.mode=mode
			con.carrier=carrier
			con.origin=origin
			con.destination=destination
			con.pickupdate=pickupdate
			con.pickuptime=pickuptime
			con.Expected_Delivery_date=Expected_Delivery_date
			con.qty=qty
			con.piece_type=piece_type
			con.weight=weight
			con.ch_weight=ch_weight
			con.length=length
			con.width=width
			con.height=height
			con.save()
			context['status']='consignment has been add successfully'
		else:
			context['status']='data is not in right format'
		return render(request,'cmr/add_single_consignment.html',context)	
	else:
		return render(request,'cmr/add_single_consignment.html',context)	
				

@login_required()
def update_single_consignment(request,uid):
	context={}
	if request.method=="POST":
		shipping_address=request.POST.get("shipping_address")
		reciving_address=request.POST.get("reciving_address")
		shipper_name=request.POST.get("shipper_name")
		reciver_name=request.POST.get("reciver_name")
		type_of_shipment=request.POST.get("type_of_shipment")
		invoice_number=request.POST.get("invoice_number")
		mode=request.POST.get("mode")
		carrier=request.POST.get("carrier")
		origin=request.POST.get("origin")
		destination=request.POST.get("destination")
		pickupdate=request.POST.get("pickupdate")
		pickuptime=request.POST.get("pickuptime")
		Expected_Delivery_date=request.POST.get("Expected_Delivery_date")
		qty=request.POST.get("qty")
		piece_type=request.POST.get("piece_type")
		weight=request.POST.get("weight")
		ch_weight=request.POST.get("ch_weight")
		length=request.POST.get("length")
		width=request.POST.get("width")
		height=request.POST.get("height")
		gh=[uid,shipping_address,reciving_address,shipper_name,reciver_name,type_of_shipment,invoice_number,mode,carrier,
		origin,destination,pickuptime,pickuptime,Expected_Delivery_date,qty,piece_type,weight,ch_weight,length,width,height]
		if check_blank_or_null([gh]):
			con=consignment.objects.get(uid=uid)
			con.shipping_address=shipping_address
			con.reciving_address=reciving_address
			con.shipper_name=shipper_name
			con.reciver_name=reciver_name
			con.type_of_shipment=type_of_shipment
			con.invoice_number=invoice_number
			con.mode=mode
			con.carrier=carrier
			con.origin=origin
			con.destination=destination
			con.pickupdate=pickupdate
			con.pickuptime=pickuptime
			con.Expected_Delivery_date=Expected_Delivery_date
			con.qty=qty
			con.piece_type=piece_type
			con.weight=weight
			con.ch_weight=ch_weight
			con.length=length
			con.width=width
			con.height=height
			con.save()
			context['status']='consignment has been add updated successfully'
		else:
			context['status']='data is not in right format'
	else:
		context['Consignment']=consignment.objects.get(uid=uid)
		context['uid']=uid
	return render(request,'cmr/update_single_consignment.html',context)	
				


@login_required()
def add_shipping_history(request,pk):
	context={}
	if request.method == "POST":
		date=request.POST.get("date")
		time=request.POST.get("time")
		location=request.POST.get("location")
		status=request.POST.get("status")
		update_by=request.POST.get("update_by")
		remarks=request.POST.get("remarks")
		if check_blank_or_null([date,time,location,status,update_by,remarks]):
			if consignment.objects.filter(pk=pk).exists():
				con=consignment.objects.get(pk=pk)
				shh,__=shippment_history.objects.get_or_create(consignment=con,date=date,time=time)
				shh.location=location
				shh.update_by=update_by
				shh.remarks=remarks
				shh.save()
				context['status']="shippment history has been added successfully"
			else:
				context['status']="Consignment uid is not exists"
		else:
			context['status']="Input format is worng"

		context['pk']=pk
	else:
		context['pk']=pk
	return render(request,'cmr/add_shipping_history.html',context)	
							

@login_required()
def update_shipping_history(request,pk):
	context={}
	if request.method == "POST":
		date=request.POST.get("date")
		time=request.POST.get("time")
		location=request.POST.get("location")
		status=request.POST.get("status")
		update_by=request.POST.get("update_by")
		remarks=request.POST.get("remarks")
		if check_blank_or_null([date,time,location,status,update_by,remarks]):
			shh=shippment_history.objects.get(pk=pk)
			shh.date=date
			shh.time=time
			shh.location=location
			shh.update_by=update_by
			shh.remarks=remarks
			shh.save()
			context['status']="shippment history has been updated successfully"
		else:
			context['status']="Input data is not right format"
		context['pk']=pk
		context['shippment']=shippment_history.objects.get(pk=pk)		
		context['con_pk']=str(shippment_history.objects.get(pk=pk).consignment.pk)		
	else:
		context['pk']=pk
		context['shippment']=shippment_history.objects.get(pk=pk)
		context['con_pk']=str(shippment_history.objects.get(pk=pk).consignment.pk)
	return render(request,'cmr/update_shipping_history.html',context)	
		



@login_required()
def view_shippment_history(request,pk):
	context={}
	if consignment.objects.filter(pk=pk).exists():
		con=consignment.objects.get(pk=pk)
		sh=shippment_history.objects.filter(consignment=con)
		context['history']=sh
	else:
		context['status']='Consignment is not exists'
	context['pk']=pk
	return render(request,'cmr/view_shippment_history.html',context)


@login_required()
def delete_shippment_history(request,pk):
	context={}
	if shippment_history.objects.filter(pk=pk).exists():
		sh=shippment_history.objects.get(pk=pk)
		cons=sh.consignment.pk
		sh.delete()
		return redirect('/view_shippment_history/'+str(cons))
	else:
		context['status']='shippment_history is not exists'
	return render(request,'cmr/view_shippment_history.html',context)


@login_required()
def add_pof(request,pk):
	context={}
	if request.method == 'POST':
		file=request.FILES['file']
		print(file)
		if consignment.objects.filter(pk=pk).exists():
			con=consignment.objects.get(pk=pk)
			p,__=pof.objects.get_or_create(consignment=con)
			p.proof_of_delivery=file
			p.save()
			context['status']='Proof of delivery has been added successfully'
		else:
			context['status']='consignment is not exists'
		context['pk']=pk
	else:
		context['pk']=pk
	return render(request,'cmr/add_pof.html',context)





login_required()
def view_slider(request):
	context={}
	if request.method == 'POST':
		image=request.FILES['image']
		spec=request.POST.get('spec')
		des=request.POST.get('des')
		if check_blank_or_null([image,spec,des]):
			sliderO=slider.objects.create()
			sliderO.image=image
			sliderO.spec=spec
			sliderO.des=des
			sliderO.save()
			context['status']='Slider has been added successfully'
		else:
			context['status']='Any Input field can not be empty'
		c=slider.objects.all()
		page = request.GET.get('page', 1)
		paginator = Paginator(c, 100)
		try:
			con = paginator.page(page)
		except PageNotAnInteger:
			con = paginator.page(1)
		except EmptyPage:
			con = paginator.page(paginator.num_pages)
		context['contact']=con
	else:
		c=slider.objects.all()
		page = request.GET.get('page', 1)
		paginator = Paginator(c, 100)
		try:
			con = paginator.page(page)
		except PageNotAnInteger:
			con = paginator.page(1)
		except EmptyPage:
			con = paginator.page(paginator.num_pages)
		context['contact']=con
	return render(request,"cmr/view_slider.html",context)

@login_required()
def delete_slider(request,pk):
	context={}
	if slider.objects.filter(pk=pk).exists():
		sl=slider.objects.get(pk=pk)
		sl.delete()
		return redirect('/view_slider')
	else:
		context['status']='Slider id is not exists'
	return render(request,"cmr/view_slider.html",context)
				