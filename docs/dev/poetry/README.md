#
```
Удалить venv из проекта
```
# Устанавливаем poetry
```
pip install poetry
```
# (Опционально)Указываем директорию куда poetry будет записывать кэш. По умолчанию appdata.
```
poetry config cache-dir <path>
```
# (Опционально) Настроить хранение .venv/ в корне проекта. По умолчанию appdata.
```
poetry config virtualenvs.in-project true
```
# Установка библиотек
```
poetry install
```
# Активация виртуальной среды
```
poetry shell
```
# Запуск сервера
```
python wsgi.py
```

----------------------------------------

Установка зависимостей:

# Устанавливает ВСЕ неопциональные(обязательные) группы зависимостей.
```
poetry install
```

# Добавление и исключение группы (Вместе использовать нельзя).
```
poetry install --without <groupname>
poetry install --with <groupname>
```
When used together, --without takes precedence over --with. For example,
the following command will only install the dependencies
specified in the optional test group.

# Установка библиотеки в группу
```
poetry add <library> --group dev
```