"""tejasangeethawebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import RedirectView
#from django.conf.urls import url
from django.urls import path
from django.views import generic
from django.conf.urls.static import static
from django.views.generic import RedirectView, TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from tejas import views

tejas_patterns = ([
    path('', views.HomeView.as_view(), name='home'),
    path('projectlist', views.project_index, name='project_index'),
    path('<int:pk>', views.project_detail, name='project_detail'),
    path('resume', views.resume, name='resume'),
    path('contact', views.contact, name='contact'),
    path('research', views.ResearchPaperListView.as_view(), name='research'),
    path('researchpaper/<int:pk>', views.ResearchPaperDetailView.as_view(), name='researchpaper'),
    path('postlist', views.PostList.as_view(), name="post_list"),
    path('<slug:slug>', views.post_detail, name='post_detail'),
    path('contacta', views.contactView, name='contacta'),
    path('success', views.successView.as_view(), name='success'),
    ],'tejas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tejas/', include(tejas_patterns)),
    ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path('', RedirectView.as_view(url='/tejas/', permanent=True))
    ]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

