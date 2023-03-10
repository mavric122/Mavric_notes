Как рендерить шаблон:
def index(request):
    news = News.objects.all()
    return render(request, 'news/index.html', {'news': news, 'title': 'Список новостей'})

В качестве параметров мы передаём

1)request
2)Путь к шаблону
3)Контекст

Если контекста много, то его можно использовать как переменную. 
Пример:

def index(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей'
    }
    return render(request, 'news/index.html', context)










































Основные теги шаблона:
Запуск цикла для вывода каждого объекта с помощью перменных.
{% for item in news %} 
---------------------------------------------------------------------------------
{{block… }}  ???
---------------------------------------------------------------------------------
{% autoescape off %} – это отключает автоэкранирование кода.
           <title>{{ title }}</title>
{% endautoescape %} – Конец отключения автоэкранирования кода

---------------------------------------------------------------------------------
{% comment %} – это включает комментирование кода
     Всё что тут закоментировано и будет игнорироваться 
{% endcomment %} – это отключает комментирование кода

---------------------------------------------------------------------------------
{{ item.created_at | date:"Y-m-d H:i:s" }} - Где Y-год, m-месяц, d-день, H-час, i-минуты, s-секунды
---------------------------------------------------------------------------------
Проверка наличия переменной и вывод при наличии:
{% if article_item.examples %}
h5 class="card-title">{{ article_item.examples }}</h5>
{% endif %}



























Как установить дополнительные пути к шаблону не по умолчанию:
В settings.py в разделе TEMPLATES = [ есть подменю ‘DIRS’ где дописываем 

'DIRS': [os.path.join(BASE_DIR, 'templates')],
 
где templates это папка где лежат шаблоны.
______________________________________________________________________________
Пример шаблона:
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ title }}</title>
</head>
<body>

<h1>{{ title }}</h1>

{{news}}

</body>
</html>
_____________________________________________________________________________________
Циклы:
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ title }}</title>
</head>
<body>

<h1>{{ title }}</h1>

{% for item in news %}
<div>
    <p>{{ item.title }}</p>
    <p>{{ item.content }}</p>
    <p>{{ item.created_at }}</p>
</div>
<hr>
{% endfor %}

</body>
</html>
_____________________________________________________________________________
Дата/время:

<p>{{ item.created_at | date:"Y-m-d H:i:s" }}</p>

Где Y-год, m-месяц, d-день, H-час, i-минуты, s-секунды

| - Это фильтр он используется, что бы изменить значения переменной или строки. Мы можем использовать несколько фильтров.


Создание ссылок по id

<a href="/category/{{ item.pk }}" class="

Css в шаблоне
Как подключить статику css в Django читай в settings или смотри {{Django лучший курс урок 22}}
В html странице на первой строчке (или второй если бесит ошибка) помещаем:
{% load static %}
В файле прописываем
<link rel="stylesheet "href="{% static 'bootstrap/css/bootstrap.min.css' %}">
И другие необходимые.
Это путь без /static/  - во всех местах, за это отвечает STATIC_URL в settings/Django.

