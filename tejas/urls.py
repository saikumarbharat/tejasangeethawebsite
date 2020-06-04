from django.urls import path
from . import views
from django.views import generic
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path
from django.contrib import admin
from django.urls import include
from django.urls import include, path, re_path
from django.views.generic import RedirectView, TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import contact, contactView, successView
#from blog.views import UserCreateView
#from tejas.views import PersonCreateView

urlpatterns = [
    path('projectlist/', views.project_index, name='project_index'),
    path('<int:pk>/', views.project_detail, name='project_detail'),
    path('resume/', views.resume, name='resume'),
    path('contact/', views.contact, name='contact'),
    path('research/', views.ResearchPaperListView.as_view(), name='research'),
    path('researchpaper/<int:pk>', views.ResearchPaperDetailView.as_view(), name='researchpaper-detail'),
    path('', views.index, name='index'),
    path('postlist/', views.PostList.as_view(), name="post_list"),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('contacta/', contactView, name='contacta'),
    path('success/', successView, name='success'),
    ]

