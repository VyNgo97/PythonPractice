from os import path
from pydub import AudioSegment
import logging
import json

logger = logging.getLogger(__name__)
audio_path = "/songs/"

def main():
    # milliseconds
    audio = AudioSegment.from_file("soundtracks.mp4")

    song_file = open("songTimes.json")
    song_list = json.load(song_file)
    
    for k, v in song_list.items():
        segment = audio[v.get("start_time") * 1000: v.get("end_time") * 1000]
        segment.export(f'songs/{v.get("title")}.mp3', format="mp3", bitrate="192k")

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logger.info('Starting segmenter script...')
    main()