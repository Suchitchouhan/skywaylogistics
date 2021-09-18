from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class slider(models.Model):
	image = models.ImageField(default="avatars/Train-Freight-1024x576.jpg",upload_to='avatars/', blank=True, null=True)
	spec = models.CharField(default=' ',max_length=200)
	des = models.CharField(default= "Client & Service comes first and you`ll be surprised how far we will go for you,",max_length=300)
	def __str__(self):
		return self.spec

	
class contact(models.Model):
	fullname = models.CharField(default=" ",max_length=100)
	email = models.CharField(default=" ",max_length=100)
	des = models.CharField(default=" ",max_length=100)
	def __str__(self):
		return self.fullname+' - '+self.email

class feight(models.Model):
	name=models.CharField(default=" ",max_length=200)
	address=models.CharField(default=" ",max_length=400)
	city=models.CharField(default=" ",max_length=400)
	state=models.CharField(default=" ",max_length=400)
	country=models.CharField(default=" ",max_length=400)
	commodity =models.CharField(default=" ",max_length=400)
	phone=models.CharField(default=" ",max_length=20)
	cargo_file=models.FileField(upload_to ='feight',null=True,blank=True)
	verification=models.CharField(default="",max_length=20)
	def __str__(self):
		return str(self.pk)


class consignment(models.Model):
	uid=models.CharField(default="",max_length=200)
	shipping_address=models.CharField(default=" ",max_length=800,blank=True)
	reciving_address=models.CharField(default=" ",max_length=800,blank=True)
	shipper_name=models.CharField(default=" ",max_length=300,blank=True)
	reciver_name=models.CharField(default=" ",max_length=300,blank=True)
	type_of_shipment=models.CharField(default=" ",max_length=300,blank=True)
	invoice_number=models.CharField(default=" ",max_length=50,blank=True)
	mode=models.CharField(default=" ",max_length=100,blank=True)
	carrier=models.CharField(default=" ",max_length=300,blank=True)
	origin=models.CharField(default=" ",max_length=300,blank=True)
	destination=models.CharField(default=" ",max_length=300,blank=True)
	pickupdate=models.CharField(default=" ",max_length=50,blank=True)
	pickuptime=models.CharField(default=" ",max_length=50,blank=True)
	Expected_Delivery_date=models.CharField(default=" ",max_length=50,blank=True)
	qty=models.CharField(default=" ",max_length=40,blank=True)
	piece_type=models.CharField(default=" ",max_length=100,blank=True)
	weight=models.CharField(default=" ",max_length=100,blank=True)
	ch_weight=models.CharField(default=" ",max_length=100,blank=True)
	length=models.CharField(default=" ",max_length=100,blank=True)
	width=models.CharField(default=" ",max_length=100,blank=True)
	height=models.CharField(default=" ",max_length=100,blank=True)
	def __str__(self):
		return str(self.pk)
	# date2=models.CharField(default=" ",max_length=100,blank=True)
	# time2=models.CharField(default=" ",max_length=100,blank=True)
	# location2=models.CharField(default=" ",max_length=100,blank=True)
	# status2=models.CharField(default=" ",max_length=100,blank=True)
	# update_by2=models.CharField(default=" ",max_length=100,blank=True)
	# remarks2=models.CharField(default=" ",max_length=100,blank=True)
	# date3=models.CharField(default=" ",max_length=100,blank=True)
	# time3=models.CharField(default=" ",max_length=100,blank=True)
	# location3=models.CharField(default=" ",max_length=100,blank=True)
	# status3=models.CharField(default=" ",max_length=100,blank=True)
	# update_by3=models.CharField(default=" ",max_length=100,blank=True)
	# remarks3=models.CharField(default=" ",max_length=100,blank=True)
	
class pof(models.Model):
	consignment=models.ForeignKey(consignment,on_delete=models.CASCADE,null=True)
	proof_of_delivery=models.FileField(upload_to ='proof_of_delivery',null=True,blank=True)
	def __str__(self):
		return str(self.pk)

class shippment_history(models.Model):
	consignment=models.ForeignKey(consignment,on_delete=models.CASCADE,null=True)
	date=models.CharField(default=" ",max_length=100,blank=True)
	time=models.CharField(default=" ",max_length=100,blank=True)
	location=models.CharField(default=" ",max_length=100,blank=True)
	status=models.CharField(default=" ",max_length=100,blank=True)
	update_by=models.CharField(default=" ",max_length=100,blank=True)
	remarks=models.CharField(default=" ",max_length=100,blank=True)
	def __str__(self):
		return self.date

class feedback(models.Model):
	email=models.CharField(default='',max_length=100)
	mobile=models.CharField(default='',max_length=20)
	fullname=models.CharField(default='',max_length=200)
	about=models.CharField(default='',max_length=200)
	description=models.CharField(default='',max_length=300)
	def __str__(self):
		return self.email