import moviepy.editor as mp
import speech_recognition as sr
import moviepy.editor as mp
import sys from pydub import AudioSegment

#a variável path contem o nome do arquivo do seu vídeo
path = “nome_do_arquivo.mp4” 

#converter de mp4 para mp3
clip = mp.VideoFileClip(path).subclip()
clip.audio.write_audiofile("./nome_para_audio.mp3")

src=(r"./nome_para_audio.mp3")
# converter de mp3 para wav
sound = AudioSegment.from_mp3(src)
sound.export("./nome_arquivo.wav", format="wav")
file_audio = sr.AudioFile(r"./nome_arquivo.wav")

# use the audio file as the audio source
r = sr.Recognizer()
with file_audio as source:
   audio_text = r.record(source)
   text = r.recognize_google(audio_text,language='pt-BR')

arq = open(‘transcricao.txt’,’w’)
arq.write(text)
arq.close()

print(text)   