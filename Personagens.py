from random import randint
from math import floor


# Definindo a classe Personagem
class Personagem:
    # def __init__(self, nome, vida_maxima, defesa_base, sorte_base, ataque_base, nivel, exp, variacao_especial:float):
    def __init__(self, nome, vida_maxima, defesa_base, sorte_base, ataque_base, variacao_especial:float, status=0):
        self.__nome = nome
        self.__vida_atual = vida_maxima
        self.__vida_maxima = vida_maxima
        self.__defesa_base = defesa_base
        self.__sorte_base = sorte_base
        self.__ataque_base = ataque_base
        # self.__nivel = nivel
        # self.__exp = exp
        self.__variacao_especial:float = variacao_especial
        self.__status = status
        # status: 0 = idle, 1 = defendendo, 2 = atacando
    def get_nome(self):
        return self.__nome
    
    def get_vida_atual(self):
        return self.__vida_atual
    
    def get_vida_maxima(self):
        return self.__vida_maxima

    def get_defesa_base(self):
        return self.__defesa_base

    def get_sorte_base(self):
        return self.__sorte_base
    
    def get_ataque_base(self):
        return self.__ataque_base
    
    # def get_nivel(self):
    #     return self.__nivel

    # def get_exp(self):
    #     return self.__exp
    
    def get_variacao_especial(self):
        return self.__variacao_especial
    
    def get_status(self):
        return self.__status
    
    def set_status(self, status):
        self.__status = status
    
    def set_defender(self):
        # Implementar lógica de defesa
        self.__status = 1
    
    def set_atacar(self):
        # Implementar lógica de ataque
        self.__status = 2
    
    def set_idle(self):
        # Implementar lógica de idle
        self.__status = 0
    
    def get_set_morte(self):
        # Implementar lógica de morte
        if self.__vida_atual <= 0:
            self.__vida_atual = 0
            print(f"{self.__nome} morreu!")
            return True
        return False

    def ma_sorte(self):
        # Implementar lógica de sorte
        # Sorte é um valor booleano que indica se o ataque foi bem-sucedido ou não.
        sorte = randint(1, self.__sorte_base) == self.__vida_atual
        print(f"Má Sorte: {sorte}; {self.__sorte_base} == {self.__vida_atual}")
        return sorte

    def sorte(self):
        # Implementar lógica de sorte
        # Sorte é um valor booleano que indica se o ataque foi bem-sucedido ou não.
        sorte = randint(1, self.__vida_maxima) == self.__vida_atual
        print(f"Sorte: {sorte}; {self.__sorte_base} == {self.__vida_atual}")
        return sorte

    def atacar(self, personagem) -> int:
        if self.get_set_morte():
            print(f"{self.__nome} não pode atacar, está morto(a)!")
            return -1
        # Implementar lógica de ataque
        print(f"{self.__nome} ataca {personagem.get_nome()}!")
        if self.ma_sorte():
            print(f"{self.__nome} errou o ataque!")
            return 0
        elif self.sorte():
            print(f"{self.__nome} acertou um golpe crítico!")
            dano_critico = floor(self.__ataque_base * self.__variacao_especial)
            personagem.ser_atacado(self, dano_critico)
            return 2
        else:
            personagem.ser_atacado(self, self.__ataque_base)
            return 1

    def defender(self, ataque):
        # Implementar lógica de defesa
        dano = ataque - self.__defesa_base
        if dano < 0:
            dano = 0
        self.__vida_atual -= dano
        if self.__vida_atual < 0:
            self.__vida_atual = 0

    def ser_atacado(self, personagem, ataque):
        # Implementar lógica de ser atacado
        match self.__status:
            case 0:
                self.__vida_atual -= ataque
            case 1:
                self.defender(ataque)
            case 2:
                if self.ma_sorte():
                    if self.sorte():
                        print(f"{self.__nome} defendeu o ataque crítico!")
                        return 0
                    print(f"{self.__nome} tomou um golpe crítico!")
                    self.__vida_atual -= ataque * personagem.get_variacao_especial()
                    return 2
                elif self.sorte():
                    print(f"{self.__nome} encontrou uma brecha e contra-atacou!")
                    personagem.ser_atacado(self, ataque)
                    return 3
                else:
                    self.__vida_atual -= ataque
                    return 1
        self.get_set_morte()

        

    def curar(self, cura):
        # Implementar lógica de cura
        pass
    def level_up(self):
        # Implementar lógica de level up
        pass

if __name__ == "__main__":
    monica = Personagem('Mônica', 130, 10, 15, 25, 1.8)
    cebolinha = Personagem('Cebolinha', 90, 15, 35, 18, 3.5)
    print(f"Nome: {monica.get_nome()}")
    print(f"Vida Atual: {monica.get_vida_atual()}")
    print(f"Vida Máxima: {monica.get_vida_maxima()}")
    print(f"Defesa Base: {monica.get_defesa_base()}")
    print(f"Sorte Base: {monica.get_sorte_base()}")
    print(f"Ataque Base: {monica.get_ataque_base()}")
    print(f"Variação Especial: {monica.get_variacao_especial()}")
    print("\n")
    print(f"Nome: {cebolinha.get_nome()}")
    print(f"Vida Atual: {cebolinha.get_vida_atual()}")
    print(f"Vida Máxima: {cebolinha.get_vida_maxima()}")
    print(f"Defesa Base: {cebolinha.get_defesa_base()}")
    print(f"Sorte Base: {cebolinha.get_sorte_base()}")
    print(f"Ataque Base: {cebolinha.get_ataque_base()}")
    print(f"Variação Especial: {cebolinha.get_variacao_especial()}")
    print("\n")
    # Testando o ataque
    def status():
        print(f"       {monica.get_nome()}\tVS.\t{cebolinha.get_nome()}!")
        print(f"      Vida Atual: {monica.get_vida_atual()}\tVS.\t{cebolinha.get_vida_atual()}")
        print(f"      Defesa Base: {monica.get_defesa_base()}\tVS.\t{cebolinha.get_defesa_base()}")
        print(f"      Sorte Base: {monica.get_sorte_base()}\tVS.\t{cebolinha.get_sorte_base()}")
        print(f"      Ataque Base: {monica.get_ataque_base()}\tVS.\t{cebolinha.get_ataque_base()}")
        print(f"Variação Especial: {monica.get_variacao_especial()}\tVS.\t{cebolinha.get_variacao_especial()}")
    def main():
        print("Iniciando o combate!")
        monica.set_atacar()
        cebolinha.set_defender()
        monica.atacar(cebolinha)
        cebolinha.set_idle()
        cebolinha.set_atacar()
        monica.set_idle()
        cebolinha.atacar(monica)
        status()
    
    main()