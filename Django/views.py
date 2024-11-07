from django.http import HttpResponse


def main(request):
    res = '''<h1>Главная</h1><br>
    <a href=/news>Новости города</a><br>
    <a href=/management>Руководство города</a><br>
    <a href=/history>Факты о городе</a><br>
    <a href=/contacts>Контактные телефоны городских служб</a><br>'''
    return HttpResponse(res)


def news(request):
    return HttpResponse(f'<h2>Новости города</h2>')


def news_(request, wrong):
    return news(request)


def management(request):
    return HttpResponse(f'<h2>Руководство города</h2>')


def management_(request, wrong):
    return management(request)


def history(request):
    return HttpResponse(f'<h2>Факты о городе</h2>')


def people(request):
    return HttpResponse(f'<h3>Информация об известных жителях города</h3>')


def photos(request):
    return HttpResponse(f'<h3>Исторические фотографии города</h3>')


def contacts(request):
    return HttpResponse(f'<h2>Контактные телефоны городских служб</h2>')


def contacts_(request, wrong):
    return contacts(request)


def wrong(request):
    return HttpResponse('Неверный адрес')
