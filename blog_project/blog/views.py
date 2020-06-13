from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from blog.models import Post,UserProfile
from django.contrib import messages


# Create your views here.
@login_required(login_url="/user_login/")
def home(request):
	my_dict=dict()
	my_dict['posts']=Post.objects.all()
	return render(request,'home.html',my_dict)


@login_required(login_url="/user_login/")
def create_post(request):
	if request.method=='POST':
		title=request.POST.get('title')
		text=request.POST.get('text')
		new_post=Post.objects.create(
			title=title,
			text=text,
			user=request.user
		)
		return redirect('home')

	return render(request,'create_post.html')


def user_registration(request):
	my_dict=dict()
	if request.method=='POST':

		username=request.POST.get('username')
		check_username=User.objects.filter(username=username).exists()
		if check_username:
			my_dict['invalid_username']=True
			return render(request,'user_registration.html',my_dict)

		email=request.POST.get('email')
		check_email=User.objects.filter(email=email).exists()
		if check_email:
			my_dict['invalid_email']=True
			return render(request,'user_registration.html',my_dict)

		new_user=User.objects.create(
			username=username,
			email=email

		)
		new_user.set_password(request.POST.get('password'))
		new_user.save()
		new_user_profile = UserProfile.objects.create(
			user=new_user
		)
		return redirect('user_login')
	return render(request,'user_registration.html',my_dict)


def user_login(request):
	my_dict=dict()
	if request.method=='POST':
		username=request.POST.get('username')
		password=request.POST.get('password')
		try:
			user=authenticate(username=username,password=password)
			login(request,user)
			return redirect('home')
		except:
			my_dict['invalid_details']=True
			return render(request,'user_login.html',my_dict)
	return render(request,'user_login.html',my_dict)

@login_required(login_url="/user_login/")
def user_logout(request):
	logout(request)
	return redirect('user_login')


@login_required(login_url="/user_login/")
def user_dashboard(request):
	my_dict=dict()
	my_dict['my_posts']=Post.objects.filter(user=request.user).order_by('-created_at')
	return render(request,'user_dashboard.html',my_dict)


@login_required
def user_profile(request):	
	if request.method=='POST':
		print(request.FILES.get('profile_pic'))
		check_user_profile = UserProfile.objects.filter(user=request.user).exists()
		if not check_user_profile:
			user_profile = UserProfile.objects.create(user=request.user)
		else:
		user_profile = UserProfile.objects.get(user=request.user)
		user_profile.first_name=request.POST.get('first_name')
		user_profile.last_name=request.POST.get('last_name')
		user_profile.contact_phone=request.POST.get('contact_phone')
		user_profile.profile_pic=request.FILES['profile_pic']
		user_profile.about=request.POST.get('about')
		user_profile.save()
		return redirect('user_dashboard')
	return render(request,'user_profile.html')

def post_details(request, pk):
	context_data = dict()
	try:
		post = Post.objects.get(pk=pk)
	except Post.DoesNotExist:
		post = None

	if post is None:
		context_data['invalid_request'] = True
		return render(request, 'post_details.html', context_data)
	post.views += 1
	post.save()
	context_data['post'] = post
	return render(request, 'post_details.html', context_data)

@login_required(login_url="/user_login/")
def post_delete(request, pk):
	my_dict=dict()
	try:
		post=Post.objects.get(pk=pk)
	except Post.DoesNotExist:
		post=None
	if post is None:
		return redirect('not_found')
	else:
		if request.user == post.user:
			post.delete()
			messages.success(request,'Your post was deleted successfully')
			return redirect('user_dashboard')
	return redirect('not_found')

def not_found(request):
	return render(request,'not_found.html')

@login_required(login_url="/user_login/")
def post_edit(request,pk):
	my_dict=dict()
	try:
		post=Post.objects.get(pk=pk)
	except Post.DoesNotExist:
		return redirect('not_found')

	if not request.user == post.user:
		return redirect('not_found')

	my_dict['post']=post

	if request.method=='POST':
		post.title=request.POST.get('title')
		post.text=request.POST.get('text')
		post.save()
		return redirect('user_dashboard')

	return render(request,'post_edit.html',my_dict)
	





