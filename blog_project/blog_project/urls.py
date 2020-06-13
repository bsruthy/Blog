"""blog_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog.views import(
	home,
	create_post,
	user_registration,
	user_login,
	user_logout,
	user_dashboard,
    user_profile,
    post_details,
    post_delete,
    not_found,
    post_edit,
	)
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home,name='home'),
    path('create_post/',create_post,name='create_post'),
    path('user_registration/',user_registration,name='user_registration'),
    path('user_login/',user_login,name='user_login'),
    path('user_logout/',user_logout,name='user_logout'),
    path('user_dashboard/',user_dashboard,name='user_dashboard'),
    path('user_profile/',user_profile,name='user_profile'),
    path('post_details/<int:pk>/', post_details, name='post_details'),
    path('post_delete/<int:pk>/',post_delete,name='post_delete'),
    path('not_found/',not_found,name='not_found'),
    path('post_edit/<int:pk>/',post_edit,name='post_edit'),


] + static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)
