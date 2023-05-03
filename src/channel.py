
from googleapiclient.discovery import build
class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.youtube = build('youtube', 'v3', developerKey='api_key')

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        response = self.youtube.channels().list(
            part='snippet,statistics',
            id=self.channel_id
        ).execute()

        channel = response['items'][0]
        snippet = channel['snippet']
        statistics = channel['statistics']

        print(f"Title: {snippet['title']}")
        print(f"Description: {snippet['description']}")
        print(f"Custom URL: {snippet['customUrl']}")
        print(f"Published At: {snippet['publishedAt']}")
        print(f"View Count: {statistics['viewCount']}")
        print(f"Subscriber Count: {statistics['subscriberCount']}")
        print(f"Video Count: {statistics['videoCount']}")
