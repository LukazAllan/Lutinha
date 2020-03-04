def abre(arg='data', slot=0):
    """
    abre arquivos .csv somente para este jogo
    :param arg: nome do .csv que será aberto
    :param slot: não faço ideia
    """
    with open(f'{arg}.csv', encoding='utf-8') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        #print(data)
        #cls()
        cont: int = -1
        for row in data:
            cont += 1
            data_cont[slot].append({'nivel' : row[0], 'nome' : row[1], 'pv' : row[2], 'pvt' : row[2], 'pa' : row[3], 's' : row[4]})
            if row[0] != '-':
                for a in ('nivel', 'pv', 'pvt', 'pa', 's'):
                    data_cont[slot][cont][a] = int(data_cont[slot][cont][a])
            else:
                pass
    csvfile.close()


def acc():
    pa1 = int(0)
    pv1 = int(0)
    ps1 = int(0)
    pa2 = int(0)
    pv2 = int(0)
    ps2 = int(0)
    for c in range(1, len(J1)):
        if J1[c]['pv'] != 0:
            pv1 = pv1 + int(J1[c]['pv'])
            pa1 = pa1 + int(J1[c]['pa'])
            ps1 = ps1 + int(J1[c]['s'])
        else:
            pass
    for c in range(1, len(J2)):
        if J2[c]['pv'] != 0:
            pv2 = pv2 + int(J2[c]['pv'])
            pa2 = pa2 + int(J2[c]['pa'])
            ps2 = ps2 + int(J2[c]['s'])
        else:
            pass
    ac1 = ((pa1+pv1+ps1)/(pa1+pv1+ps1+pa2+pv2+ps2)*100)
    ac2 = ((pa2+pv2+ps2)/(pa1+pv1+ps1+pa2+pv2+ps2)*100)
    return (ac1, ac2)


def Print():
    a = acc()
    if a[0] >= 60 and a[1] <= 40:
        if a[0] != 100:
            if a[0] <= 90:
                print(f"\033[7;32m{'Ganhando':>17} {a[0] :.2f}%\033[m{' ' * 7}\033[7;31m{a[1] :.2f}%{' ' * 18}\033[m")
                print(f"\033[7;32m{J1[0]:>24}\033[m{' ' * 7}\033[7;31m{J2[0]:<24}\033[m")
            else:
                print(f"\033[7;32m{'Ganhando':>17} {a[0] :.2f}%\033[m{' ' * 7}\033[7;31m{a[1] :.2f}%{' ' * 19}\033[m")
                print(f"\033[7;32m{J1[0]:>24}\033[m{' ' * 7}\033[7;31m{J2[0]:<24}\033[m")
        else:
            print(f"\033[7;32m{'Ganhou':>16} {a[0] :.2f}%\033[m{' ' * 7}\033[7;31m{a[1] :.2f}%{' ' * 19}\033[m")
            print(f"\033[7;32m{J1[0]:>24}\033[m{' ' * 7}\033[7;31m{J2[0]:<24}\033[m")
    elif a[0] <= 40 and a[1] >= 60:
        if a[1] != 100:
            print(f"\033[7;31m{a[0] :>23.2f}%\033[m{' ' * 7}\033[7;32m{a[1] :<4.2f}% Ganhando{' ' * 9}\033[m")
            print(f"\033[7;31m{J1[0]:>24}\033[m{' ' * 7}\033[7;32m{J2[0]:<24}\033[m")
        else:
            print(f"\033[7;31m{a[0] :>23.2f}%\033[m{' ' * 7}\033[7;32m{a[1] :<4.2f}% Ganhou{' ' * 10}\033[m")
            print(f"\033[7;31m{J1[0]:>24}\033[m{' ' * 7}\033[7;32m{J2[0]:<24}\033[m")
    else:
        print(f"{a[0] :>24.2f}%{' ' * 7}{a[1] :.2f}%")
        print(f"{J1[0]:>24}{' ' * 7}{J2[0]}")
    if len(J1) == len(J2):
        for c in range(1, len(J1)):
            if J1[c]['pv'] > (2 * J1[c]['pvt'] / 3):
                print(f"\033[7;32m{J1[c]['nome'] :>17} {J1[c]['pa']:>2} {J1[c]['pv'] :>3}\033[m  {c :>2}   ", end='')
            elif (J1[c]['pvt'] / 3) < J1[c]['pv'] <= (2 * J1[c]['pvt'] / 3):
                print(f"\033[7;33m{J1[c]['nome'] :>17} {J1[c]['pa']:>2} {J1[c]['pv'] :>3}\033[m  {c :>2}   ", end='')
            elif 0 < J1[c]['pv'] <= (J1[c]['pvt'] / 3):
                print(f"\033[7;31m{J1[c]['nome'] :>17} {J1[c]['pa']:>2} {J1[c]['pv'] :>3}\033[m  {c :>2}   ", end='')
            elif J1[c]['pv'] == 0:
                print(f"\033[7;30m{J1[c]['nome'] :>17} {J1[c]['pa']:>2} {J1[c]['pv'] :>3}\033[m  {c :>2}   ", end='')
            if J2[c]['pv'] > (2 * J2[c]['pvt'] / 3):
                print(f"\033[7;32m{J2[c]['pv'] :<3} {J2[c]['pa']:>2} {J2[c]['nome'] :<17}\033[m")
            elif (J2[c]['pvt'] / 3) < J2[c]['pv'] <= (2 * J2[c]['pvt'] / 3):
                print(f"\033[7;33m{J2[c]['pv'] :<3} {J2[c]['pa']:>2} {J2[c]['nome'] :<17}\033[m")
            elif 0 < J2[c]['pv'] <= (J2[c]['pvt'] / 3):
                print(f"\033[7;31m{J2[c]['pv'] :<3} {J2[c]['pa']:>2} {J2[c]['nome'] :<17}\033[m")
            elif J2[c]['pv'] == 0:
                print(f"\033[7;30m{J2[c]['pv'] :<3} {J2[c]['pa']:>2} {J2[c]['nome'] :<17}\033[m")

    elif len(J1) != len(J2):
        if len(J1) > len(J2):
            for c in range(1, len(J2)):
                if J1[c]['pv'] > (2 * J1[c]['pvt'] / 3):
                    print(f"\033[7;32m{J1[c]['nome'] :>17} {J1[c]['pa']:>2} {J1[c]['pv'] :>3}\033[m  {c :>2}   ", end='')
                elif (J1[c]['pvt'] / 3) < J1[c]['pv'] <= (2 * J1[c]['pvt'] / 3):
                    print(f"\033[7;33m{J1[c]['nome'] :>17} {J1[c]['pa']:>2} {J1[c]['pv'] :>3}\033[m  {c :>2}   ", end='')
                elif 0 < J1[c]['pv'] <= (J1[c]['pvt'] / 3):
                    print(f"\033[7;31m{J1[c]['nome'] :>17} {J1[c]['pa']:>2} {J1[c]['pv'] :>3}\033[m  {c :>2}   ", end='')
                elif J1[c]['pv'] == 0:
                    print(f"\033[7;30m{J1[c]['nome'] :>17} {J1[c]['pa']:>2} {J1[c]['pv'] :>3}\033[m  {c :>2}   ", end='')
                if J2[c]['pv'] > (2 * J2[c]['pvt'] / 3):
                    print(f"\033[7;32m{J2[c]['pv'] :<3} {J2[c]['pa']:>2} {J2[c]['nome'] :<17}\033[m")
                elif (J2[c]['pvt'] / 3) < J2[c]['pv'] <= (2 * J2[c]['pvt'] / 3):
                    print(f"\033[7;33m{J2[c]['pv'] :<3} {J2[c]['pa']:>2} {J2[c]['nome'] :<17}\033[m")
                elif 0 < J2[c]['pv'] <= (J2[c]['pvt'] / 3):
                    print(f"\033[7;31m{J2[c]['pv'] :<3} {J2[c]['pa']:>2} {J2[c]['nome'] :<17}\033[m")
                elif J2[c]['pv'] == 0:
                    print(f"\033[7;30m{J2[c]['pv'] :<3} {J2[c]['pa']:>2} {J2[c]['nome'] :<17}\033[m")
            for a in range(len(J2), len(J1)):
                if J1[a]['pv'] > (2 * J1[a]['pvt'] / 3):
                    print(f"\033[7;32m{J1[a]['nome'] :>17} {J1[a]['pa']:>2} {J1[a]['pv'] :>3}\033[m  {a :>2}   ")
                elif (J1[a]['pvt'] / 3) < J1[a]['pv'] <= (2 * J1[a]['pvt'] / 3):
                    print(f"\033[7;33m{J1[a]['nome'] :>17} {J1[a]['pa']:>2} {J1[a]['pv'] :>3}\033[m  {a :>2}   ")
                elif 0 < J1[a]['pv'] <= (J1[a]['pvt'] / 3):
                    print(f"\033[7;31m{J1[a]['nome'] :>17} {J1[a]['pa']:>2} {J1[a]['pv'] :>3}\033[m  {a :>2}   ")
                elif J1[a]['pv'] == 0:
                    print(f"\033[7;30m{J1[a]['nome'] :>17} {J1[a]['pa']:>2} {J1[a]['pv'] :>3}\033[m  {a :>2}   ")
        elif len(J1) < len(J2):
            for c in range(1, len(J1)):
                if J1[c]['pv'] > (2 * J1[c]['pvt'] / 3):
                    print(f"\033[7;32m{J1[c]['nome'] :>17} {J1[c]['pa']:>2} {J1[c]['pv'] :>3}\033[m  {c :>2}   ", end='')
                elif (J1[c]['pvt'] / 3) < J1[c]['pv'] <= (2 * J1[c]['pvt'] / 3):
                    print(f"\033[7;33m{J1[c]['nome'] :>17} {J1[c]['pa']:>2} {J1[c]['pv'] :>3}\033[m  {c :>2}   ", end='')
                elif 0 < J1[c]['pv'] <= (J1[c]['pvt'] / 3):
                    print(f"\033[7;31m{J1[c]['nome'] :>17} {J1[c]['pa']:>2} {J1[c]['pv'] :>3}\033[m  {c :>2}   ", end='')
                elif J1[c]['pv'] == 0:
                    print(f"\033[7;30m{J1[c]['nome'] :>17} {J1[c]['pa']:>2} {J1[c]['pv'] :>3}\033[m  {c :>2}   ", end='')
                if J2[c]['pv'] > (2 * J2[c]['pvt'] / 3):
                    print(f"\033[7;32m{J2[c]['pv'] :<3} {J2[c]['pa']:>2} {J2[c]['nome'] :<17}\033[m")
                elif (J2[c]['pvt'] / 3) < J2[c]['pv'] <= (2 * J2[c]['pvt'] / 3):
                    print(f"\033[7;33m{J2[c]['pv'] :<3} {J2[c]['pa']:>2} {J2[c]['nome'] :<17}\033[m")
                elif 0 < J2[c]['pv'] <= (J2[c]['pvt'] / 3):
                    print(f"\033[7;31m{J2[c]['pv'] :<3} {J2[c]['pa']:>2} {J2[c]['nome'] :<17}\033[m")
                elif J2[c]['pv'] == 0:
                    print(f"\033[7;30m{J2[c]['pv'] :<3} {J2[c]['pa']:>2} {J2[c]['nome'] :<17}\033[m")
            for a in range(len(J1), len(J2)):
                if J2[a]['pv'] > (2 * J2[a]['pvt'] / 3):
                    print(f"{'' :>26}{a :>2}   \033[7;32m{J2[a]['pv'] :<3} {J2[a]['pa']:>2} {J2[a]['nome'] :<17}\033[m")
                elif (J2[a]['pvt'] / 3) < J2[a]['pv'] <= (2 * J2[a]['pvt'] / 3):
                    print(f"{'' :>26}{a :>2}   \033[7;33m{J2[a]['pv'] :<3} {J2[a]['pa']:>2} {J2[a]['nome'] :<17}\033[m")
                elif 0 < J2[a]['pv'] <= (J2[a]['pvt'] / 3):
                    print(f"{'' :>26}{a :>2}   \033[7;31m{J2[a]['pv'] :<3} {J2[a]['pa']:>2} {J2[a]['nome'] :<17}\033[m")
                elif J2[a]['pv'] == 0:
                    print(f"{'' :>26}{a :>2}   \033[7;30m{J2[a]['pv'] :<3} {J2[a]['pa']:>2} {J2[a]['nome'] :<17}\033[m")
