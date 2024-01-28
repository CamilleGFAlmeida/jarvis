import speech_recognition as sr
import pyttsx3
import wikipedia

import pywhatkit 
import openai

audio = sr.Recognize
maquina = pyttsx3.init()

def listen_command():
try: 
    with sr.Microphone() as source:
        print("Escutando...")
        voz = audio.listen(source)
        comando = audio.recognize_google(voz, language='pt-BR')
        comando = comando.lower()
        if 'jarvis' in comando:
            comando = comando.replace('jarvis', '')
            maquina.say(comando)
            maquina.runAndWait()

except Exception as e:
    print(f'Microfone não está ok {e}')
    # print (f'o comando é: {comando}')
    return comando 

def execute_command(): 
    comando = listen_command()
    if 'procure por' in comando:
    procurar = comando.replace('procure por', '')
    wikipedia.set_lang("pt")
    resultado = wikipedia.summary(procurar, 2)
    print(resultado)
    maquina.say(resultado)
    maquina.runAndWait()
    elif 'toque' in comando:
        musica = comando.replace('toque', '')
        resultado = pywhatkit.playonyt(musica)
        maquina.say(f'Tocando {musica} no youtube')
        maquina.runAndWait()

while True:
execute_command()
saida = input("Deseja sair? (s/n) ")
if saida == 's':
    break  


