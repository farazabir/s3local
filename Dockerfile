FROM python:3.11-alpine AS builder

WORKDIR /app
RUN apk update && apk add --no-cache gcc musl-dev libffi-dev

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
FROM python:3.11-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY .  .

EXPOSE 8080
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
