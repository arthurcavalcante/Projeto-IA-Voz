import utils.corretor as corretor
import utils.mp3towav as mp3towav
import utils.mp4tomp3 as mp4tomp3
import utils.wavtotext as wavtotext

# Dicionário que mapeia opções para funções de execução dos módulos
opcoes = {
    '1': wavtotext.executar,
    '2': mp3towav.executar,
    '3': mp4tomp3.executar,
    '4': wavtotext.executar,
}

def mostrar_opcoes():

    print("""
      Escolha qual opção você deseja!
      1 - Para converter Audio .wav ou .mp3 para texto .txt
      2 - Para converter .mp3 para .wav
      3 - Para converter Vídeo .mp4 em audio .mp3 ou .wav   
      4 - Para corrir um texto em pt-br
      0 - Sair        
         """)


def main():
    while True:
        mostrar_opcoes()
        opcao = input("Digite a opção desejada: ")
        if opcao == '0':
            print("Saindo...")
            break
        try:
            # Executa a função correspondente à opção
            opcoes[opcao]()
        except KeyError:
            print("Opção inválida. Tente novamente.")


