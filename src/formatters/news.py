from src.models.news import News


def news_format(news: News) -> str:
    return "<b>{title}</b>\n\n{desc}\n\nRead more: {url}".format(
        title=news.title,
        desc=news.description if news.description else "",
        url=news.url,
    )
