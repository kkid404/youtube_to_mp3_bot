import os
import logging

from pytube import YouTube
from pytube.helpers import safe_filename
from pytube.exceptions import VideoUnavailable, RegexMatchError

class Yt:
    @staticmethod
    def download(link: str):
        try:
            logging.info(f'Downloading {link} at quality...')
            yt_link = YouTube(link)
            stream = yt_link.streams.filter(progressive=True, file_extension='mp4').first()
            if stream:
                filename = f'{safe_filename(yt_link.title)}.mp4'
                path = os.path.abspath(filename)
                stream.download(output_path='.', filename=filename)  # Используйте текущую директорию для сохранения
                logging.info(f'Download completed: {path}')
                return path
            else:
                error_message = f'Error: Video with {quality} quality not available'
                logging.error(error_message)
                return error_message
        except (VideoUnavailable, RegexMatchError, Exception) as e:
            error_message = f'Error: {str(e)}'
            logging.error(error_message)
            return error_message