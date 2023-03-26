FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1 

WORKDIR /newsbot
COPY . .

RUN pip install -r requirements/production.txt

CMD ["python", "bot.py"]