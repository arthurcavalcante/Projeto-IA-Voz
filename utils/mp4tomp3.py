from moviepy.editor import *
from principal import video_path

# variável
converted_audio = 'example.mp3'

# carregar o vídeo em mp4
video = VideoFileClip(video_path)

# extrair o áudio do vídeo
video.audio.write_audiofile(converted_audio)

# biblioteca: pip install moviepy