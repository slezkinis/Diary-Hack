from datacenter.models import Mark
from datacenter.models import Chastisement
from django.core.exceptions import MultipleObjectsReturned
from django.core.exceptions import ObjectDoesNotExist
from random import choice
from datacenter.models import Commendation
from datacenter.models import Schoolkid
from datacenter.models import Lesson
import random


def create_commendation(name, subject, commendations):
    try:
        schoolkid = Schoolkid.objects.get(
            full_name__contains=name
        )
        lesson = Lesson.objects.filter(
            year_of_study=schoolkid.year_of_study,
            group_letter=schoolkid.group_letter,
            subject__title=subject
        ).order_by('-date').first()
        Commendation.objects.create(
            schoolkid=schoolkid,
            subject=lesson.subject,
            teacher=lesson.teacher,
            text=random.choice(commendations),
            created=lesson.date
        )
    except ObjectDoesNotExist:
        print('Такого ученика или урока не существует!')
        return
    except MultipleObjectsReturned:
        print('Существует несколько учеников с таким именем!')
        return


def remove_chastisements(schoolkid):
    chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    chastisements.delete()


def fix_marks(schoolkid):
    bad_marks = Mark.objects.filter(
        schoolkid=schoolkid,
        points__lt=4
    )
    for mark in bad_marks:
        mark.points = 5
        mark.save()


def main():
    commendations = [
        'Молодец!',
        'Отлично!',
        'Хорошо!',
        'Гораздо лучше, чем я ожидал!',
        'Ты меня приятно удивил!',
        'Великолепно!',
        'Прекрасно!',
        'Ты меня очень обрадовал!',
        'Именно этого я давно ждал от тебя!',
        'Сказано здорово – просто и ясно!',
        'Ты, как всегда, точен!',
        'Очень хороший ответ!',
        'Талантливо!',
        'Ты сегдня прыгнул выше головы!',
        'Я поражен!',
        'Уже существенно лучше!',
        'Потрясающе!',
        'Замечательно!',
        'Прекрасное начало!',
        'Так держать!',
        'Ты на верном пути!',
        'Здорово!',
        'Это как раз то, что нужно!',
        'Я тобой горжусь!',
        'С каждым разом у тебя получается всё лучше!',
        'Мы с тобой не зря поработали!',
        'Я вижу, как ты стараешься!',
        'Ты растешь над собой!',
        'Ты многое сделал, я это вижу!',
        'Теперь у тебя точно все получится!'
    ]
