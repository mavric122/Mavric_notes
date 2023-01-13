Как обращятся к атрибутам объекта

obj = model.objects.get(id=id)
obj.counter # и через точку можешь обращаться к атрибутам объекта

Для Классов
# Мы берём объект и сохраняем вго в переменную. Всё сработает при перезагрузке страницы.
obj = Tovar.objects.get(pk=self.kwargs['tovar_id'])

if obj.amount <= 0:
    obj.there_is = False
    obj.save()
if obj.amount > 0:
    obj.there_is = True
    obj.save()

    
Тоже самое только для POST объекта:
    
    
class UpdateTovar(LoginRequiredMixin, UpdateView):
form_class = TovarForm
model = Tovar
template_name = 'tovar/edit_tovar.html'

def post(self, request, **kwargs):
    # Возвращает копию объекта, используя copy.deepcopy() из стандартной библиотеки Python. 
    # Эта копия будет изменяемой, даже если оригинал таковым не являлся.
    request.POST = request.POST.copy()
    if request.POST['amount'] != '0':
        request.POST['there_is'] = "True"
    else:
        request.POST['there_is'] = "False"

    return super(UpdateView, self).post(request, **kwargs)





Методы объектов

python manage.py shell ---- Вход в ORM
from Name.models import Name, Category ---- Импорт моделей для работы
Name.objects.all() ==== Вывод всех экземпляров объектов класса. Сортировка изначально по полю ordering в классе Meta в Models.py
Name.objects.get(pk=1) ==== Получаение одной записи. Метод get ожидает получить только одну запись. Не подходит для нескольких.

Работа с атрибутами объекта


name1 = _    →  Присвоить переменной name1 Последний результат выборки
cat2 = Category.objects.get(pk=2) →  Присвоить переменной cat2 <Category: Наука>
name1.is_publushed      → True/False
name1.title    → «Новость 1» 
Обращение к атрибуту объекта. 
Обращение идёт не по записи в полях БД. А как указанно в модели.

name1.category → «Наука»  ==== Обращение к атрибуту связанных данных объекта ==== Вернёт название если определён метод в модели.
 def __str__(self):
return self.title
Что в return указано — то и будет возвращено.

name1.category.pk   → 4
name1.category.pk   → «Наука»  ==== Обращение к атрибуту связанных данных объекта

 <name_model>_set

cat2 = Category.objects.get(pk=2) 
cat = cat2.news_set.all()
Обратная связь







Cортировка


Name.objects.order_by(«pk») ==== Сортировка по полю (« x »)

Name.objects.order_by(«pk»).reverse() ==== Сортировка по полю (« x ») в обратном порядке







Фильтры
Двойная нижняя черта


Tovar.objects.filter(id__gt=4) ==== Greted_then - gt - Получить больше > чем id-4 
Tovar.objects.filter(id__gte=4) ==== Greted_then - gt - Получить >= чем id-4
Tovar.objects.filter(id__lt=4)
Tovar.objects.filter(id__lte=4) ==== Тоже самое только < <=
T.objects.filter(title__contains=“Шкаф“) ==== Поиск по полю x__contains
contains → регистрозависимый
icontains → нерегистрозависимый

Tovar.objects.first() → Первая
Tovar.objects.last() → последняя
Tovar.objects.order_by(«-pk»).first() ==== Получить первую/последнюю новость по сортировке

Name1 = Name.objects.get(pk=4)
Name1.get_previous_by_created_at() → предыдущая
Name1.get_next_by_created_at() → Следующая
олучить на 1 раньше или позже запись по полю.

cat1 = Category.objects.get(pk=4)
cat1.news.__set.count()→ 3
Получить количество записей
Работает не только у связанных моделей.



























