Модели в классе описываются классом.
Все модели являются подклассом models из django.db.
В модели мы описываем все атрибуты класса (свойства).
Атрибуты модели представляют собой соответствующие поля в таблицах  базы данных.
Например:
    1. Id – INT (интеджер)(цифровое значение)
    2. title – Varchar (небольшой текст)
    3. content – Text (большое текст)
    4. created_at – Datetime (дата и время)
    5. creater_date – (Дата)
    6. updated_at  - DataTime
    7. photo – Image
    8. is_published – Boolean
Атрибут id создаётся автоматически.  Прописывать его не надо.
Справочник по типам полей
https://django.fun/docs/django/ru/3.1/ref/models/fields/#model-field-types
Каждый атрибут может принимать и опции полей.
Порядок построения модели
------------------------------------------------------------------------------------------------------------------------------------
Пример:

class Categorys(models.Model):
    title = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']  # Сортировка по title

    def __str__(self):
        return self.title


    1) Идет сам класс
    2) Класс Meta
    3) def __str__

------------------------------------------------------------------------------------------------------------------------------------

Параметры атрибутов:

(blank=True) = Поле не обязательно к заполнению.
(max_length=150) = Максимальное количество символов.
(auto_now_add=True) = Единоразово при создании будет заполнено.
(auto_now=True) = При создании и обновлении будет заполнено.
(upload_to='photos/%Y/%m/%d/') = Куда загружать картинку/файл.
(db_index=True) = Для этого поля будет создан индекс базы данных. Делает более быстрым для поиска.
(default=1) = Значение по умолчанию, если поле не заполнено. Вместо 1 – нужное значение.

------------------------------------------------------------------------------------------------------------------------------------


Пример модели:
# Модель статьи.
class Article(models.Model):
   title = models.CharField(max_length=90, verbose_name='Наименование')
   content = models.TextField(verbose_name='Описание')
   examples = models.TextField(verbose_name='Примеры', blank=True)
   solution = models.TextField(verbose_name='Решение', blank=True)
   created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Фото')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано?')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'
        ordering = ['created_at']  # Сортировка по дате создания

    def __str__(self):
        return self.title



------------------------------------------------------------------------------------------------------------------------------------



Работа с моделями через командную строку:
>>> python manage.py shell   - Вызывает командную строку
>>> from name.models import Name – Импортируем модель где name/Name = имя модели
>>> news(title='Новость 1', content='Контент новости 1')  - Добавление данных в базу Sqlite
>>> news1 = _ - Сохранение данных в переменную, где _ это псевдопеременная в которой хранится предыдущий результат.
>>> news1.save() – Сохранение данных в базе
>>> from django.db import connection
>>> connection.queries – Список словарей с Sql и Time всех записей
>>> news3 = News()
>>> news3.title = 'Новость 3'
>>> news3.content = 'Контент новости 3'
>>> news3.save() – Второй вариант добавления в базу.
>>> news4 = News.objects.create(title='Новость 4', content = 'Контент новости 4') – Третий вариант добавления в базу. При таком подходе не нужно дополнительно сохранять в базе.
>>> News.objects.get(id=3) = Обращение к базе по ключам
>>> News.objects.get(pk=4)  = Обращение к базе по ключам. pk – общепринятое определение id.
<News: News 2>
>>> news4 = _
>>> news4.title = 'Новость 4'
>>> news4.save()  - Изменение записей в базе.

>>> news6 = News.objects.get(pk=6)
>>> news6.delete() – Удаление записей из базы.

------------------------------------------------------------------------------------------------------------------------------------




Изменение названий в админке.
В models.py создаём внутри нашего класса:
class Meta:
    verbose_name = 'Новость'
    verbose_name_plural = 'Новости'
    ordering = ['-created_at']



verbose_name = наименование модели в единственном числе. После этого в админке наименование “News” будет  “Новость”
verbose_name_plural = Наименование модели в множественном числе.
ordering =  Порядок сортировки.
------------------------------------------------------------------------------------------------------------------------------------
Колонки в админке с дополнительными данными.

В admin.py:

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_published')


admin.site.register(News, NewsAdmin)

(Из admin.py) В админке появились дополнительные поля. Что бы их показывать на Русском:
В models.py добавляем verbose_name:

class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')


------------------------------------------------------------------------------------------------------------------------------------


Категории
Пример:
class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title'] # Сортировка по title

Для связывания моделей пишем во вторичной модели (первоначальном классе) как обычное поле:
class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано?')
    category = models.ForeignKey('Category', on_delete= models.PROTECT, null=True)

В зависимости от того, раньше или позже объявлена первичная модель от вторичной, используется два варианта связи моделей:
    1) category = models.ForeignKey('Category')# если первичная позже вторичной
    2) category = models.ForeignKey(Category) # если первичная раньше вторичной

on_delete = Что делать при удалении категории, варианты читай в документации.
Null=True  = По умолчанию False. Из за того что добавляем строчку после создания базы, ставим Null что бы не пришлось его проставлять вручную, что бы не было проблем при обновлении базы.
ForeignKey = Один из «Полей отношений». Это Отношения многие-к-одному. Ещё есть:
ManyToManyField = Отношения многие ко многим. Разница с ForeignKey в том что одной категории может принадлежать много статей, или одна статья может принадлежать многим категорий.
OneToOneField = Отношения один-к-одному. Концептуально это похоже на ForeignKey  но «обратная» сторона отношения будет напрямую возвращать один объект.
После создания связи и успешной миграции, не забываем зарегистрировать её в админке.
В admins.py:
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

admin.site.register(Category)

В админке появились категории :)

------------------------------------------------------------------------------------------------------------------------------------

Построение ссылок на отдельные экземпляры моделей
Создаём в админке кнопку “Посмотреть на сайте”
Например если мы хотим получать ссылки на категории не по id а конкретному экземпляру модели:
Так же данный метод  def get_absolute_url(self):   Создаёт в админке кнопку “Посмотреть на сайте”
В models.py мы в классе создаём функцию:
from django.urls import reverse  # Или reverse_lazy



def get_absolute_url(self):   # get_absolute_url название по конвенции Django

    return reverse('category', kwargs={'category_id': self.pk})


Где - 'category' это название нашего маршрута из urls.py  …
path('category/<int:category_id>/', get_category, name='category'),

Где - kwargs={'category_id': self.pk}) Вместо kwargs можно использовать args.


Где 'category_id': Это параметр из…

path('category/<int:category_id>/', get_category, name='category'),

В шаблоне мы заменяем
href="{% url 'category' item.pk %}

На
href="{ item.get_absolute_url }"