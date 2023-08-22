import os
import logging

from pydub import AudioSegment
from pydub.exceptions import CouldntDecodeError


class Converter:

    @staticmethod
    def mp4_to_mp3(file: str):
        try:
            name = file.split(".")[0]
            output_file = f"{name}.mp3"
            logging.info(f"Converting {file} to {output_file}...")
            audio = AudioSegment.from_file(file, format="mp4")
            audio.export(output_file, format="mp3")
            os.remove(file)
            logging.info(f"Conversion completed: {output_file}")
            return os.path.abspath(output_file)
        except CouldntDecodeError as e:
            logging.error(f"Error: {str(e)}")
            return f"Error: {str(e)}"