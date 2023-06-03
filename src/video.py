from src.channel import Channel


class Video:
    video_id = None
    title = None
    url = None
    view_count = None
    like_count = None

    def __init__(self, video_id):
        self.video_id = video_id
        try:
            channel_data: dict = self.get_video_data()

            self.title: str = channel_data['items'][0]['snippet']['title']
            self.url: str = str("https://youtu.be/" + video_id)
            self.view_count: int = channel_data['items'][0]['statistics']['viewCount']
            self.like_count: int = channel_data['items'][0]['statistics']['likeCount']
        except:
            self.title = None
            self.url = None
            self.view_count = None
            self.like_count = None

    def __str__(self):
        """Возвращает строковое представление атрибута класса"""
        return f"{self.title}"

    def get_video_data(self):
        """Получает информацию о видео"""
        return Channel.get_service().videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                   id=self.video_id
                                                   ).execute()


class VideoNotFound(Exception):
    """
    Базовый класс исключения VideoNotFound
    """
    pass


class PLVideo(Video):
    video_id = None
    playlist_id = None

    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)

        self.playlist_id = playlist_id
