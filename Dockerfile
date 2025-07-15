# Базовый образ
FROM python:3.9-slim

# Рабочая директория
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .
RUN pip install -r requirements.txt

# Копируем код
COPY . .

# Открываем порт
EXPOSE 5000

# Команда запуска
CMD ["python", "app.py"]