# Тестовое задание для Backend-разработчика учебного проекта &laquo;Парковки Москвы&raquo; #

## Содержание ##

[1. Условия задания](#условия-задания)    
[2. Описание решения](#описание-решения)    
[3. Результат](#результат)    
[4. Инструкция по запуску проекта](#инструкция-по-запуску-проекта)    

## Условия задания ##

Нужно потрудиться над созданием поисковой системы базы данных парковочных мест
нашего приложения.

***Подсказка:***    
Надо взять базу адресов, индексировать ее **`Sphinx`**, и сделать поиск по ней.

***Ситуация:***    
Пользователь (автовладелец) выехал в центр Москвы на деловую встречу. Но,
приехав к месту встречи, обнаружил, что свободных парковочных мест от
Московского паркинга на улице нет. Пользователь вспоминает о нашем приложении,
заходит в него. В приложении подгружается поисковая система парковочных мест по
адресам нашей базы данных. Пользователь вводит в поисковик необходимый ему
адрес, например, `Ленинградский...` и после нажатия кнопки **`Найти`**
приложение обрабатывает запрос и выдает пользователю места из нашей базы, в
тексте которых присутствует слово `Ленинградский`.

База данных адресов [здесь](data/db_parking.xlsx).

Важно понимать, что база учебная. Пока в ней расположены адреса не подключённые
к приложению и не одобренные для него. :warning: Важно увидеть как выполняется
задача с любым набором адресов.

Желательно, но не обязательно, чтобы приложение автоматически предлагало
пользователю ввод адреса при вводе нескольких первых букв названия улицы,
площади, проспекта, etc.

[:arrow_up: Содержание](#содержание)

----

## Описание решения ##

*TEMPORAL TODO*    

Отладить настройку для ручного запуска Sphinx в виртуальном окружении.

На начальном этапе для работы Sphinx отработать преобразование файла Excel в JSON
(лучше в XML), чтобы Sphinx с ним заработал.

В связке python + pandas + psycopg2/sqlalchemy отработать SQL-запрос.
Предусмотреть, чтобы запрос к базе отправлялся после набора трёх букв поиска
адреса и далее новый запрос после каждой следующей буквы. С выдачей всех
найденных (оставшихся) вариантов.

Включить в схему PostgreSQL. Закачка из Excel в базу. Индексация.

Демо реализовать в Bottle?

[:arrow_up: Содержание](#содержание)

----

## Результат ##

[:arrow_up: Содержание](#содержание)

----

## Инструкция по запуску проекта ##

1. На компьютере должен быть установлен **Python** версии **3.8** или более
поздней и соответствующий пакетный менеджер **pip**.
2. Скачать файлы проекта из текущей директории репозитория в локальную
директорию компьютера.
3. Скачать [с сайта](http://sphinxsearch.com/downloads/current/) архив
бинарников **Sphinx** и распаковать в поддиректорию текущего проекта, например
`sphinx-3.4.1/`.
4. Создать пустые файлы `sphinx-3.4.1/log/query.log`,
`sphinx-3.4.1/log/searchd.log` и директорию `sphinx-3.4.1/index/`.
5. Переместить в `sphinx-3.4.1/etc/` файл `sphinx.conf`, изменить в нём
соответствующим образом пути в параметрах `xmlpipe_command`, `path`, `log`,
`query_log`, `pid_file`, `binlog_path`.
6. Примерная последовательность команд в консоли терминала для запуска проекта
в виртуальном окружении `virtualenv` в локальной директории:

    ```bash
    python -m venv VENV

    # для ОС Linux:
    source VENV/bin/activate
    # для ОС Windows:
    VENV\Scripts\activate

    pip install -r requirements.txt

    python api_demo.py
    # Выход по Ctrl+C

    # Выход из виртуального окружения
    # для ОС Linux:
    deactivate
    # для ОС Windows:
    VENV\Scripts\deactivate.bat
    ```

7. В консоли виртуального окружения для запуска **Sphinx** ввести команду (для
Windows):

    ```dos
    sphinx-3.4.1\bin\searchd.exe --config sphinx-3.4.1\etc\sphinx.conf
    ```

8. Команда для ручного обновления индексов:

    ```dos
    sphinx-3.4.1\bin\indexer.exe test1 --config sphinx-3.4.1/etc/sphinx.conf --rotate
    ```

[:arrow_up: Содержание](#содержание)

----
