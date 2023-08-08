# Используем официальный образ Python
FROM python:3.9-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости и код в контейнер
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Определяем переменную окружения для токена бота
ENV BOT_TOKEN=6593318840:AAHCLZQA9chZOonVjyW6oO_OaOwAt0Srz-U

# Запускаем бота при старте контейнера
CMD ["python", "app.py"]