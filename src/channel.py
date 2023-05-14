import json
from googleapiclient.discovery import build
class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        youtube = self.get_service()
        response = youtube.channels().list(
            part='snippet,statistics',
            id=self.channel_id
        ).execute()
        channel = response['items'][0]
        self.title = channel['snippet']['title']
        self.description = channel['snippet']['description']
        self.custom_url = channel['snippet']['customUrl']
        self.published_at = channel['snippet']['publishedAt']
        self.view_count = channel['statistics']['viewCount']
        self.subscriber_count = channel['statistics']['subscriberCount']
        self.video_count = channel['statistics']['videoCount']

    @classmethod
    def get_service(cls):
        """Возвращает объект для работы с YouTube API"""
        return build('youtube', 'v3', developerKey='api_key')

    def to_json(self, filename):
        """Сохраняет в файл значения атрибутов экземпляра Channel"""
        data = {
            'channel_id': self.channel_id,
            'title': self.title,
            'description': self.description,
            'custom_url': self.custom_url,
            'published_at': self.published_at,
            'view_count': self.view_count,
            'subscriber_count': self.subscriber_count,
            'video_count': self.video_count
        }
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        response = self.youtube.channels().list(
            part='snippet,statistics',
            id=self.channel_id
        ).execute()

        print(json.dumps(response, indent=4, ensure_ascii=False))
