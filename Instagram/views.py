from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import UserFollower, post, upload_post, signin, signupp, Profile_Picture, Comments,comments_form, Profile_Picture, Pro_Pic
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.conf import settings
from django.conf.urls.static import static

def loginuser(request):
    if request.method == 'POST':
        form = signin(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            username = request.POST['username']
            password = request.POST['password']
            print(username)
            print(password)
            user = authenticate(request, username = username, password = password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect('/Instagram/'+username+ '/')
            else:
                return redirect('/Instagram/loginuser/')
    else:
        form = signin()
    return render(request, "login.html",{'signin': form})

def signup(request):
    if request.method == 'POST':
        form = signupp(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            email = form.cleaned_data['email']
            a = User.objects.create(username = username, password = password, first_name = firstname, last_name = lastname, email = email)
            a.set_password(form.cleaned_data['password'])
            a.is_staff = True
            a.is_superuser = True
            a.save()

            return redirect('/Instagram/loginuser/')
    else:
        form = signupp()
    return render(request, "signup.html", {'signup': form})

def profile(request,username):
    username = request.user.username
    user = User.objects.exclude(username = request.user)
    count_follow = request.user.users.count()
    count_follower = request.user.followers.count()
    all_followings = request.user.followers.all()
    img_post = post.objects.filter(owner_id=request.user).order_by('-time_stamp')
    namee = Comments.objects.all()
    pro = Profile_Picture.objects.filter(main_owner = request.user)
    return render(request, "profile.html", {'username': request.user.username , 'user': user, 'count_follow': count_follow, 'count_follower': count_follower,'all_followings' : all_followings, 'img_post':img_post, 'media_url':settings.MEDIA_URL,'namee':namee,'pro':pro})

def signout(request):
    logout(request)
    return redirect('/Instagram/loginuser/')

def follow_Unfollow(request,num):
    a = User.objects.get(id = num)
    if UserFollower.objects.filter(user_id=request.user,follower_id=a).exists():
        UserFollower.objects.filter(user_id=request.user,follower_id=a).delete()
        return redirect('/Instagram/profile/')
    else :
        b = UserFollower(user_id = request.user , follower_id = a)
        b.save()
        return redirect('/Instagram/profile/')

def following(request):
    all_followers = request.user.users.all()
    return render(request, "followings.html", {'all_followers':all_followers})

def follower(request):
    all_followings = request.user.followers.all()
    return render(request, "followers.html", {'all_followings':all_followings})

def upload(request):
    formm = upload_post(request.POST, request.FILES)
    if formm.is_valid():
        formm.save()
        return redirect('/Instagram/profile/')
    return render(request, 'addpost.html', {'formm': formm})

def pro_picture(request):
    form = Pro_Pic(request.POST, request.FILES)
    if form.is_valid():
        main_owner = request.user
        profilepic = form.cleaned_data['profilepic']
        a = Profile_Picture.objects.create(main_owner = main_owner, profilepic = profilepic)
        a.save()
        return redirect('/Instagram/profile/')
    else:
        form = Pro_Pic()
    return render(request, "profile_upload.html", {'form' :form})

def like(request,num):
    a = post.objects.get(id = num).likes
    a+=1
    post.objects.filter(id = num).update(likes = a)
    return redirect('/Instagram/timeline/')


def timeline(request):
    # a = post.objects.all()
    img_post = post.objects.all()
    namee = Comments.objects.all()
    # count_like = Like.objects.filter(likes = a).count()
    return render(request, "timeline.html", {'img_post':img_post,'namee':namee,'media_url': settings.MEDIA_URL})

def comment(request, num):
    if request.method == 'POST':
        form = comments_form(request.POST)
        if form.is_valid():
            commentss = form.cleaned_data['commentss']
            main_ownerr = request.user
            main_pic = post.objects.get(id = num)
            a = Comments.objects.create(comment = commentss, main_ownerr = main_ownerr, main_pic = main_pic)
            a.save()
            return redirect('/Instagram/timeline/')
    else:
        form = comments_form()
    return render(request, "Comments.html", {'form': form})
