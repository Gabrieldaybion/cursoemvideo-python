from time import sleep
def pr(v1,v2):
    print(f'{v1}={v2}')
def binary_programa():
    print('Iniciando app.')
    a='01100001'
    b='01100010'
    c='01100011'
    d='01100100'
    e='01100101'
    f='01100110'
    g='01100111'
    h='01101000'
    i='01101001'
    j='01101010'
    k='01101011'
    l='01101100'
    m='01101101'
    n='01101110'
    o='01101111'
    p='01110000'
    q='01110001'
    r='01110010'
    s='01110011'
    t='01110100'
    u='01110101'
    v='01110110'
    w='01110111'
    x='01111000'
    y='01111001'
    z='01111010'
    sleep(0.6)
    try:
        print('Digite uma letra em minusculo, para transformar em codigo binario.')
        print('Digite [sair: Para sair. ')
        while True:
            gg=input('==: ')
            if gg=='':
                print('Você não digitou nada.')

            elif gg==' ':
                print('Desculpe mas precionar espaço não conta como uma letra.')


            elif gg=='sair':
                break
            elif gg=='a':
                pr(gg,a)

            elif gg=='b':
                pr(gg,b)

            elif gg=='c':
                pr(gg,c)

            elif gg=='d':
                pr(gg,d)

            elif gg=='e':
                pr(gg,e)

            elif gg=='f':
                pr(gg,f)

            elif gg=='g':
                pr(gg,g)

            elif gg=='h':
                pr(gg,h)

            elif  gg=='i':
                pr(gg,i)

            elif gg=='j':
                pr(gg,j)

            elif gg=='k':
                pr(gg,k)

            elif gg=='l':
                pr(gg,l)

            elif gg=='m':
                pr(gg,m)

            elif gg=='n':
                pr(gg,n)

            elif gg=='o':
                pr(gg,o)

            elif gg=='p':
                pr(gg,p)

            elif gg=='q':
                pr(gg,q)

            elif gg=='r':
                pr(gg,r)

            elif gg=='s':
                pr(gg,s)

            elif gg=='t':
                pr(gg,t)

            elif gg=='u':
                pr(gg,u)

            elif gg=='v':
                pr(gg,v)

            elif gg=='w':
                pr(gg,w)

            elif gg=='x':
                pr(gg,x)

            elif gg=='y':
                pr(gg,y)

            elif gg=='z':
                pr(gg,z)

            else:
                print('Desculpe-me, mas a letra não bate no  banco de dados, pfv digite uma letra de cada vez.')
        print('''[1]Transformar binário em letra.
[2].Transformar letra em binario.
[3]Sair.''')

    except (ValueError,TypeError):
             print('Desculpe mas o app deu algum problema. Então irémos reiniciar.')
    finally:
        print('App concluiu seu obetivo.')

def binary_programa_2():
    print('Iniciando App.')
    try:
        print('Digite o codigo binario.Apenas um codigo, e irá transformar em letra.')
        print('Digite sair, para sair do programa.')
        letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v','w', 'x', 'y', 'z',]
        valores=['sair','01100001','01100001','01100001',
                  '01100100','01100101','01100110','01101000','01101001','01101010',
                  '01101011','01101100','01101101','01101101','01101110','01101111',
                  '01110000','01110001','01110010','01110011','01110100',
                  '01110101','01110110','01110111','01111000','01111001','01111010',]

        a = '01100001'
        b = '01100010'
        c = '01100011'
        d = '01100100'
        e = '01100101'
        f = '01100110'
        g = '01100111'
        h = '01101000'
        i = '01101001'
        j = '01101010'
        k = '01101011'
        l = '01101100'
        m = '01101101'
        n = '01101110'
        o = '01101111'
        p = '01110000'
        q = '01110001'
        r = '01110010'
        s = '01110011'
        t = '01110100'
        u = '01110101'
        v = '01110110'
        w = '01110111'
        x = '01111000'
        y = '01111001'
        z = '01111010'

        try:
         while True:
            po = input('==: ')
            if po == '':
                print('Desculpe,mas você não digitou nada.')

            elif po == ' ':
                print('Desculpe mas vc digitou espaço.')

            elif po == letras:
                print('Desculpe,mas letra nesse programa não pode ser covertido.')

            elif po == letras[1]:
             print('Desculpe,mas letra nesse programa não pode ser covertido.')

            elif po == letras[2]:
                print('Desculpe,mas letra nesse programa não pode ser covertido.')

            elif po == letras[3]:
                print('Desculpe,mas letra nesse programa não pode ser covertido.')

            elif po == letras[4]:
                print('Desculpe,mas letra nesse programa não pode ser covertido.')

            elif po == letras[5]:
                print('Desculpe,mas letra nesse programa não pode ser covertido.')

            elif po == letras[6]:
                print('Desculpe,mas letra nesse programa não pode ser covertido.')

            elif po == letras[7]:
                print('Desculpe,mas letra nesse programa não pode ser covertido.')

            elif po == letras[8]:
                print('Desculpe,mas letra nesse programa não pode ser covertido.')

            elif po == letras[9]:
                print('Desculpe,mas letra nesse programa não pode ser covertido.')

            elif po == letras[10]:
                print('Desculpe,mas letra nesse programa não pode ser covertido.')

            elif po == letras[11]:
                print('Desculpe,mas letra nesse programa não pode ser covertido.')

            elif po == letras[12]:
                print('Desculpe,mas letra nesse programa não pode ser covertido.')

            elif po == letras[12]:
                print('Desculpe,mas letra nesse programa não pode ser covertido.')

            elif po == letras[13]:
                print('Desculpe,mas letra nesse programa não pode ser covertido.')

            elif po == letras[14]:
                print('Desculpe,mas letra nesse programa não pode ser covertido.')

            elif po == letras[15]:
                print('Desculpe,mas letra nesse programa não pode ser covertido.')

            elif po == letras[16]:
                print('Desculpe,mas letra nesse programa não pode ser covertido.')

            elif po == letras[17]:
                print('Desculpe,mas letra nesse programa não pode ser covertido.')

            elif po == letras[18]:
                print('Desculpe,mas letra nesse programa não pode ser covertido.')

            elif po == letras[19]:
                print('Desculpe,mas letra nesse programa não pode ser covertido.')

            elif po == letras[20]:
                print('Desculpe,mas letra nesse programa não pode ser covertido.')

            elif po == letras[21]:
                print('Desculpe,mas letra nesse programa não pode ser covertido.')

            elif po == letras[22]:
                print('Desculpe,mas letra nesse programa não pode ser covertido.')

            elif po == letras[23]:
                print('Desculpe,mas letra nesse programa não pode ser covertido.')

            elif po == letras[24]:
                print('Desculpe,mas letra nesse programa não pode ser covertido.')

            elif po == letras[25]:
                print('Desculpe,mas letra nesse programa não pode ser covertido.')

            elif po==valores[0]:
                    break
#Ifs só para ver se escreveu alguma letra.Ps o codido no futuro precisa ser atualizado.
            elif po=='01100001':
                print(f'{po}=a')
                print()
            elif po=='01100010':
                print(f'{po}=b')

            elif po=='01100011':
                print(f'{po}=c')

            elif po=='01100100':
                print(f'{po}=d')

            elif po=='01100100':
                print(f'{po}=e')

            elif po=='01100110':
                print(f'{po}=f')

            elif po=='01100111':
                print(f'{po}=g')

            elif po=='01101000':
                print(f'{po}=h')

            elif po=='01101001':
                print(f'{po}=i')

            elif po=='01101010':
                print(f'{po}=j')

            elif po=='01101011':
                print(f'{po}=k')

            elif po=='01101100':
                print(f'{po}=l')

            elif po=='01101101':
                print(f'{po}=m')

            elif po=='01101110':
                print(f'{po}=n')

            elif po=='01101111':
                print(f'{po}=o')

            elif po=='01110000':
                print(f'{po}=p')

            elif po=='01110001':
                print(f'{po}=q')

            elif po=='01110010':
                print(f'{po}=r')

            elif po=='01110011':
                print(f'{po}=s')

            elif po=='01110100':
                print(f'{po}=t')

            elif po=='01110101':
                print(f'{po}=u')

            elif po=='01110110':
                print(f'{po}=v')

            elif po=='01110111':
                print(f'{po}=w')

            elif po=='01111000':
                print(f'{po}=x')

            elif po=='01111001':
                print(f'{po}=y')

            elif po=='01111010':
                print(f'{po}=z')

            else:
                print('Desculpe o caractere inserido não pode ser confertido.')

        except(IndexError):
            print('Desculpe mas valor inserido deu erro. Escolha novamente.')

    except(TypeError):
        print('Desculpe.Mas o app irá reineciar.')
    finally:
        print('Ótimo acredetido que app tenha concluído.')
    print('-'*35)
    print('''[1]Transformar binário em letra.
[2]Transformar letra em binario.
[3]Sair.''')
    print('-'*35)