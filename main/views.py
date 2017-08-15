from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from main.models import *
from django.db.models import F
from django.http import HttpResponse
from django.utils.translation import ugettext
from django.conf import settings
from django.utils import translation
from django.utils.translation import ugettext as _
from django.utils.translation import activate
# Create your views here.
# from django.views.decorators.cache import cache_page


# ----------------------------------------------------------------------------------------------
def get_news_line():
    news_line_data = Content.objects.filter(news_line=True).values(
        'id', 'title', 'desc', 'img', 'video')
    return news_line_data


# @cache_page(20)
def index(request):
    general_slider_data = Content.objects.filter(general_slider=True).values(
        'id', 'title', 'img', 'video')
    news_line_data = get_news_line()
    context = {
        'general_slider_data': general_slider_data,
        'news_line_data': news_line_data,
    }
    return render(request, 'main/index.html', context)


# @cache_page(20)
def article(request, article_id):
    try:
        article = Content.objects.get(pk=article_id)

    except Content.DoesNotExist:
        return redirect('/')

    context = {'article': article}
    response = render(request, 'main/article.html', context)
    response.set_cookie(key='article_id', value=article_id)
    return response


# def program(request, category_id, lang):
#     try:
#         category_obj = Category.objects.get(id=category_id)
#     except Category.DoesNotExist:
#         return redirect('/%s/' % lang)
#     categories = Content.objects.filter(category=category_obj, lang__name=lang).order_by('-id')
#     paginator = Paginator(categories, 10) # Show 25 contacts per page

#     page = request.GET.get('page')
#     try:
#         contacts = paginator.page(page)
#     except PageNotAnInteger:
#         # If page is not an integer, deliver first page.
#         contacts = paginator.page(1)
#     except EmptyPage:
#         # If page is out of range (e.g. 9999), deliver last page of results.
#         contacts = paginator.page(paginator.num_pages)
#     right_data = right_view(lang)
#     context = {'categories': contacts,
#                'lang': lang,
#                'category': category_obj,
#                'right_data': right_data,
#                'users': contacts,
#                'contacts': contacts}
#     return render(request, 'blog/category.html', context)


# def category(request, category_id, lang):
#     try:
#         category_obj = Category.objects.get(id=category_id)
#     except Category.DoesNotExist:
#         return redirect('/%s/' % lang)
#     categories = Content.objects.filter(category=category_obj, lang__name=lang).order_by('-id')
#     paginator = Paginator(categories, 10) # Show 25 contacts per page

#     page = request.GET.get('page')
#     try:
#         contacts = paginator.page(page)
#     except PageNotAnInteger:
#         # If page is not an integer, deliver first page.
#         contacts = paginator.page(1)
#     except EmptyPage:
#         # If page is out of range (e.g. 9999), deliver last page of results.
#         contacts = paginator.page(paginator.num_pages)
#     right_data = right_view(lang)
#     context = {'categories': contacts,
#                'lang': lang,
#                'category': category_obj,
#                'right_data': right_data,
#                'users': contacts,
#                'contacts': contacts}
#     return render(request, 'blog/category.html', context)


def program(request, program_id):
    try:
        category_obj = Category.objects.get(id=program_id)
    except Category.DoesNotExist:
        return redirect('/')
    categories = Content.objects.filter(category=category_obj).order_by('-id')

    paginator = Paginator(categories, 1) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        data = paginator.page(paginator.num_pages)

    context = {'data': data}
    response = render(request, 'main/program.html', context)
    # response.set_cookie(key='article_id', value=article_id)
    return response
