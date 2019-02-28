from django.contrib.auth.models import Permission, User
from django.db import models
from django import forms
from django.forms import ModelForm

class signin(forms.Form):
    username = forms.CharField(label = 'Username ', max_length = 150)
    password = forms.CharField(widget = forms.PasswordInput)
    widget = { 'Password' : forms.PasswordInput}

class signupp(forms.Form):
    username = forms.CharField(label = 'Username', max_length = 50)
    password = forms.CharField(widget = forms.PasswordInput)
    widget = {'Password' : forms.PasswordInput}
    firstname = forms.CharField(label = 'First Name', max_length = 50)
    lastname = forms.CharField(label = 'Last Name', max_length = 50)
    email = forms.CharField(label = 'Email', max_length = 50)

class UserFollower(models.Model):
    user_id = models.ForeignKey(User, related_name = "users", on_delete=models.SET_NULL,null=True)
    follower_id = models.ForeignKey(User, related_name = "followers", on_delete=models.SET_NULL,null=True)

class post(models.Model):
    owner_id = models.ForeignKey(User, related_name= "owner", on_delete = models.SET_NULL,null=True)
    time_stamp = models.DateTimeField(auto_now_add = True)
    likes = models.PositiveSmallIntegerField(default=0)
    caption = models.CharField(max_length = 100)
    photo = models.FileField(upload_to='Documents/')

class upload_post(forms.ModelForm):
    class Meta:
        model = post
        fields = ['photo','caption']

# class Like(models.Model):
#     liked_by = models.ForeignKey(User, related_name= "liked_by", on_delete = models.SET_NULL, null=True)
#     picture = models.ForeignKey(post, related_name= "picture", on_delete = models.SET_NULL, null=True)
#     created = models.DateTimeField(auto_now_add = True)

class Profile_Picture(models.Model):
    main_owner = models.ForeignKey(User, related_name= "main_owner", on_delete=models.SET_NULL,null = True)
    profilepic = models.FileField(upload_to ='Documents/')

class Pro_Pic(forms.Form):
    profilepic = forms.FileField()

class Comments(models.Model):
    main_ownerr = models.ForeignKey(User, related_name= "main_ownerr", on_delete=models.SET_NULL,null = True)
    main_pic = models.ForeignKey(post, related_name= "main_pic", on_delete = models.SET_NULL, null=True)
    comment = models.CharField(max_length = 100)

class comments_form(forms.Form):
    commentss = forms.CharField(max_length = 100)
