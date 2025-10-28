from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect

# первоначальное представление hello_world
# def hello_world(request):
#     # получаем name и age, устанавливая пустую строку значением по умолчанию
#     name = request.GET.get('name', 'User')
#     age = request.GET.get('age', '0')
#     return HttpResponse(f'<h1>Hello, {name}! You are {age} years old.</h1>')

# hello_world с куками
def hello_world(request):
    name = request.GET.get('name', 'User')
    age = request.GET.get('age', '0')
    # создаём ответ
    response = HttpResponse(f'<h1>Hello, {name}! You are {age} years old.</h1>')
    # устанавливаем куку с именем пользователя
    response.set_cookie('username', name)
    # возвращаем ответ
    return response

def show_cookies(request):
    # получаем словарь всех куки
    cookies = request.COOKIES
    return JsonResponse(cookies)

def redirect_example(request):
    # перенаправляем на hello_world со встроенными параметрами по умолчанию
    # под капотом redirect вернёт HttpResponseRedirect со статус-кодом 302
    # либо в HttpResponse можно напрямую указать status=302
    # return redirect('/hello/?name=Vitya&age=20')
    # либо используем параметры по умолчанию из самого hello_world
    return redirect('/hello')

# представление возвращает обычный ответ в виде json
def json_example(request):
    user_data = {
        "name": "Ivan",
        "age": 30
    }
    return JsonResponse(user_data)