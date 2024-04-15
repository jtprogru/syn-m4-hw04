from django.http import HttpResponse


def page1(request):
    return HttpResponse("<h1>Добро пожаловать на страницу 1!</h1>")


def page2(request):
    return HttpResponse("<h1>Добро пожаловать на страницу 2!</h1>")


def index(request):
    content = """
    <h1>Добро пожаловать на главную страницу!</h1>
    </br>
    <a href="pages/page1/">Перейти на страницу 1</a>
    </br>
    <a href="pages/page2/">Перейти на страницу 2</a>
    """
    return HttpResponse(content)
