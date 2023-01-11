Виды функций:
    Рендер HTML страницы.
from django.shortcuts import render

def title_menu(request):
    return render(request, 'title/title.html')



    Вывод простого HttpResponse запроса
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello world')



    Рендер простого шаблона с использованием переменной в цикле.
def index(request):
    news = News.objects.all()
    res = '<h1>Список новостей</h1>'
    for item in news:
        res += f'<div\n><p>{item.title}</p>\n<p>{item.content}</p>\n</div>\n<hr>\n'
    return HttpResponse(res)



    Рендер HTML шаблона с использованием переменной.
def index(request):
    news = News.objects.all()
    return render(request, 'news/title.html', {'news': news},{'title': 'Список новостей'})

    Более сложный рендер HTML шаблона с динамическим URL
def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    return render(request, 'news/category.html', {'news': news, 'categories': categories,
                                                  'category': category})





    Вывод 404 при отсутствии страницы

from django.shortcuts import render, get_object_or_404

def view_article(request, article_id):
    article_item = get_object_or_404(Article, pk=article_id)
    content = {'article_item': article_item
               }
    return render(request, 'mysite/view_article.html', content)
