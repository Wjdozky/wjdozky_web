"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from myblog import views
from django.conf import settings  # new
from django.urls import path # new
from django.conf.urls.static import static  # new
from myblog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.blog_postListView.homeview,name='home'),
    path('article/<int:id>',views.articleListView.article,name='article'),
    path('about/',views.about_meListView.about,name='about'),
    path('article/',views.cateArticleListView.cate_article,name='ar'),
    path('music/',views.cateMusicListView.cate_article,name='mu'),
    path('search/',views.get_queryset,name='search_results')
    # path('',views.home_pageListView.as_view(),name='index'),
]
if settings.DEBUG:  # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)