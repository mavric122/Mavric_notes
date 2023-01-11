Admin.py
------------------------------------------------------------------------------------------------------------------------------------
Команда для создания суперюзера:
python manage.py createsuperuser
------------------------------------------------------------------------------------------------------------------------------------
Добавление модели в админку
В admin.py  импортируем нашу модель
from .models import News # где News название нашей модели
и
admin.site.register(News) # В админке появится меню для управления моделью

Изменение названий в админке.
В models.py создаём внутри нашего класса:
class Meta:
    verbose_name = 'Новость'
    verbose_name_plural = 'Новости'
    ordering = ['-created_at']



verbose_name = наименование модели в единственном числе. После этого в админке наименование “News” будет  “Новость”
verbose_name_plural = Наименование модели в множественном числе. 
ordering = Порядок сортировки. 
------------------------------------------------------------------------------------------------------------------------------------
Колонки в админке с дополнительными данными.

В admin.py:

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_published')


admin.site.register(News, NewsAdmin)

В админке появились дополнительные поля. Что бы их показывать на Русском:
В models.py добавляем verbose_name:

class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

Добавление ссылок в поля на соответсвующие модели:

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title', )

Не забудь запятую в конце!

Поля по которым можно производить поиск:

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title', )
    search_fields = ('title', 'content')

После в админке появится поле для поиска.  В переменную передаются в каких полях искать.


Поля для редактирования из списка:
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','category', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title',)
    search_fields = ('title', 'content')
    list_editable = ('is_published',)

Не забудь запятую в конце!

Создание фильтров.
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','category', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title',)
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')

list_filter = создание фильтрации, в неё передаётся какие поля фильтровать.
