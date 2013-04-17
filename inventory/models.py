from django.db import models

#to enable the admin interface for this app
from django.contrib import admin

class Unit(models.Model):
	name = models.CharField(max_length=10)
	created = models.DateTimeField(auto_now=False)
	updated = models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return self.unit

class Currency(models.Model):
	name = models.CharField(max_length=100)
	code = models.CharField(max_length=3)
	symbol = models.CharField(max_length=3)
	created = models.DateTimeField(auto_now=False)
	updated = models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return self.code


# Create your models here.
class Commodity(models.Model):
	name = models.CharField(max_length=100)
	unit = models.ForeignKey(Unit)
	balance = models.IntegerField()
	currency = models.ForeignKey(Currency)
	price = models.DecimalField(max_digits=20, decimal_places=2)
	stock_record_num = models.CharField(max_length=6)
	optimum_level = models.DecimalField(max_digits=10)
	created = models.DateTimeField(auto_now=False)
	updated = models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return self.name
    
	class Meta:
		ordering = ['name']
		verbose_name = "Commodity"
		verbose_name_plural = "Commodities"

class Program(models.Model):
	program_id = models.IntegerField(max_length=8)
	name = models.CharField(max_length=20)
	description = models.CharField(max_length=254)
	created = models.DateTimeField(auto_now=False)
	updated = models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return self.name
	
	class Meta:
		ordering = ['name']
		verbose_name = "Program"
		verbose_name_plural = "Programs"

class ProjectReference(models.Model):
	name = models.CharField(max_length=254)
	program = models.ForeignKey(Program)
	created = models.DateTimeField(auto_now=False)
	updated = models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return self.name
		
class FromEntity(models.Model):
	name = models.CharField(max_length=254)
	contact_person = models.CharField(max_length=254)
	email = models.EmailField(max_length=254)
	phone = models.CharField(max_length=100)
	def __unicode__(self):
		return self.name
		
		
class Incoming(models.Model):
	commodity = models.ForeignKey(Commodity)
	program = models.ForeignKey(Program)
	pr_num = models.CharField(max_length=10)
	po_num = models.CharField(max_length=10)
	grn_num = models.CharField(max_length=10)
	waybill_num = models.CharField(max_length=10)
	from_entity = models.ForeignKey(FromEntity)
	date_received = models.DateField(auto_now=False)
	quantity = models.IntegerField()
	expiration_date = models.DateField(auto_now=False)
	created = models.DateTimeField(auto_now=False)
	updated = models.DateTimeField(auto_now=True)
	
	class Meta:
		ordering = ['-created', 'program', 'commodity']
		verbose_name = "Incomming Commodity"
		verbose_name_plural = "Incoming Commodities"
	
class Dispatching(models.Model):
	commodity = models.ForeignKey(Commodity)
	program = models.ForeignKey(Program)
	project_reference = models.ForeignKey(ProjectReference)
	date_dispatched = models.DateField(auto_now=False)
	store_release_num = models.CharField(max_length=10)
	waybill_num = models.CharField(max_length=10)
	to_entity = models.CharField(max_length=200)
	quantity = models.IntegerField()
	created = models.DateTimeField(auto_now=False)
	updated = models.DateTimeField(auto_now=True)
	
	class Meta:
		ordering = ['-created', 'program', 'commodity']
		verbose_name = "Dispatching Commodity"
		verbose_name_plural = "Dispatching Commodities"

class Returning(models.Model):
	commodity = models.ForeignKey(Commodity)
	program = models.ForeignKey(Program)
	grn_num = models.CharField(max_length=10)
	from_entity = models.ForeignKey(FromEntity)
	quantity = models.IntegerField()
	date_returned = models.DateField(auto_now=False)
	created = models.DateTimeField(auto_now=False)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-created', 'program', 'commodity']
		verbose_name = "Returning Commodity"
		verbose_name_plural = "Returning Commodities"

### Admin
class CommodityAdmin(admin.ModelAdmin):
    search_fields = ["name"]

admin.site.register(Commodity, CommodityAdmin)