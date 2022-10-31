# Diary-Hack

В этом репозитории лежат модули, которые помогают повысить успеваемостть в школе. Здесь можно: убрать замечания, исправить все плохие оценки, добавить реалистичную похвалу от учителя.

## Перед запуском

Прежде, чем использовать эти функции обязательно нужно импортировть нужные модели:
```python
from datacenter.models import Mark
from datacenter.models import Chastisement
from django.core.exceptions import MultipleObjectsReturned
from django.core.exceptions import ObjectDoesNotExist
from random import choice
from datacenter.models import Commendation
from datacenter.models import Schoolkid
from datacenter.models import Subject
from datacenter.models import Lesson
```

## Описание каждого модуля

1. Функция `create_commendation(name, subject)` создаёт похвалу от учителя. В поле `name` нужно указать своё имя и фамилию, в поле `subject` - название предмета, по которому нужно добавить похвалу. Вот пример запуска:
    ```python
    create_commendation('Фролов Иван', 'Музыка')
    ```
2. Функция `remove_chastisements(schoolkid)` удаляет все замечания указанного ученика. В поле `schoolkid` нужно передать объект нужного ученика. Вот пример запуска:
    ```python
    remove_chastisements(ivan)
    ```
3. Функция `fix_marks(schoolkid)` исправляет все плохие оценки на 5. В поле `schoolkid` нужно передать объект нужного ученика. Вот пример запуска:
    ```python
    fix_marks(ivan)
    ```

## Подключение функций
Чтобы использовать эти функции в консоли можно их импортировать. Вот пример:
```python
from scripts import fix_marks
```
А затем их можно просто вызвать.
Также можно их скопировать в консоль и также вызвать

# Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).