import moviepy.editor as mp
import speech_recognition as sr
import moviepy.editor as mp

# Coleta de vídeos e audios. Mp3 e Mp4

video_path = 'nome_do_arquivo.mp4'  
audio_path = 'exemplo.mp4'

# Escolher qual você vai traduzir

while True:
   escolha = input('Escolha qual opção você deseja. 1 Para converter Audio para texto, 2 Para converter Vídeo em texto, 3 Para converter Vídeo em audio.')
   if escolha in [1,2,3]:
      break

# Escolhendo a tradução correta

def traducao():
   


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