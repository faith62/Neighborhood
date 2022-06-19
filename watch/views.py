from multiprocessing import context
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from watch.models import Posts
from .decorators import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail,BadHeaderError

@unauthenticated_user
def signup(request):
    form = SignUpForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')

            user_profile=Profile(
                user=user,
                name=username
            )
            user_profile.save_profile()

            subject = 'Welcome to IG'
            recipient_list = email
            message = '''   
            Hello,

                Welcome to Neighborhood

                Thank you for signing up. 
                We are excited to welcome you to the family.

                Karibu Nyumba kumi
                        
                    '''
            from_email = 'no-reply@example.com'
            try:
                send_mail(subject, message, from_email, [recipient_list])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

            messages.success(request, "Account created successfully")
            return redirect('login')

    context = {
        'form': form,
    }
    return render (request, 'accounts/signup.html', context=context)

@unauthenticated_user
def loginuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            messages.info(request, "Username or Password is incorrect")
            
    context = {}
    return render (request, 'accounts/login.html', context=context)

def logoutuser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def profile(request,id):
    user_profile = Profile.objects.get(id=id)

    context={
        'user_profile':user_profile,
    }
    return render(request,'profile.html',context=context)

@login_required(login_url='login')
def profile_update(request,username):
    user_name = User.objects.get(username=username)
    user_profile = Profile.objects.get(user=user_name.id)

    data = get_object_or_404(Profile, id=user_profile.id)
    profile_form = ProfileUpdateForm(instance=data)

    if request.method == "POST":
        profile_form = ProfileUpdateForm(request.POST,request.FILES, instance=data)
        if profile_form.is_valid():
            profile_form.save()
            
            return redirect ('profile_update', username=user_name)

    context={
        'user_name':user_name,
        'profile_form':profile_form,
        'user_profile':user_profile
    }
    return render(request,'profile_update.html',context=context)

def homepage(request):
    posts = Posts.objects.all().order_by('id').reverse()
    neighbourhoods=Neighbourhood.objects.all
    context={
        'posts':posts,
        'neighbourhoods':neighbourhoods
    }
    return render(request,'watch/index.html',context=context)

def post_create(request):
    post_create_form = PostCreateForm()

    if request.method == "POST":
        post_create_form = PostCreateForm(request.POST,request.FILES)
        if post_create_form.is_valid():
            post_user = request.user
            
            image = post_create_form.cleaned_data.get('image')
            title = post_create_form.cleaned_data.get('title')
            description = post_create_form.cleaned_data.get('description')
            profile = Profile.objects.get(user=post_user)
            neighborhood = Neighbourhood.objects.get(neighborhood=post_user.neighborhood.name)
            
            new_post = Posts(
                image=image,
                title=title,
                description=description,
                profile=profile,
                neighborhood=neighborhood
            )
            new_post.save_post()
            return redirect('homepage')

    context={
        'post_create_form':post_create_form
    }
    return render(request,'watch/post_create.html',context=context)

def bussiness_create(request):
    business_create_form = BusinessCreateForm()

    if request.method == "POST":
        business_create_form = BusinessCreateForm(request.POST,request.FILES)
        if business_create_form.is_valid():
            user = request.user
            
            bsn_name = business_create_form.cleaned_data.get('bsn_name')
            bsn_email = business_create_form.cleaned_data.get('bsn_email')
            phone = business_create_form.cleaned_data.get('phone')
            weburl = business_create_form.cleaned_data.get('weburl')
            category = business_create_form.cleaned_data.get('category')
            bsn_image = business_create_form.cleaned_data.get('bsn_image')
            profile = Profile.objects.get(user=user)
            neig_id = Neighbourhood.objects.get(name=profile.neighborhood.name)
            
            new_bus = Business(
                bsn_name=bsn_name,
                bsn_email=bsn_email,
                phone=phone,
                weburl=weburl,
                category=category,
                bsn_image=bsn_image,
                profile=profile,
                neig_id=neig_id
            )
            new_bus.create_business()
            return redirect('user_profile',user.id)

    context={
        'business_create_form':business_create_form
    }
    return render(request,'watch/bussiness_create.html',context=context)

def police(request):
    police_station=Business.objects.filter(category='Police Station')
    context={'police_station':police_station}
    return render(request,'amenities/police.html',context=context)

def hair_and_grooming(request):
    hair_and_grooming=Business.objects.filter(category='Hair&Grooming')
    context={'hair_and_grooming':hair_and_grooming}
    return render(request,'amenities/hair&grooming.html',context=context)

def hospital(request):
    hospital=Business.objects.filter(category='Hospital')
    context={'hospital':hospital}
    return render(request,'amenities/hospital.html',context=context)

def malls_and_markets(request):
    malls=Business.objects.filter(category='Mall&Markets')
    context={'malls':malls}
    return render(request,'amenities/malls.html',context=context)

def fastfood(request):
    fastfood=Business.objects.filter(category='Fast Foods')
    neighbourhood = Neighbourhood.objects.all()
    context={
        'fastfood':fastfood,
        'neighbourhood':neighbourhood
        }
    return render(request,'amenities/fastfood.html',context=context)

def hood(request,hoodname):
    hoodname_id = Neighbourhood.objects.get(name=hoodname)
    hood_people = Profile.objects.filter(neighborhood=hoodname_id)
    hood_business = Business.objects.filter(neig_id=hoodname_id)

    context={
        'hood_people':hood_people,
        'hood_business':hood_business
    }
    return render(request,'watch/hood.html',context=context)