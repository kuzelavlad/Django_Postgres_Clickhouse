# Используем базовый образ Python для Django
FROM python:3.9

# Устанавливаем переменную окружения PYTHONUNBUFFERED для вывода логов
ENV PYTHONUNBUFFERED=1

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файлы зависимостей в контейнер
COPY requirements.txt /app/

# Устанавливаем зависимости
RUN pip install -r requirements.txt

# Копируем все файлы проекта в контейнер
COPY . /app/

# Убеждаемся, что manage.py доступен из-под командной строки внутри контейнера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]