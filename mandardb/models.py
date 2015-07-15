from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class Address(models.Model):
	address_id = models.AutoField(primary_key=True)
	line1 = models.CharField(max_length=50)
	line2 = models.CharField(max_length=50)
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=40)
	zipcode = models.CharField(max_length=10)
	country = models.CharField('2 Digit ISO', max_length=2)


class Person(models.Model):
	person_id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=80)
	middle_name = models.CharField(max_length=80)
	last_name = models.CharField(max_length=80)
	phone_regex = RegexValidator(regex=r'^\+?\d{10,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	mobile1 = models.CharField(max_length=15, validators=[phone_regex])
	mobile2 = models.CharField(max_length=15, validators=[phone_regex])
	landline1 = models.CharField(max_length=15, validators=[phone_regex])
	landline2 = models.CharField(max_length=15, validators=[phone_regex])
	office1 = models.CharField(max_length=15, validators=[phone_regex])
	office2 = models.CharField(max_length=15, validators=[phone_regex])
	home_address = models.ForeignKey(Address, related_name="home_add")
	office_address = models.ForeignKey(Address, related_name="off_add")

class Feed(models.Model):
	feed_id = models.AutoField(primary_key=True)
	feed_title = models.CharField(max_length=150)
	feed_text = models.TextField()
	feed_image = models.URLField()
	upload_date = models.DateField()
	uploaded_by = models.CharField(max_length=100)

class Event(models.Model):
	event_id = models.AutoField(primary_key=True)
	event_name = models.CharField(max_length=150)
	event_venue = models.CharField(max_length=150)
	event_date = models.DateField()
	event_time = models.DateField()
	event_by  = models.CharField(max_length=150)
	event_image = models.URLField()

class Images(models.Model):
	image_id = models.AutoField(primary_key=True)
	img = models.ImageField(upload_to="feeds")

