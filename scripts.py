from datacenter.models import Mark
from datacenter.models import Chastisement
from datacenter.models import Commendation
from datacenter.models import Schoolkid
from datacenter.models import Lesson
import random


COMMENDATIONS = [
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


def create_commendation(name, subject):
    try:
        schoolkid = Schoolkid.objects.get(
            full_name__contains=name
        )
    except Schoolkid.DoesNotExist:
        print('Такого ученика или урока не существует!')
    except Schoolkid.MultipleObjectsReturned:
        print('Существует несколько учеников с таким именем!')
    else:
        lesson = Lesson.objects.filter(
            year_of_study=schoolkid.year_of_study,
            group_letter=schoolkid.group_letter,
            subject__title=subject
        ).order_by('-date').first()
        Commendation.objects.create(
            schoolkid=schoolkid,
            subject=lesson.subject,
            teacher=lesson.teacher,
            text=random.choice(COMMENDATIONS),
            created=lesson.date
        )


def remove_chastisements(schoolkid):
    chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    chastisements.delete()


def fix_marks(schoolkid):
    bad_marks = Mark.objects.filter(
        schoolkid=schoolkid,
        points__lt=4
    ).update(points=5)
