FROM python:3.10-slim

ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1
    
WORKDIR /app

COPY requirements/ requirements/

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements/production.txt \
    && rm -rf requirements

COPY . .

CMD ["python", "./bot.py"]
