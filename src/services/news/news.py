import pickle
import os

from newsapi import NewsApiClient

from src.models.news import News


class NewsClient:
    """A client for fetching news from News API.

    Usage:
        1. Set API key with `set_api_key` class method.
        2. Use client methods.

    API docs: https://newsapi.org/docs

    Example:
        >>> NewsClient.set_api_key("your_api_key")
        >>> latest_news = NewsClient.fetch_last_news()
        >>> new_news = NewsClient.get_new_news()

    """

    last_loaded_news_path: str = "last_loaded_news_object.pickle"

    @classmethod
    def set_api_key(cls, api_key: str) -> None:
        """Sets the API key to use the class.

        Args:
            api_key: A string representing the API key to use.

        """
        cls.api = NewsApiClient(api_key=api_key)

    @classmethod
    def fetch_last_news(cls) -> tuple[News]:
        """Fetches the latest news from News API.

        Returns:
            A tuple of News objects representing the latest news.

        Raises:
            NewsAPIException: If a request to the API is failed.
        """
        data = cls.api.get_top_headlines(
            country="us", category="technology", page_size=10
        )
        if data["totalResults"] > 0:
            return tuple([News(**article) for article in data["articles"]])
        return tuple()

    @staticmethod
    def _load_last_loaded_news(filename: str) -> News | None:
        """Loads the last loaded news object from a file.

        Args:
            filename: A filename to load the last loaded news object from.

        Returns:
            The last loaded news object if the file exists and is non-empty,
            None otherwise.
        """
        if os.path.isfile(filename) and os.path.getsize(filename) > 0:
            with open(filename, "rb") as last_loaded_news_file:
                return pickle.load(last_loaded_news_file)

    @staticmethod
    def _dump_last_loaded_news(filename: str, news: News) -> None:
        """Dumps the last loaded news object to a file.

        Args:
            filename: A filename to dump the last loaded news object to.
            news: A last loaded news object to dump.
        """
        with open(filename, "wb+") as last_loaded_news_file:
            pickle.dump(news, last_loaded_news_file)

    @classmethod
    def get_new_news_list(cls) -> tuple[News]:
        """Fetches new news since the last loaded news object.

        Returns:
            A tuple of News objects representing the new news since
            the last loaded news object.
        """
        news_list = cls.fetch_last_news()
        if not news_list:
            return tuple()

        last_loaded_news = cls._load_last_loaded_news(cls.last_loaded_news_path)
        cls._dump_last_loaded_news(cls.last_loaded_news_path, news_list[0])

        if last_loaded_news:
            for i, news in enumerate(news_list):
                if news == last_loaded_news:
                    return news_list[:i]
        return news_list

    @classmethod
    def get_last_news(cls) -> News | None:
        """Returns a last loaded news from the file or fetches a top news.

        Returns:
            The last loaded news object or None.
        """
        if news := cls._load_last_loaded_news(cls.last_loaded_news_path):
            return news
        elif news_list := cls.fetch_last_news():
            return news_list[0]
