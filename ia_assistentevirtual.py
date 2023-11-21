#Importando as bibliotecas
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit
import os
import requests
import json
import pyowm
import locale

#---------------------------------------------- Assistente Virtual - IA -------------------------------------------#

audio = sr.Recognizer()
maquina = pyttsx3.init('sapi5')
locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

def executa_comando():
    try:
        with sr.Microphone() as source:
            print('Ouvindo...')
            audio.adjust_for_ambient_noise(source)
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()
            
            if 'Tipi' in comando:
                comando = comando.replace('Tipi','')
                maquina.say(comando)
                maquina.runAndWait()      
    except:
        print('Não estou entendendo...')
    return comando

def comando_voz_usuario():
    comando = executa_comando()
    if 'que horas' in comando:
        hora = datetime.datetime.now().strftime('%H')
        minutos = datetime.datetime.now().strftime('%M')
        maquina.say(f'Agora são {hora} horas e {minutos} minutos')
        maquina.runAndWait()
        
    elif 'hoje' in comando:
        dia = datetime.datetime.now().strftime('%d')
        mes = datetime.datetime.now().strftime('%B')
        maquina.say(f'Hoje é dia {dia} de {mes}')
        maquina.runAndWait()

    elif 'depois' in comando:
        dia = datetime.datetime.now().strftime('%d')
        dia = int(dia) + 1
        maquina.say(f'Amanhã será {dia}')
        maquina.runAndWait()

    elif 'pesquisa' in comando:
        procurar = comando.replace('pesquisa', '')
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar, 2)
        maquina.say(resultado)
        maquina.runAndWait()

    elif 'tocar' in comando:
        musica = comando.replace('tocar', '')
        resultado = pywhatkit.playonyt(musica)
        maquina.say('Tocando musica')
        maquina.runAndWait()

    elif 'assistir' in comando:
        musica = comando.replace('assistir', '')
        resultado = pywhatkit.playonyt(musica)
        maquina.say('Assistindo')
        maquina.runAndWait()

    elif 'navegador' in comando:
        os.system('start Chrome.exe')
        maquina.say('Abrindo navegador')
        maquina.runAndWait()

    elif 'fechar navegador' in comando:
        os.system('taskkill /f /im  Chrome.exe')
        maquina.say('Fechando navegador')
        maquina.runAndWait()

    elif 'google' in comando:
        os.startfile('https://www.google.com.br/')
        maquina.say('Abrindo google')
        maquina.runAndWait()

    elif 'excel' in comando:
        os.system('start Excel.exe')
        maquina.say('Abrindo Excel')
        maquina.runAndWait()

    elif 'whats' in comando:
        os.startfile('https://web.whatsapp.com/')
        maquina.say('Abrindo whatsapp web')
        maquina.runAndWait()

    elif 'univem' in comando:
        os.startfile('https://www.univem.edu.br/home')
        maquina.say('Abrindo site do univem')
        maquina.runAndWait()

    elif 'youtube' in comando:
        os.startfile('https://www.youtube.com/')
        maquina.say('Abrindo youtube')
        maquina.runAndWait()

    elif 'meu nome' in comando:
        nome = 'Daniel'
        maquina.say('Seu nome é'+ nome)
        maquina.runAndWait()

    elif 'seu nome' in comando:
        ia = 'Tipi'
        maquina.say('Meu nome é' + ia)
        maquina.runAndWait()

while True:
    try:
        comando_voz_usuario()
    except:
        pass

