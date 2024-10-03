'''

python3 -m pip install pydub SpeechRecognition
Baixar ffmpeg e colocar no PATH do windows

'''

from pydub import AudioSegment
import speech_recognition as sr
from utils.gravarAudio import getAudioMP3Path

audio_path = getAudioMP3Path()

def menu():

   while True:

      print(
         '''
         1. Audio para texto
         2. Sair
         '''
      )

      escolha = int(input("Escolha uma opcao: "))
      
      if escolha == 1:
         traducao()
      elif escolha == 2:
         print("Closing...")
         break
      else:
         print("Opcao invalida")

def mp3_to_wav(input_audio_path, output_wav_path):
   sound = AudioSegment.from_mp3(input_audio_path)
   sound.export(output_wav_path, format="wav")


def audio_to_text(audio_wav_path, output_text_file):
   r = sr.Recognizer()
   with sr.AudioFile(audio_wav_path) as source:
      audio_text = r.record(source)
      text = r.recognize_google(audio_text,language='pt-BR')
   with open(output_text_file, 'w') as arquivo:
        arquivo.write(text)

def traducao():
   wav_path = "./audioToText.wav"
   mp3_to_wav(audio_path, wav_path)

   output_text = 'transcricao.txt'
   audio_to_text(wav_path, output_text)
   print(f"Transcricao salva em {output_text}")

if __name__ == '__main__':
    menu()