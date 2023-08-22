import os
import logging

from pytube import YouTube
from pytube.helpers import safe_filename
from pytube.exceptions import VideoUnavailable, RegexMatchError


class Yt:

    @staticmethod
    def download(link: str, quality='720p'):
        try:
            logging.info(f'Downloading {link} at {quality} quality...')
            yt_link = YouTube(link)
            stream = yt_link.streams.filter(progressive=True, res=quality).first()
            if stream:
                filename = f'{safe_filename(yt_link.title)}.mp4'
                path = os.path.abspath(filename)
                stream.download(output_path='.', filename=filename)  # Используйте текущую директорию для сохранения
                logging.info(f'Download completed: {path}')
                return path
            else:
                raise VideoUnavailable(f'Video with {quality} quality not available')
        except (VideoUnavailable, RegexMatchError, Exception) as e:
            logging.error(f'Error: {str(e)}')
            return f'Error: {str(e)}'
