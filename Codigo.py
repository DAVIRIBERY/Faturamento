import json
from datetime import datetime

Faturamento=[]

def convenio():
    return input('\nDigite o nome do convênio: ')
def tabela():
    return input('\nTabela de honorarios medicos acordada: ')
def med():
    return input('\nTabela de medicamentos acordada: ')
def mat():
    return input('\nTabela de materiais acordada: ')
def fisio_andares():
    return input('\nQuantidade de fisioterapia a cobrar por dia na clinica medica: ')
def fisio_uti():
    return input('\nQuantidade de fisioterapia a cobrar por dia na UTI neo / UTI adulto: ')
def fono():
    return input('\nQuantidade a cobrar de consulta de fonoaudiologia por dia: ')
def data():
    return datetime.now().strftime("%d/%m/%y %H:%M:%S")

def salvar_dados():

        with open('convenios.json','w',encoding='utf-8')as Arquivo:
            json.dump(Faturamento,Arquivo,ensure_ascii=False,indent=4)
def carregar_dados():
    
    global Faturamento
    try:
        with open('convenios.json','r',encoding='utf-8')as Arquivo:
            Faturamento=json.load(Arquivo)
    except FileNotFoundError:
        Faturamento=[]
        
carregar_dados()

while True:
    print("\n Faturamento \n")
    print("\n----MENU----")
    print("1-Para cadastrar convênio ")
    print("2-Para pesquisar por convênio ")
    print("3-Para alterar informações ja cadastradas ")
    print("4-Para conferir todos os convênios cadastrados ")
    print("5-Para sair")

    menu=input('\nDigite a opção desejada pelo numero da mesma: ')

    if menu=='1':
        while True:
            convenios={}
            convenios['Convenio']=convenio()
            convenios['Tabela']=tabela()
            convenios['Med']=med()
            convenios['Mat']=mat()
            convenios['Fisio_andares']=fisio_andares()
            convenios['Fisio_uti']=fisio_uti()
            convenios['Fonoaudiologia']=fono()
            convenios['Data']=data()
            Faturamento.append(convenios)
            salvar_dados()
            print('\n Convenio cadastrado com sucesso !!!\n')
            print('-'*30)
            escolha=input('Deseja continuar cadastrando ? S/N').strip().lower()
            if escolha=='n':
                break
    elif menu=='2':
        Pesquisa=input ('\nDigite o nome do convênio que deseja pesquisar: ').strip().lower()

        Resultado=False

        for convenios in Faturamento:
            if convenios['Convenio'].strip().lower()==Pesquisa:
                print(f'\nConvênio: {convenios['Convenio']}')
                print(f'\nTabela de honorarios medicos: {convenios['Tabela']}')
                print(f'\nTabela de medicamentos acordada: {convenios['Med']}')
                print(f'\nTabela de materias acordada: {convenios['Mat']}')
                print(f'\nQuantidade de fisioterapias por dia na clinica medica(andares):{convenios['Fisio_andares']} ')
                print(f'\nQuantidade de fisioterapias por dia na UTI adulto / Neo : {convenios['Fisio_uti']}')
                print(f'\nQuantidade de fonoaudiologia por dia:{convenios['Fonoaudiologia']} ')
                print(f'\nData do cadastro das informações: {convenios['Data']}')
                print('-'*30)
                Resultado=True
                break
        if not Resultado:
            print(f'\nConvênio {Pesquisa},não localizado !\n ')

    elif menu=='3':

       pesquisa=input('Digite o convênio que deseja alterar informações cadastradas: ').strip().lower()

       if pesquisa.isdigit():
           print('Você digitou um numero, valido apenas letras ')

       resultado=False

       for convenios in Faturamento:

           if convenios['Convenio'].strip().lower()==pesquisa:
               print(f'\nConvênio: {convenios['Convenio']}')
               print(f'\nTabela de honorarios medicos: {convenios['Tabela']}')
               print(f'\nTabela de medicamentos acordada: {convenios['Med']}')
               print(f'\nTabela de materias acordada: {convenios['Mat']}')
               print(f'\nQuantidade de fisioterapias por dia na clinica medica(andares):{convenios['Fisio_andares']} ')
               print(f'\nQuantidade de fisioterapias por dia na UTI adulto / Neo : {convenios['Fisio_uti']}')
               print(f'\nQuantidade de fonoaudiologia por dia {convenios['Fonoaudiologia']}')
               print(f'\nData do cadastro das informações: {convenios['Data']}')
               print('-'*30)
               resultado=True

               while True:
                print("\nQual informação deseja alterar ?"
                    "\n1-Para alterar tabela de honoraios medicos"
                    "\n2-Para alterar tabela de medicamentos "
                    "\n3-Para alterar tabela de materias "
                    "\n4-Para alterar quantidade  de fisioterapia por dia na clinica medica(andares) "
                    "\n5-Para alterar quantidade de fisioterapia por dia na UTI adulto / neo " 
                    "\n6-Para alterar quantidade de fonoaudiologia por dia" )
                
                acao=input('Qual a opção desejada: ')
                if acao =='1':
                    alterador=input('Digite a tabela de honarios medicos acordada: ')

                    if alterador.isdigit():
                        print('Você digitou um numero, valido apenas letras ! ')

                    convenios['Tabela']=alterador
                    convenios['Data']=data()
                    salvar_dados()
                    print('Alteração realizada com sucesso !!!')

                    desejo=input('Deseja continuar alterando ? s/n').strip().lower()

                    if desejo =='n':
                        break

                elif acao=='2':
                    alterador=input('Digite a tabela de medicamentos acordada: ')

                    if alterador.isdigit():
                        print('Você digitou um numero, valido apenas letras !')

                    convenios['Med']=alterador
                    convenios['Data']=data()
                    salvar_dados()
                    print('\n Alteração realizada com sucesso !!!')

                    desejo=input('Deseja continuar alterando ? s/n ').strip().lower()

                    if desejo=='n':
                        break

                elif acao=='3':
                    alterador=input('Digite a tabela de materiais acordada: ')

                    if alterador.isdigit():
                        print('Você digitou um numero, valido apenas letras! ')

                    convenios['Mat']=alterador
                    convenios['Data']=data()
                    salvar_dados()
                    print('\n Alteração realizada com sucesso !!!')

                    desejo=input('Deseja continuar alterando ? s/n ').strip().lower()
                    if desejo=='n':
                        break

                elif acao=='4':
                    alterador=input('Digite a nova quantidade de fisioterapias por dia na clinica medica (andares): ')

                    if alterador.isdigit():
                        print('Voce digitou um numero, valido somente letras !')

                    convenios['Fisio_andares']=alterador
                    convenios['Data']=data()
                    salvar_dados()
                    print('\n Alteração realizada com sucesso !!!')

                    desejo=input('Deseja continuar alterando ? s/n ').strip().lower()
                    if desejo=='n':
                        break
                elif acao=='5':
                    alterador=input('Digite a nova quantidade de fisioterapia por dia na UTI adulto / neo : ')

                    if alterador.isdigit():
                        print('Você digitou um numero,valido somente letras !')

                    convenios['Fisio_uti']=alterador
                    convenios['Data']=data()
                    salvar_dados()
                    print('\n Alteração realizada com sucesso !!!')

                    desejo=input('Deseja continuar alterando ? s/n ').strip().lower()
                    if desejo=='n':
                        break
                elif acao=='6':
                    alterador=fono()

                    if alterador.isdigit():
                        print('Você digitou um numero,valido somente letras !')

                    convenios['fonoaudiologia']=alterador
                    convenios['Data']=data()
                    salvar_dados()
                    print('\n Alteração realizada com sucesso !!!')

                    desejo=input('Deseja continuar alterando ? s/n ').strip().lower()

                    if desejo=='n':
                        break
       if not resultado:
             print('\n Não localizado convênio \n ')  
    elif menu=='4':

        for convenios in Faturamento:
              print(f'\nConvênio: {convenios['Convenio']}')
              print(f'\nTabela de honorarios medicos: {convenios['Tabela']}')
              print(f'\nTabela de medicamentos acordada: {convenios['Med']}')
              print(f'\nTabela de materias acordada: {convenios['Mat']}')
              print(f'\nQuantidade de fisioterapias por dia na clinica medica(andares):{convenios['Fisio_andares']} ')
              print(f'\nQuantidade de fisioterapias por dia na UTI adulto / Neo : {convenios['Fisio_uti']}')
              print(f'\nQuantidade de fonoaudiologia por dia {convenios['Fonoaudiologia']}')
              print(f'\nData do cadastro das informações: {convenios['Data']}')
              print('-'*30)

    elif menu=='5':
        print('Programa finalizado !!!')
        salvar_dados()
        break
    else:
        print('Digite os numeros que representam as opções do menu !!!')
