'''
<  pip install sounddevice numpy soundfile  >
'''

import sounddevice as sd
import numpy as np
import soundfile as sf
import tempfile

def gravar_audio(duracao=10, taxa_amostragem=44100, canais=1):
    print("Gravando...")
    audio_data = []
    
    def callback(indata, frames, time, status):
        if status:
            print(status)
        audio_data.append(indata.copy())
    
    with sd.InputStream(samplerate=taxa_amostragem, channels=canais, callback=callback):
        input("Pressione ENTER para parar a gravação.")
    
    audio_array = np.concatenate(audio_data, axis=0)
    return audio_array, taxa_amostragem

def salvar_audio_em_arquivo(audio_array, taxa_amostragem):

    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_audio_file:
        sf.write(temp_audio_file.name, audio_array, taxa_amostragem)
        temp_audio_file_path = temp_audio_file.name
    
    print(f"Áudio salvo em: {temp_audio_file_path}")
    return temp_audio_file_path

'''

def reproduzir_audio(file_path):
    data, fs = sf.read(file_path)
    print("Reproduzindo áudio...")
    sd.play(data, fs)
    sd.wait()
    
'''

def getAudioMP3Path():
    audio, tx_amostragem = gravar_audio()
    audio_path = salvar_audio_em_arquivo(audio, tx_amostragem)
    return audio_path