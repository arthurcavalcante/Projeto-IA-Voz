from principal import audio_path
from os import path
from pydub import AudioSegment

# arquivos mp3 e wav                                                   
wave_audio = "test.wav"

# converter mp3 para wav                                             
sound = AudioSegment.from_mp3(audio_path)
sound.export(wave_audio, format="wav")

# windows: pip install pydub
# ubuntu: apt-get install ffmpeg

