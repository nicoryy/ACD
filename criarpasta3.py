'''
    Versão 3.0
'''


from getpass import getuser
import os
import datetime
from shutil import move
import wmi

c = wmi.WMI()
    
#Pegar a data do dia atual
dia = datetime.datetime.now().day
if dia < 10:
    dia = f'0{dia}'
mes = datetime.datetime.now().month
if mes < 10:
    mes = f'0{mes}'


# Achar a letra do diretorio do pendrive 'PETE'
for disk in c.Win32_LogicalDisk() :
    if disk.VolumeName == 'PETE':
        local = disk.name
    else:
        raise Exception("Diretorio nao encontrado!!")
# print(local)

# Nome da pasta
nome = f'{dia}{mes}{datetime.datetime.now().year}'


# Pegar o nome de usuario do computador
usuario = getuser()


# Diretorio = Area de trabalho
dir = fR'C:\Users\{usuario}\Desktop\{nome}'

'''
    Verificar:
        Caso não tenha uma pasta nomeada com o dia atual : Criar uma na area de trabalho.

        Caso tenha: Copiar a pasta para o pendrive e apagar a da area de trabalho.
'''

destino = fR'{local}\infinity'

if os.path.isdir(dir):
    if os.path.isdir(fR'{destino}\{nome}'):
        os.rename(fR'{destino}\{nome}', fR'{destino}\{nome}teste')
    try:
        move(src=dir, dst=destino)
        print('Uma pasta foi encontrada, movida e excluída com sucesso!')
    except Exception as erro:
        print(erro)
        os.system('pause')
else:
    os.mkdir(dir)
    print('Pasta feita.')   




