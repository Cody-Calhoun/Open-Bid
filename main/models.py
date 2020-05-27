from django.db import models
import re
from datetime import datetime


class User_manager(models.Manager):
    def con_validator(self, post_data):
        errors = {}
        arr = Contractor.objects.all()
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(post_data['bname']) < 2:
            errors['bname'] = 'Business name needs to be at least 2 characters.'
        if len(post_data['alias']) < 2:
            errors['alias'] = 'Alias needs to be at least 2 characters.'
        if not EMAIL_REGEX.match(post_data['email']):          
            errors['email'] = "Invalid email address!"
        for user in arr:
            if user.email == post_data['email']:
                errors['email'] = 'Email alread exists. Please use another.'
        if len(post_data['password']) < 8:
            errors['password'] = 'Password needs to be at least 8 characters.'
        if len(post_data['city']) < 4:
            errors['city'] = 'Please provide full name of city.'
        if len(post_data['state']) < 4:
            errors['state'] = 'Please provide full name of state.'
        return errors

    def cus_validator(self, post_data):
        errors = {}
        arr = Customer.objects.all()
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(post_data['fname']) < 2:
            errors['fname'] = 'First name needs to be at least 2 characters.'
        if len(post_data['lname']) < 2:
            errors['lname'] = 'Last name needs to be at least 2 characters.'
        if not EMAIL_REGEX.match(post_data['email']):          
            errors['email'] = "Invalid email address!"
        for user in arr:
            if user.email == post_data['email']:
                errors['email'] = 'Email alread exists. Please use another.'
        if len(post_data['password']) < 8:
            errors['password'] = 'Password needs to be at least 8 characters.'
        if len(post_data['city']) < 4:
            errors['city'] = 'Please provide full name of city.'
        if len(post_data['state']) < 4:
            errors['state'] = 'Please provide full name of state.'
        return errors




class Contractor(models.Model):
    bname = models.CharField(max_length = 25)
    alias = models.CharField(max_length = 25)
    city = models.CharField(max_length = 25)
    state = models.CharField(max_length = 25)
    zipcode = models.IntegerField()
    email = models.CharField(max_length = 25)
    password = models.CharField(max_length = 50)
    objects = User_manager()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Customer(models.Model):
    fname = models.CharField(max_length = 25)
    lname = models.CharField(max_length = 25)
    city = models.CharField(max_length = 25)
    state = models.CharField(max_length = 25)
    zipcode = models.IntegerField()
    email = models.CharField(max_length = 25)
    password = models.CharField(max_length = 50)
    objects = User_manager()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Project(models.Model):
    title = models.CharField(max_length = 50)
    location = models.CharField(max_length = 50)
    measurements = models.TextField()
    description = models.TextField()
    customer = models.ForeignKey(Customer, related_name='projects', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Bid(models.Model):
    price = models.IntegerField()
    scope = models.TextField()
    contractor = models.ForeignKey(Contractor, related_name='bids', on_delete=models.CASCADE)
    project = models.ForeignKey(Project, related_name="bids", on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Specialty(models.Model):
    title = models.CharField(max_length = 20)
    projects = models.ManyToManyField(Project, related_name="specialties")
    contractors = models.ManyToManyField(Contractor, related_name='specialties')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Review(models.Model):
    title = models.CharField(max_length = 20)
    customer = models.ForeignKey(Customer, related_name='reviews', on_delete=models.CASCADE)
    contractor = models.ForeignKey(Contractor, related_name='reviews', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)