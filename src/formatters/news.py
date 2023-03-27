from src.models.news import News


def news_format(news: News) -> str:
    """
    Formats news object into a string to be sent as a message in a Telegram bot.

    Args:
        news: An instance of the News class representing a news article.

    Returns:
        A formatted string containing the news article's title,
        description (if available), and URL.
    """
    return "<b>{title}</b>\n\n{desc}\n\nRead more: {url}".format(
        title=news.title,
        desc=news.description if news.description else "",
        url=news.url,
    )
