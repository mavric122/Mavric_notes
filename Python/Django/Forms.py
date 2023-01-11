Создаём новый .py файл для создания формы

from django import forms
from .models import Category  # Для выбора категорий из списка


from django import forms
from .models import Category  

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=150, label='Тема')
    content = forms.CharField(label='Текст')
    is_published = forms.BooleanField(label='Опубликовано?')
    category = forms.ModelChoiceField(label='Категория',
                                      queryset=Category.objects.all())

label = Как это будет выводится на сайте.
empty_label = “Выберите категорию” = Вместо пропуска будет значение
required=False Делает поле не обязательным к заполнению.
Initial=True Будет ли поле по умолчанию заполнено.

Во view.py прописываем

def add_article(request):
    if request.method == 'POST':
        pass
    else:
        form = ArticleForm()
    return render(request, 'mysite/add_article.html', {'form': form})

Автоматический рендеринг формы

<form action="{% url 'add_article' %}" method="post">
    
    {% csrf_token %}
    {{ form.as_p  }}
    <button type="submit" class="btn btn-primary btn-block" >Добавить новость</button>
</form>

{% csrf_token %} – Это токен для защиты формы от подделки.

Есть три варианта автоматического рендеринга формы
    1 as.p – Каждое поле будет заключено в параграф.
    2 as.ul – Каждое поле будет элементом списка
    3 as.table - Каждое поле будет элементом таблицы

-----------------------------------------------------------------------------------------------------------------------------------

В forms.py переопределяем css нужной формы:
class EntranceForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['address'].widget.attrs.update({
            'required': '',
            'name': 'address',
            'id': 'address',
            'maxlength': '200',
            'minlength': '5',
            'class': 'form-input',
            'placeholder': '1234',
            'type': 'text',
            'font - size': '80px',
            })

    class Meta:
        fields = ['address']
