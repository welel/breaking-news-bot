# Breaking News Telegram Bot

![aiogram](https://img.shields.io/badge/python-v3.10-blue.svg?logo=python&logoColor=yellow) ![aiogram](https://img.shields.io/badge/aiogram-v3-blue.svg?logo=telegram)

A Telegram bot that delivers breaking news headlines related to technology. This bot is designed to keep users up to date with the latest news and developments in the tech industry. With its ability to source breaking news from various publications, blogs, and news websites, the bot delivers reliable and relevant news to its users.

## Features

The bot provides the following features:

-
-

## Commands

The bot has several commands that can be used to access its features:

- `/start`: Sends a ...
- `/help`: Sends a ...

## Requirements

- Python v3.10
- aiogram v3
- dotenv v1 - for the bot configuration
- [newsapi-python](https://github.com/mattlisiv/newsapi-python) - for using [NewsAPI](https://newsapi.org/)

## Installation

To get started with this bot, follow these steps:

- Clone this repository to your local machine.

    ```
    $ git clone [source]
    ```

- Create a virtual environment, activate it and install required dependencies.

    ```
    $ python3.10 -m venv env
    $ source env/bin/activate
    $ pip install -r requirements/local.txt
    ```

- Create a new bot on Telegram by talking to the BotFather, and [obtain the API token](https://www.siteguarding.com/en/how-to-get-telegram-bot-api-token).

- Rename the file `.env.dist` to `.env` and replace the placeholders with required data.

- Run the bot using `python bot.py`.

