from os import path, system


def tit(txt):
    t = int(len(txt) + 8)
    print('-' * t)
    print(f'{txt:^{t}}')
    print('-' * t)


def cls():
    android: bool = path.exists('/storage/emulated/0')
    windows: bool = path.exists('C:/Program Files')
    linux: bool = path.exists('/home/')
    if android or linux:
        system('clear')
    if windows:
        system('cls')


def limpa():
    """
    Função que limpa a tela
    """
    if path.isdir('C:/'):
        system('cls')
    if path.isdir('/storage/emulated/0/'):
        system('clear')


# noinspection PyArgumentList
def linque(caminho, form='r', asci=True):
    """
    Função que linca o arquivo
    :type asci: bool
    :type form: object
    :param caminho: indica o caminho do arquivo
    :param asci: leitura de códigos ascii, que
    para ativar escreva False para ele
    :return: a
    """
    if path.isfile(caminho, form):
        return open(caminho, form, ensure_ascii=asci)


def pc():
    if path.isdir('C:/'):
        return 'windows'
    elif path.isdir('/storage/emulated/0/'):
        return 'android/linux'


def rinput(texto: object, b: object = None, enfeite: object = ':', errormsg = 'Tente novamente.'):
    """
    Função que não para de executar input
    até que você digite alguma coisa ou
    digite a coisa correta.
    :type texto: object
    :param texto: Exibe no input
    :type b: object
    :param b: lista de condição
    :return: var c
    """
    if b is None:
        b = False
    cont = -1
    while True:
        cont += 1
        if cont == 0:
            c = input(f'{texto}{enfeite} ')
        else:
            c = input(f'{errormsg}\n{texto}{enfeite} ')
        if c == '':
            limpa()
            pass
        else:
            if not b:
                return str(c)
            else:
                if c in b:
                    return str(c)
                else:
                    pass
