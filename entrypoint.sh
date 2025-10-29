#!/bin/sh
set -e

# Ожидаем, пока PostgreSQL будет готов к подключению
echo "⏳ Waiting for PostgreSQL to be ready..."
until nc -z db 5432; do
  sleep 1
done
echo "✅ PostgreSQL is ready!"

# Выполняем миграции Django
echo "📦 Running migrations..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

# Собираем статические файлы
echo "📁 Collecting static files..."
python manage.py collectstatic --noinput --clear

# Запускаем бота (в фоне)
echo "🤖 Starting bot..."
python accounts/bot.py &

# Запускаем Gunicorn
echo "🚀 Starting Gunicorn..."
gunicorn core.wsgi:application --bind 0.0.0.0:8000 --timeout 600
