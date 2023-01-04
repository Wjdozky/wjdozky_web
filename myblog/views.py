from django.core.paginator import Paginator
import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView
from .models import blog_post,home,about_me

date=datetime.datetime.now()
yas=date.strftime('%Y')
class blog_postListView(ListView):
    model = blog_post
    template_name = "home.html"
    def homeview(request):
        myhome=home.objects.get(id=1)
        mypost=blog_post.objects.all().order_by('-id')
        paginator=Paginator(mypost,6)
        templatelist=['home.html','master.html','about.html','article.html','cate_article.html','cate_music.html']
        template=loader.select_template(templatelist)
        page_number=request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context= {'myhome':myhome,'mypost':mypost,'date':yas,'page_obj': page_obj}
        return HttpResponse(template.render(context,request))


def get_queryset(request):
    myhome=home.objects.get(id=1)
    query=request.GET.get('q')
    object_list=blog_post.objects.filter(title__icontains=query).order_by('-id')
    paginator=Paginator(object_list,6)
    page_number=request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    templatelist=['search.html','master.html','about.html','article.html','cate_article.html','cate_music.html']
    template=loader.select_template(templatelist)
    context= {'myhome':myhome,'object_list':object_list,'date':yas,'page_obj': page_obj}
    return HttpResponse(template.render(context,request))
    

    
class articleListView(ListView):
    model = blog_post
    template_name = "article.html"
    def article(request,id):
        mymember=blog_post.objects.get(id=id)
        mylist=blog_post.objects.all().order_by('-id')
        myhome=home.objects.get(id=1)

        templatelist=['article.html']
        template=loader.select_template(templatelist)
        context = {'myhome':myhome,'mymember':mymember,'date':yas,'mylist':mylist}
        return HttpResponse(template.render(context,request))

class cateArticleListView(ListView):
    model = blog_post
    template_name = "cate_article.html"
    def cate_article(request):
        myhome=home.objects.get(id=1)
        mypost=blog_post.objects.all().order_by('-id')
        paginator=Paginator(mypost,6)
        templatelist=['cate_article.html','home.html','master.html','about.html','article.html','cate_music.html']
        template=loader.select_template(templatelist)
        page_number=request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context= {'myhome':myhome,'mypost':mypost,'date':yas,'page_obj': page_obj}
        return HttpResponse(template.render(context,request))

class cateMusicListView(ListView):
    model = blog_post
    template_name = "cate_music.html"
    def cate_article(request):
        myhome=home.objects.get(id=1)
        mypost=blog_post.objects.all().order_by('-id')
        paginator=Paginator(mypost,6)
        templatelist=['cate_music.html','home.html','master.html','about.html','article.html','cate_article.html',]
        template=loader.select_template(templatelist)
        page_number=request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context= {'myhome':myhome,'mypost':mypost,'date':yas,'page_obj': page_obj}
        return HttpResponse(template.render(context,request))


class about_meListView(ListView):
    model = about_me
    template_name = "about.html"
    def about(request):
        myabout=about_me.objects.get(id=1)
        myhome=home.objects.get(id=1)
        templatelist=['about.html']
        template=loader.select_template(templatelist)
        context={'myhome':myhome,'myabout':myabout,'date':yas}
        return HttpResponse(template.render(context,request))

  



