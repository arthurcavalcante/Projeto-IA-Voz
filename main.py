'''

python3 -m pip install pydub SpeechRecognition
Baixar ffmpeg e colocar no PATH do windows

'''

from pydub import AudioSegment
import speech_recognition as sr
from utils.gravarAudio import getAudioMP3Path
import os

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
         printText()
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

def printText():
    try:
        with open('transcricao.txt', 'r') as file:
            text = file.read()
            print("\nConteúdo da transcrição:\n")
            print(text)
    except FileNotFoundError:
        print("Arquivo transcricao.txt não encontrado. Certifique-se de que o arquivo foi gerado corretamente.")

def remove_files():
    arquivos = ['transcricao.txt', 'audioToText.wav']
    for arquivo in arquivos:
        if os.path.exists(arquivo):
            os.remove(arquivo)
            print(f"{arquivo} removido.")
        else:
            print(f"{arquivo} não encontrado.")

if __name__ == '__main__':
    try:
        menu()
    finally:
        remove_files()