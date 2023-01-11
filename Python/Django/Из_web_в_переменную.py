Пример:

В HTML:
<form action="add_result">
    Введите первое число: <input type="text" name="num1"><br>
    Введите второе число: <input type="text" name="num2"><br>
    <input type="submit">
</form>

В Django views создаём функцию которая сложит два числа и выведет результат:

def add_result(request):
    val1 = request.GET['num1']
    val2 = request.GET['num2']
    res = int(val1) + int(val2)
    return render(request, 'web_site/result.html', {'result': res})
