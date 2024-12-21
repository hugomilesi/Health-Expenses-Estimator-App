FROM python:3.12-bookworm

ENV PYTHONDONTWRITEBYTECODE = 1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

COPY health_expenses/predictions/models app/health_expenses/predictions/models

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

# 
# CMD ["python", "health_expenses/manage.py", "runserver", "0.0.0.0.8000"]

CMD ["waitress-serve", "--listen=*:8000", "health_expenses.wsgi:application"]

