#encoding: utf-8

#Importando libs
import hashlib
import subprocess
from datetime import datetime
from platform import system
import os

#Criando tratamento de data 
dia = datetime.now().day
mes = datetime.now().month
ano = datetime.now().year

data =  str(dia)+ '/' + str(mes)+ '/' + str(ano)

#Fim do tratamento de data 

#Criando tratamento de hora 
hora = datetime.now().hour
minutos = datetime.now().minute
segundos = datetime.now().second

hora = 'Hora:'+ str(hora)+ ':' + str(minutos)+ ':' + str(segundos)

#Fim do tratamento de hora

#Criando função que limpa o display 
def limpa_display():
    sistema = system()
    if(sistema == 'Linux'):
        os.system("clear")
    elif(sistema != 'Linux'):
        os.system("cls")
#Fim da função que limpa o display
#Chamando função limpa_display()
limpa_display()
#Créditos (Não remover os créditos)
print("#########################################################")
print("Pyxcrypter v1.0")
print("Desenvolvido por:Jhonas Henrique")
print("#########################################################")
#Fim dos crédtios (Não remover os créditos)
#Criando menu de escolha
print("Escolha uma das opções a seguir:"+'\n')
print("1)MD5")
print("2)SHA1")
print("3)SHA256")
print("4)SHA512"+'\n')
#Pegando opção que o usuário informou
opcao = input("Digite o número da opção:")
#Chamando função limpa_display()
limpa_display()
#Entrada de dados
texto = input("Digite seu texto ou número a ser cifrado:")
#Chamando função que limpa display
limpa_display()
#estrutura de controle 
if(opcao == '1'):
   md5 = hashlib.md5(texto.encode('utf-8')).hexdigest()
   print('\n')
   print("##########################################################################")
   print('Sua cifra:'+md5)
   print("##########################################################################")
   print('Gerada em:'+data+' '+hora)
   print("##########################################################################")
   print('\n')
   #Exibindo notificação para o usuário
   subprocess.call(['notify-send', 'Notificação', 'Sua hash md5 foi gerada com êxito!'])
elif(opcao == '2'):
   print('\n')
   sha1 = hashlib.sha1(texto.encode('utf-8')).hexdigest()
   print("##########################################################################")
   print('Sua cifra:'+sha1)
   print("##########################################################################")
   print('Gerada em:'+data+' '+hora)
   print("##########################################################################")
   print('\n')
   #Exibindo notificação ao usuário
   subprocess.call(['notify-send', 'Notificação', 'Sua hash sha1 foi gerada com êxito!'])
elif(opcao == '3'):
   print('\n')
   sha256 = hashlib.sha256(texto.encode('utf-8')).hexdigest()
   print("##########################################################################")
   print('Sua cifra:'+sha256)
   print("##########################################################################")
   print('Gerada em:'+data+' '+hora)
   print("##########################################################################")
   print('\n')
   #Exibindo Notificação ao usuário
   subprocess.call(['notify-send', 'Notificação', 'Sua hash sha256 foi gerada com êxito!'])
elif(opcao == '4'):
   print('\n')
   sha512 = hashlib.sha512(texto.encode('utf-8')).hexdigest()
   print("##########################################################################")
   print('Sua cifra:'+sha512)
   print("##########################################################################")
   print('Gerada em:'+data+' '+hora)
   print("##########################################################################")
   print('\n')
   #Exibindo notificação ao usário
   subprocess.call(['notify-send', 'Notificação', 'Sua hash sha512 foi gerada com êxito!'])
else:
   print("Escolha uma opção válida!")
