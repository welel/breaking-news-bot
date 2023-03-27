# Breaking News Telegram Bot

![aiogram](https://img.shields.io/badge/python-v3.10-blue.svg?logo=python&logoColor=yellow) ![aiogram](https://img.shields.io/badge/aiogram-v3-blue.svg?logo=telegram)

The main feature of this bot is to deliver latest news headlines related to technology along with a URL to the source to keep users up to date with the latest news and developments in the tech industry. The bot is designed to have only one command, `/start`, which initiates the bot and sends a short description of its capabilities. Any message sent to the bot will receive a notification that the bot only sends news and does not receive messages.

![Screenshot](https://i.ibb.co/sPH56W2/Group-2.png)

### Requirements

- Linux 
- Python v3.10
- aiogram v3
- dotenv v1 - for the bot configuration
- [newsapi-python](https://github.com/mattlisiv/newsapi-python) - for using [NewsAPI](https://newsapi.org/)
- [aiosqlite](https://github.com/omnilib/aiosqlite) - for keeping users ids
- APScheduler v3.1 - for scheduling tasks

### Installation

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

- Get an API key on the [NewsAPI](https://newsapi.org/) website.

- Rename the file `.env.dist` to `.env` and replace the placeholders with required data.

- Run the bot using `python bot.py`.

