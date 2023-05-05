FROM python:3.10-alpine
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir
COPY . .
RUN python manage.py collectstatic --noinput
RUN python manage.py migrate
RUN python manage.py populate_table
CMD ["gunicorn","spa_table_test.wsgi:application","--bind","0:8000"]
