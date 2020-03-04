import csv, os, os.path as path, urllib.request as req, random
from typing import List
from canivete import tit, cls, rinput
from funcs import *


data_cont = [[],[]]

J1 = [input('Jogador 1, qual o teu nome?').strip()]
J2 = [input('Jogador 2, qual o teu nome?').strip()]
slot = False
for c in range(2):
    print(f"{tit('Database')}\nJá existe um arquivo disponível no disco\nusá-lo, Descarregar do repositório ou Carregar outro?")
    i = rinput('>>', ['u', 'c', 'd'], '')
    if 'u' in i.lower():
        abre(slot=c)
    elif 'c' in i.lower():
        print('Qual o nome do arquivo?(Sem extensão)\nLembre de verificar se o arquivo\nestá na mesma pasta deste código.')
        while True:
            arquivo = input('>> ').strip()
            if path.isfile(f'{arquivo}.csv') == True:
                abre(arquivo, c)
                break
    elif 'd' in i.lower():
        req.urlretrieve('https://drive.google.com/uc?authuser=0&id=1v-BbhiTD_1pATcrLNttVK0C_akUVnl-l&export=download', 'data1.csv')
        abre(slot=c)
    if c == 0:
        stay = rinput('Usar um slot para cada um?\n[s/n] ', ['s', 'n'], '>>')
        if 'n' in stay.lower():
            break
        if 's' in stay.lower():
            slot = True
            pass

imp = ''
#print(f'{data_cont}\n')
if not slot:
    for a in range(-1, len(data_cont[0])):
        if a == -1:
            pass
            #print(emoji.emojize(f" *|Nv|{'Nome' :>17}|\033[31m:heart:\033[m|\033[31m:fire:\033[m|\033[32m:four_leaf_clover:\033[m|", use_aliases=True))
        else:
            print(f"{(a + 1) :>2}|{data_cont[0][a]['nivel']:>2}|{data_cont[0][a]['nome']:>17}|{data_cont[0][a]['pvt'] :>2}|{data_cont[0][a]['pa']:>2}|{data_cont[0][a]['s']}|{(data_cont[0][a]['pv'] + data_cont[0][a]['s'] + data_cont[0][a]['pa'])}")
    for a in range(1, 3):
        while True:
            if a == 1:
                imp = input(f'{J1[0]} escolha teus personagens\n(Separe por vírgula, 0 - tudo)\n')

            elif a == 2:
                imp = input(f'{J2[0]} escolha teus personagens\n(Separe por vírgula, 0 - tudo)\n')
            esc = imp.strip().split(',')
            n = False
            if imp == '':
                break
            for c in range(0, len(esc)):
                #print(f"For {c} in range, and len(data_cont[0]) == {len(data_cont[0])}")
                if esc[c].isnumeric() == True:
                    esc[c]: int = int(esc[c])
                    if esc[c] <= len(data_cont[0]):
                        if c == len(esc) - 1:
                            n = True
                            #print(n)
                        pass
                    else:
                        break
                else:
                    break
            if n == True:
                if a == 1:
                    print(esc)
                    if len(esc) == 1 and esc[0] == 0:
                        # print('estou dentro')
                        for a in range(0, len(data_cont[0])):
                            # print('passei pelo for in range pela {}° vez.' .format(a+1))
                            J1.append(data_cont[0][a].copy())
                    elif len(esc) != 1 and esc[0] == 0:
                        for a in range(0, len(data_cont[0])):
                            # print('passei pelo for in range pela {}° vez.' .format(a+1))
                            J1.append(data_cont[0][a].copy())
                        for c in range(1, len(esc)):
                            J1.append(data_cont[0][(esc[c] - 1)].copy())
                    else:
                        # print('considerei diferente de zero')
                        for c in esc:
                            J1.append(data_cont[0][c - 1].copy())
                elif a == 2:
                    print(esc)
                    if len(esc) == 1 and esc[0] == 0:
                        print('estou dentro')
                        for a in range(0, len(data_cont[0])):
                            # print('passei pelo for in range pela {}° vez.' .format(a+1))
                            J2.append(data_cont[0][a].copy())
                    elif len(esc) != 1 and esc[0] == 0:
                        for a in range(0, len(data_cont[0])):
                            # print('passei pelo for in range pela {}° vez.' .format(a+1))
                            J2.append(data_cont[0][a].copy())
                        for c in range(0, len(esc)):
                            J2.append(data_cont[0][(esc[c] - 1)].copy())
                    else:
                        # print('considerei else')
                        for c in esc:
                            J2.append(data_cont[0][c - 1].copy())
                break
            if n == False:
                pass
elif slot:
    for a in range(-1, len(data_cont[0])):
        if a == -1:
            print(emoji.emojize(f" *|Nv|{'Nome' :>17}|\033[31m:heart:\033[m|\033[31m:fire:\033[m|\033[32m:four_leaf_clover:\033[m|", use_aliases=True))
        else:
            print(f"{(a + 1) :>2}|{data_cont[0][a]['nivel']:>2}|{data_cont[0][a]['nome']:>17}|{data_cont[0][a]['pvt'] :>2}|{data_cont[0][a]['pa']:>2}|{data_cont[0][a]['s']}|{(data_cont[0][a]['pv'] + data_cont[0][a]['s'] + data_cont[0][a]['pa'])}")
    while True:
        imp = input(f'{J1[0]} escolha teus personagens\n(Separe por vírgula, 0 - tudo)\n')
        esc = imp.strip().split(',')
        n = False
        if imp == '':
            break
        for c in range(0, len(esc)):
            #print(f"For {c} in range, and len(data_cont[0]) == {len(data_cont[0])}")
            if esc[c].isnumeric() == True:
                esc[c]: int = int(esc[c])
                if esc[c] <= len(data_cont[0]):
                    if c == len(esc) - 1:
                        n = True
                        #print(n)
                    pass
                else:
                    break
            else:
                break
        if n == True:
            print(esc)
            if len(esc) == 1 and esc[0] == 0:
                # print('estou dentro')
                for a in range(0, len(data_cont[0])):
                    # print('passei pelo for in range pela {}° vez.' .format(a+1))
                    J1.append(data_cont[0][a].copy())
            elif len(esc) != 1 and esc[0] == 0:
                for a in range(0, len(data_cont[0])):
                    # print('passei pelo for in range pela {}° vez.' .format(a+1))
                    J1.append(data_cont[0][a].copy())
                for c in range(1, len(esc)):
                    J1.append(data_cont[0][(esc[c] - 1)].copy())
            else:
                # print('considerei diferente de zero')
                for c in esc:
                    J1.append(data_cont[0][c - 1].copy())
            break
        if n == False:
            pass
    for a in range(-1, len(data_cont[1])):
        if a == -1:
            print(emoji.emojize(f" *|Nv|{'Nome' :>17}|\033[31m:heart:\033[m|\033[31m:fire:\033[m|\033[32m:four_leaf_clover:\033[m|", use_aliases=True))
        else:
            print(f"{(a + 1) :>2}|{data_cont[1][a]['nivel']:>2}|{data_cont[1][a]['nome']:>17}|{data_cont[1][a]['pvt'] :>2}|{data_cont[1][a]['pa']:>2}|{data_cont[1][a]['s']}|{(data_cont[1][a]['pv'] + data_cont[1][a]['s'] + data_cont[1][a]['pa'])}")
    while True:
        imp = input(f'{J1[0]} escolha teus personagens\n(Separe por vírgula, 0 - tudo)\n')
        esc = imp.strip().split(',')
        n = False
        if imp == '':
            break
        for c in range(0, len(esc)):
            #print(f"For {c} in range, and len(data_cont[1]) == {len(data_cont[1])}")
            if esc[c].isnumeric() == True:
                esc[c]: int = int(esc[c])
                if esc[c] <= len(data_cont[1]):
                    if c == len(esc) - 1:
                        n = True
                        #print(n)
                    pass
                else:
                    break
            else:
                break
        if n == True:
            print(esc)
            if len(esc) == 1 and esc[0] == 0:
                # print('estou dentro')
                for a in range(0, len(data_cont[1])):
                    # print('passei pelo for in range pela {}° vez.' .format(a+1))
                    J2.append(data_cont[1][a].copy())
            elif len(esc) != 1 and esc[0] == 0:
                for a in range(0, len(data_cont[1])):
                    # print('passei pelo for in range pela {}° vez.' .format(a+1))
                    J2.append(data_cont[1][a].copy())
                for c in range(1, len(esc)):
                    J2.append(data_cont[1][(esc[c] - 1)].copy())
            else:
                # print('considerei diferente de zero')
                for c in esc:
                    J2.append(data_cont[1][c - 1].copy())
            break
        if n == False:
            pass


sel = ['nulo']
while True:
    sorte = [False, False, False, False, False, False, False, False, False, False, False, False]
    Print()
    b = acc()
    if int(b[0]) == 100:
        print(f"{J1[0]} Ganhou!!")
        break
    elif int(b[1]) == 100:
        print(f"{J2[0]} Ganhou!!")
        break
    com: List[str] = input('>> ').split(' ')
    """if com[0] != 'sel' or com[0] != 'sub' or com[0] != 'atq' or com[0] != 'sudo' or com[0] != 'ajuda' or com[0] != 'help' or com[0] != 'sair':
        while True:
            com: List[str] = input('>> ').split(' ')
            if com[0] == 'sel' or com[0] == 'sub' or com[0] == 'atq' or com[0] == 'sudo' or com[0] == 'ajuda' or com[0] == 'help' or com[0] == 'sair':
                break"""
    if com[0] == 'sel' and len(com) == 3:
        if com[1].isnumeric() and com[2].isnumeric():
            # sel 1 1
            com[2]: int = int(com[2])
            com[1]: int = int(com[1])
            sel.insert(1, com[1])
            sel.insert(2, com[2])
            while True:
                com: List[str] = input('>> ').split(' ')
                if com[0] == 'sel' and len(com) == 3:
                    if com[1].isnumeric() and com[2].isnumeric():
                        # sel 1 1
                        com[2]: int = int(com[2])
                        com[1]: int = int(com[1])
                        sel.insert(1, com[1])
                        sel.insert(2, com[2])
                elif com[0] == 'sub' and len(com) == 3:
                    if com[2].isnumeric() == True:
                        com[2]: int = int(com[2])
                        if com[1] == 'j1':
                            sel.pop(1)
                            sel.insert(1, com[2])
                        elif com[1] == 'j2':
                            sel.pop()
                            sel.insert(2, com[2])
                elif com[0] != 'sub' and com[0] != 'sel':
                    break
    if com[0] == 'sub':
        while True:
            try:
                if com[2].isnumeric() == True:
                    break
            except IndexError:
                print('Digite quem você quer trocar.')
                com: List[str] = input('>> ').split(' ')
        if sel != ['nulo']:
            com[2]: int = int(com[2])
            if com[1] == 'j1':
                sel.pop(1)
                sel.insert(1, com[2])
            elif com[1] == 'j2':
                sel.pop()
                sel.insert(2, com[2])
            while com[0] == 'sel' or com[0] == 'sub':
                com: List[str] = input('>> ').split(' ')
                if com[0] == 'sel' and com[1].isnumeric() and com[2].isnumeric():
                    # sel 1 1
                    com[2]: int = int(com[2])
                    com[1]: int = int(com[1])
                    sel.insert(1, com[1])
                    sel.insert(2, com[2])
                    com: List[str] = input('>> ').split(' ')
                if com[0] == 'sub' and com[2].isnumeric() == True:
                    com[2]: int = int(com[2])
                    if com[1] == 'j1':
                        sel.pop(1)
                        sel.insert(1, com[2])
                    elif com[1] == 'j2':
                        sel.pop()
                        sel.insert(2, com[2])
            else:
                pass
        else:
            print('Selecione primeiro, antes de substituí-lo\ncomando: sel (Jogador 1) (Jogador 2)')
    if 'atq' == com[0]:
        try:
            if com[1] == 'j1':
                if J1[sel[1]]['pv'] != 0:
                    #print('estou dentro')
                    for c in range(0, (J1[sel[1]]['s'] + 1)):
                        sorte.insert(0, True)
                    rad: int = random.randint(1, (len(sorte) - 1))
                    atdf: bool = sorte[rad]
                    print(rad, atdf)
                    if atdf:
                        print(f"{J2[sel[2]]['nome']} defendeu-se.")
                    else:
                        if J2[sel[2]]['pv'] - J1[sel[1]]['pa'] >= 0:
                            # print('considerei if')
                            J2[sel[2]]['pv'] -= J1[sel[1]]['pa']
                        else:
                            # print('considerei else')
                            J2[sel[2]]['pv'] = 0
                            pass
                    if J2[sel[2]]['pv'] == 0:
                         pass
                else:
                    print(f'{J1[sel[1]]["nome"]} tem 0 de vida, não pode atacar')
                sorte = [False, False, False, False, False, False, False, False, False, False, False, False]
                if J2[sel[2]]['pv'] != 0:
                    # print('estou dentro')
                    for c in range(0, (J1[sel[1]]['s'] + 1)):
                        sorte.insert(0, True)
                    rad: int = random.randint(1, (len(sorte) - 1))
                    atdf: bool = sorte[rad]
                    print(rad, atdf)
                    if atdf:
                        print(f"{J1[sel[1]]['nome']} defendeu-se")
                    else:
                        if J1[sel[1]]['pv'] - J2[sel[2]]['pa'] >= 0:
                            #print('considerei if')
                            J1[sel[1]]['pv'] -= J2[sel[2]]['pa']
                        else:
                            #print('considerei else')
                            J1[sel[1]]['pv'] = 0
                            pass
                    if J1[sel[1]]['pv'] == 0:
                        pass
                else:
                    print(f'{J2[sel[2]]["nome"]} tem 0 de vida, não pode atacar')
            elif com[1] == 'j2':
                if J2[sel[2]]['pv'] != 0:
                    # print('estou dentro')
                    for c in range(0, (J1[sel[1]]['s'] + 1)):
                        sorte.insert(0, True)
                    rad: int = random.randint(1, (len(sorte) - 1))
                    atdf: bool = sorte[rad]
                    print(rad, atdf)
                    if atdf:
                        print(f"{J1[sel[1]]['nome']} defendeu-se")
                    elif atdf == False and J1[sel[1]]['pv'] != 0:
                        if J1[sel[1]]['pv'] - J2[sel[2]]['pa'] >= 0:
                            #print('considerei if')
                            J1[sel[1]]['pv'] -= J2[sel[2]]['pa']
                        else:
                            #print('considerei else')
                            J1[sel[1]]['pv'] = 0
                            pass
                    elif atdf == False and J1[sel[1]]['pv'] == 0:
                        pass
                else:
                    print(f'{J2[sel[2]]["nome"]} tem 0 de vida, não pode atacar')
                sorte = [False, False, False, False, False, False, False, False, False, False, False, False]
                if J1[sel[1]]['pv'] != 0:
                    #print('estou dentro')
                    for c in range(0, (J1[sel[1]]['s'] + 1)):
                        sorte.insert(0, True)
                    rad: int = random.randint(1, (len(sorte) - 1))
                    atdf: bool = sorte[rad]
                    print(rad, atdf)
                    if atdf:
                        print(f"{J2[sel[2]]['nome']} defendeu-se.")
                    elif atdf == False and J2[sel[2]]['pv'] != 0:
                        if J2[sel[2]]['pv'] - J1[sel[1]]['pa'] >= 0:
                            # print('considerei if')
                            J2[sel[2]]['pv'] -= J1[sel[1]]['pa']
                        else:
                            # print('considerei else')
                            J2[sel[2]]['pv'] = 0
                            pass
                    elif atdf == False and J2[sel[2]]['pv'] == 0:
                         pass
                else:
                    print(f'{J1[sel[1]]["nome"]} tem 0 de vida, não pode atacar')
        except IndexError:
            print('Ou você ainda não selecionou os personagens, ou você esqueceu que tem que especificar quem ataca\ncomando: sel (Jogador 1) (Jogador 2)')
    if com[0] == 'sair':
        break
    if com[0] == 'sudo':
        if com[1] == 'hp':
            if com[2] == 'j1' and bool(com[3]) == True and bool(com[4]) == True:
                # sudo hp j1 1 100
                com[4]: int = int(com[4])
                com[3]: int = int(com[3])
                J1[com[3]]['pv'] += com[4]
            if com[2] == 'j2' and bool(com[3]) == True and bool(com[4]) == True:
                # sudo hp j2 1 100
                com[4]: int = int(com[4])
                com[3]: int = int(com[3])
                J2[com[3]]['pv'] += com[4]
        elif com[1] == 'atq':
            try:
                if com[2] == 'j1' and bool(com[3]) and bool(com[4]) and bool(com[5]):
                    # sudo atq j1 100 1 1
                    com[4]: int = int(com[4])
                    com[5]: int = int(com[5])
                    if J2[com[5]]['pv'] != 0:
                        com[3]: int = int(com[3])
                        if J2[com[5]]['pv'] - J1[com[4]]['pa'] >= 0:
                            # print('considerei if')
                            J2[com[5]]['pv'] -= com[3]
                        else:
                            J2[com[5]]['pv'] = 0
                            pass
                    else:
                        pass
                if com[2] == 'j2' and bool(com[3]) and bool(com[4]) and bool(com[5]):
                    # sudo atq j2 100 1 1
                    com[4]: int = int(com[4])
                    com[5]: int = int(com[5])
                    if J1[sel[2]]['pv'] != 0:
                        com[3]: int = int(com[3])
                        if J1[com[5]]['pv'] - J2[com[4]]['pa'] >= 0:
                            # print('considerei if')
                            J1[com[5]]['pv'] -= com[3]
                        else:
                            J1[com[5]]['pv'] = 0
                            pass
                    else:
                        pass
            except IndexError:
                try:
                    if com[2] == 'j1' and bool(com[3]):
                        # sudo atq j1 100
                        if J2[sel[2]]['pv'] != 0:
                            com[3]: int = int(com[3])
                            if J2[sel[2]]['pv'] - J1[sel[1]]['pa'] >= 0:
                                #print('considerei if')
                                J2[sel[2]]['pv'] -= com[3]
                            else:
                                J2[sel[2]]['pv'] = 0
                                pass
                        else:
                            pass
                    if com[2] == 'j2' and bool(com[3]):
                        # sudo atq j2 100
                        if J1[sel[1]]['pv'] != 0:
                            com[3]: int = int(com[3])
                            if J1[sel[1]]['pv'] - J2[sel[2]]['pa'] >= 0:
                                J1[sel[1]]['pv'] -= com[3]
                            else:
                                J1[sel[1]]['pv'] = 0
                                pass
                        else:
                            pass
                except IndexError:
                    print('Você ainda não selecionou os personagens\ncomando: sel (Jogador 1) (Jogador 2)')
    if com[0] == 'help' or com[0] == 'ajuda':
        print('Comandos:\nPara mais detalhes, digite: ajuda [comando]\nsel - selecionar/sub - substituir\natq - ataque / sair - sai da partida')
