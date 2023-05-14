from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
# Create your views here.

dict_day = {
    "monday": "Дела понедельника",
    "tuesday": "Дела вторника",
    "wednesday": "Дела среды",
    "thursday": "Дела четверга",
    "friday": "Дела пятницы",
    "saturday": "Дела субботы",
    "sunday": "Дела воскресенья"
}


def get_day_info(request, day: str):
    li = dict_day.get(day)
    if li:
        return HttpResponse(li)
    else:
        return HttpResponseNotFound("Неизвестный день недели")


def get_day_info_int(request, day: int):
    li = list(dict_day)
    if 0 < day < 8:
        red_url = reverse('week_day',args=[li[day-1]])
        return HttpResponseRedirect(red_url)
    return HttpResponseNotFound(f'Неверный номер дня {day}')


# def get_day_info_num(request, day: int):
#     if 0 < day < 8:
#         return HttpResponse(f'Today is {day} day on the week')
#     return HttpResponseNotFound(f'Incorrect day number {day}')
