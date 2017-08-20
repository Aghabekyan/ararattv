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
from django.views.decorators.cache import cache_page
from datetime import datetime, timedelta, time

# --------------- Methods ------------------


def get_news_line(limit):
    news_line_data = Content.objects.filter(news_line=True).values(
        'id', 'title', 'desc', 'img', 'video', 'publish_date').order_by('-publish_date')[:limit]
    return news_line_data


def get_general_slider(limit):
    general_slider_data = Content.objects.filter(general_slider=True).values(
        'id', 'title', 'img', 'video', 'publish_date').order_by('-publish_date')[:limit]
    return general_slider_data


def get_program(program_id, limit):
    data = Content.objects.filter(category=program_id).values(
        'id', 'title', 'img', 'video', 'publish_date').order_by('-publish_date')[:limit]
    return data


def get_most_viewed(limit):
    data = Content.objects.filter().values(
        'id', 'title', 'img', 'video', 'publish_date').order_by('-hit_count')[:limit]
    return data


def get_article_related(program_id, limit):
    data = Content.objects.filter(category=program_id).values(
        'id', 'title', 'img', 'video', 'publish_date').order_by('-publish_date')[:limit]
    return data


def get_program_date():
    print '-----------------------============----------------'
    today = datetime.now().date()
    tomorrow = today + timedelta(1)
    today_start = datetime.combine(today, time())
    today_end = datetime.combine(tomorrow, time())
    data = Program.objects.filter(date__gte=today_start, date__lt=today_end).values(
        'id', 'title', 'date')
    return data

# --------------- Views ------------------


@cache_page(60*60*24)
def index(request):
    general_slider_data = get_general_slider(5)
    news_line_data = get_news_line(15)
    haylur_data = get_program(4, 16)
    program_date_data = get_program_date()
    program_1_data = get_program(1, 4)
    program_2_data = get_program(2, 4)
    program_3_data = get_program(3, 4)
    program_4_data = get_program(4, 4)
    program_5_data = get_program(5, 4)
    program_6_data = get_program(6, 4)
    most_viewed_data = get_most_viewed(4)

    context = {
        'general_slider_data': general_slider_data,
        'news_line_data': news_line_data,
        'haylur_data': haylur_data,
        'program_date_data': program_date_data,
        'program_1_data': program_1_data,
        'program_2_data': program_2_data,
        'program_3_data': program_3_data,
        'program_4_data': program_4_data,
        'program_5_data': program_5_data,
        'program_6_data': program_6_data,
        'most_viewed_data': most_viewed_data,
    }
    return render(request, 'main/index.html', context)


@cache_page(60*60*24)
def article(request, article_id):
    try:
        article = Content.objects.get(pk=article_id)
        article_related_data = get_article_related(article.category.all().first(), 14)
    except Content.DoesNotExist:
        return redirect('/')

    context = {'article': article,
               'article_related_data': article_related_data}
    response = render(request, 'main/article.html', context)
    response.set_cookie(key='article_id', value=article_id)
    return response


@cache_page(60*60*24)
def program(request, program_id):
    try:
        category_obj = Category.objects.get(id=program_id)
    except Category.DoesNotExist:
        return redirect('/')
    categories = Content.objects.filter(category=category_obj).order_by('-id')

    paginator = Paginator(categories, 20) # Show 25 contacts per page
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


def hitcounter(request):
    if request.POST and request.is_ajax:
        id = request.POST.get('id')
        current_model = Content.objects.get(pk=id)
        current_model.hit_count = current_model.hit_count + 1
        current_model.save()
        return HttpResponse(id)
    else:
        return 0
