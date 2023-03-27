FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1 

WORKDIR /newsbot
COPY . .

RUN pip install -r requirements/production.txt

VOLUME /newsbot/data

CMD ["python", "bot.py"]