urlpatterns = [
    path('admin/', admin.site.urls),
    path('', title_menu),
    path('shop/', include('shop.urls')),
    path('test/', test),

]

Функция path может принимать параметры:
def _path(route, view, kwargs=None, name=None, Pattern=None):

route = маршрут (‘test/’,…
view = функция которую необходимо вызвать =   …test),
name = Имя маршрута, это имя можно использовать в шаблонах для построения ссылок
или список вложенных маршрутов = include('shop.urls')),

------------------------------------------------------------------------------------------------------------------------------------

Для загрузки фото в sqlite
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'

А в urls.py после urlpatterns = [] прописываем
if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

------------------------------------------------------------------------------------------------------------------------------------

Адреса по категориям(пока не знаю как ещё назвать)

urlpatterns = [
    path('', index),
    path('category/<int:category_id>/', get_category)
]

Где в треугольных скобках указывается какие страницы должны быть перехвачены, в данном случае это …category/<целое число>. Например … category/4

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
href="{% url 'category' item.pk %} На href="{ item.get_absolute_url }""

