import speech_recognition as sr
from principal import wav_path

# inicializa o recognizer
recognizer = sr.Recognizer()

# abre o arquivo de áudio
with sr.AudioFile(wav_path) as source:
    # Lê o arquivo de áudio
    audio = recognizer.record(source)

# converte o áudio em texto
try:
    texto = recognizer.recognize_google(audio, language='pt-BR')
    print('Texto extraído:', texto)
except sr.UnknownValueError:
    print('Não foi possível reconhecer o áudio.')
except sr.RequestError as e:
    print('Erro ao solicitar os resultados do serviço Google Speech Recognition; {0}'.format(e))

# biblioteca 1: pip install SpeechRecognition
# biblioteca 2: pip install
# biblioteca 3: pip install requests


