from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

zodiac_dict = {
    'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'leo': 'Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
    'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
    'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',
}

sign_types = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces']
}


year = {'capricorn': [1223, 120],
        'aquarius': [121, 219],
        'pisces': [220, 320],
        "aries": [321, 420],
        'taurus': [421, 521],
        'gemini': [522, 621],
        'cancer': [622, 722],
        'leo': [723, 821],
        'virgo': [822, 932],
        'libra': [924, 1023],
        'scorpio': [1024, 1122],
        'sagittarius': [1123, 1222],
        }


def index(request):
    zodiacs = list(zodiac_dict)
    context = {
        'zodiacs': zodiacs,
    }
    return render(request,'index.html', context=context)


def type_index(request):
    li_elem = ''
    for zod in sign_types:
        li_elem += f'<li> <a href = "{zod}/"> {zod.title()} </a> </li>'

    return HttpResponse(f'<ol> {li_elem} </ol>')


def get_signs_by_element(request,type_name):
    li_elements = ''
    for zod in sign_types[type_name]:
        redirect_path = reverse('horoscope-name', args=[zod])
        li_elements += f'<li> <a href="{redirect_path}"> {zod.title()} </a> </li>'
    return HttpResponse(f'<ol> {li_elements} </ol>')


def get_horoscope_by_sign(request, sign_of_zodiac):
    # if sign_of_zodiac.lower() in zodiac_dict:
    #     return HttpResponse(zodiac_dict[sign_of_zodiac.lower()])
    data = {
        "desc_zodiac":zodiac_dict.get(sign_of_zodiac),
        "sign": sign_of_zodiac
    }
    return render(request,"info_zodiac.html",context=data)


def get_info_about_sign_zodiac_by_number(request, sign_zodiac: int):
    zodiacs = list(zodiac_dict)
    if sign_zodiac > len(zodiacs):
        return HttpResponseNotFound(f"Неправильный порядковый номер знака зодиака - {sign_zodiac}")
    name_zodiac = zodiacs[sign_zodiac - 1]
    redirect_url = reverse('horoscope-name', args=[name_zodiac])
    return HttpResponseRedirect(redirect_url)


def calculate_zodiak(request,month:str,day:str):
    if len(day) < 2:
        day = '0' + day
    date = int(month + day)
    if 1232 > date > 100:
        for sign_monthday in year:
            checklist = year.get(sign_monthday)
            if checklist[0] <= date <= checklist[1]:
                redirected_url = reverse('horoscope-name', args=[sign_monthday])
                return HttpResponseRedirect(redirected_url)
        else:
            return HttpResponseRedirect(reverse('horoscope-name', args=['capricorn']))
    return HttpResponse('знак не найден')
