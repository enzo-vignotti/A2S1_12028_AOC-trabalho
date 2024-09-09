import sys
from dataclasses import dataclass
# define o número de palavras que cabem na memória RAM
# e o tamanho de cada segmento da RAM

arquivoInstrucoes = 'instrucoes3.txt'
enderecoInicial = 20
CLOCK = 0

def processaLinha(linha : str):
    endereco = -1
    conteudo = -1
    if linha != '':
        elementos = linha.split(sep='|')
        endereco = hex_to_int(elementos[0].strip())
        #print(f'ENDERECO = {endereco}')
        if endereco < enderecoInicial:
            conteudo = hex_to_int(elementos[1].strip())
        else:
            conteudo = '|'.join(elementos[1:])
    return endereco, conteudo
    

class RAM():
    TAMANHO = 150

    def __init__(self):
        self.RAM = [0]*self.TAMANHO
    
    def mostraConteudo(self):
        print(self.RAM)

    def leRAM(self, endereco : int) -> int:
        return self.RAM[endereco]

    def escreveRAM(self, endereco : int, conteudo : int):
        #print(f'ESCREVE NA RAM = {self.RAM[11:17]}')
        self.RAM[endereco] = conteudo

    def iniciaRAM(self, listaLinhas):
        tamListaLinhas = len(listaLinhas)

        for i in range(tamListaLinhas):
            listaLinhas[i] = listaLinhas[i].replace('\n', '')
            listaLinhas[i] = listaLinhas[i].replace('0x', '')
        
        print(f'LISTA LINHAS = {listaLinhas}\n')
        
        for i in range(tamListaLinhas):
            endereco, conteudo = processaLinha(listaLinhas[i])
            self.RAM[endereco] = conteudo
        
        self.mostraConteudo()

        #print(listaLinhas)
        #print(self.RAM)


class Processador():
    def __init__(self):
        self.PC = 0
        self.AC = 0
        self.MAR = 0
        self.MBR = 0
        self.IR = '0|0'
        self.IBR = '0|0'
        self.UnidadeControle = UC(self)

    def IRendereco(self):
        conteudo = self.IR.split(sep='|')
        endereco = hex_to_int(conteudo[1].strip())
        return endereco

    def IRinstrucao(self):
        conteudo = self.IR.split(sep='|')
        return conteudo[0].strip()

    def mostrarRegistradores(self) -> None:
        print('\n--------------------------------------------------')
        print(f'CLOCK : {CLOCK}')
        print('--------------------------------------------------')
        print(f'PC  | {self.PC}')
        print(f'MAR | {self.MAR}')
        print(f'AC  | {self.AC}')
        print(f'MBR | {self.MBR}')
        print(f'IR  | {self.IR}')
        print(f'IBR | {self.IBR}')
        print('--------------------------------------------------\n')


class UC():
    def __init__(self, proc : Processador):
        self.PROC = proc

    def cicloBusca(self, RAM : RAM) -> str:
        """
        Calcula o endereço da instrução, busca a instrução e decodifica a operação
        """
        global CLOCK

        self.PROC.MAR = self.PROC.PC
        CLOCK += 1

        self.PROC.MBR = RAM.leRAM(self.PROC.MAR)
        CLOCK += 1
    
        self.PROC.PC += 1
        self.PROC.IR = self.PROC.MBR
        self.PROC.IBR = '0|0'
        CLOCK += 1
          
        return self.PROC.IRinstrucao()

    def cicloExecucao(self, RAM : RAM, instrucao : str):
        """
        """
        global CLOCK
        fim = False
        # print(f'INSTRUCÃO = {instrucao}')
        match instrucao:
            case 'LOADM':
 
                self.PROC.MAR = self.PROC.IRendereco()
                CLOCK += 1


                self.PROC.MBR = RAM.leRAM(self.PROC.MAR)
                CLOCK += 1


                self.PROC.AC = self.PROC.MBR
                CLOCK += 1

            case 'STORM':
                self.PROC.MBR = self.PROC.AC
                CLOCK += 1
            
                self.PROC.MAR = self.PROC.IRendereco()
                CLOCK += 1

                RAM.escreveRAM(self.PROC.MAR, self.PROC.MBR)
                CLOCK += 1

            case 'STORMR':                
                self.PROC.MAR = self.PROC.IRendereco()
                CLOCK += 1
            
                self.PROC.MBR = RAM.leRAM(self.PROC.MAR)
                CLOCK += 1
            
                self.PROC.IBR = self.PROC.MBR
                CLOCK += 1

                conteudo = self.PROC.IBR.split(sep='|')
                conteudo[1] = int_to_hex(self.PROC.AC)
                buffer = '|'.join(conteudo)
                self.PROC.IBR = buffer
                CLOCK += 1

                self.PROC.MBR = self.PROC.IBR
                CLOCK += 1
                
                RAM.escreveRAM(self.PROC.MAR, self.PROC.MBR)
                CLOCK += 1

            case 'ADDM':                
                self.PROC.MAR = self.PROC.IRendereco()
                CLOCK += 1

                self.PROC.MBR = RAM.leRAM(self.PROC.MAR)
                CLOCK += 1

                self.PROC.AC += self.PROC.MBR
                CLOCK += 1


            case 'SUBM':
                self.PROC.MAR = self.PROC.IRendereco()
                CLOCK += 1                    
                self.PROC.MBR = RAM.leRAM(self.PROC.MAR)
                CLOCK += 1                    
                self.PROC.AC -= self.PROC.MBR
                CLOCK += 1

            case 'JUMPM':
                self.PROC.PC = self.PROC.IRendereco()
                CLOCK += 1

            case 'JUMP+M':
                if self.PROC.AC >= 0:
                    self.PROC.PC = self.PROC.IRendereco()
                CLOCK += 1

            case 'END':
                fim = True
        return fim

    def cicloEscrita():
        print('IMP')


# =======================================================
def hex_to_int(hexa : str) -> int:
    """
    Recebe um valor hexadecimal *hex* em formato de string e retorna seu valor convertido para inteiro
    """
    limpo = hexa

    # agora percorremos todos os caracteres do número fazendo a conversão
    numChar = len(limpo)
    expMax = numChar - 1
    
    num = 0
    for i in range(numChar):
        base = 1 << 4*(expMax - i)
        char = limpo[i]

        match char:
            case '-':
                num += 0
            case '0':
                num += 0
            case '1':
                num += base
            case '2':
                num += base * 2
            case '3':
                num += base * 3
            case '4':
                num += base * 4
            case '5':
                num += base * 5
            case '6':
                num += base * 6
            case '7':
                num += base * 7
            case '8':
                num += base * 8
            case '9':
                num += base * 9
            case 'A':
                num += base * 10
            case 'B':
                num += base * 11
            case 'C':
                num += base * 12
            case 'D':
                num += base * 13
            case 'E':
                num += base * 14
            case 'F':
                num += base * 15
    
    retorno = num
    if limpo[0] == '-':
        print('MENOS')
        retorno = -1 * num
    return retorno

def int_to_hex(num : int) -> str:
    resposta = ''
    qtd = num // 16
    resposta += match(qtd)
    resto = num % 16
    resposta += match(resto)
    return resposta

def match(operando : int):
    match operando:
        case 0: return '0'
        case 1: return '1'
        case 2: return '2'
        case 3: return '3'
        case 4: return '4'
        case 5: return '5'
        case 6: return '6'
        case 7: return '7'
        case 8: return '8'
        case 9: return '9'
        case 10: return 'A'
        case 11: return 'B'
        case 12: return 'C'
        case 13: return 'D'
        case 14: return 'E'
        case 15: return 'F'


# =======================================================

def main():
    global enderecoInicial
    global CLOCK

    ENTRADA = open(arquivoInstrucoes, 'r')
    linhas = ENTRADA.readlines()
    memRAM = RAM()
    PROC = Processador()

    memRAM.iniciaRAM(linhas)
    # Iniciamos o PC com o endereço inicial do código
    PROC.PC = enderecoInicial

    memRAM.mostraConteudo()
    PROC.mostrarRegistradores()

    fim = False
    i = 0
    while not fim:
        CLOCK += 1
        instrucao = PROC.UnidadeControle.cicloBusca(memRAM)

        fim = PROC.UnidadeControle.cicloExecucao(memRAM, instrucao) 
        i += 1
    memRAM.mostraConteudo()

main()

def testeHexToInt():
    print('TESTE HEX TO INT')
    print('HEX = 0xF -> 15')
    a = hex_to_int('0xF')
    print(f'RESPOSTA = {a}')

    print('HEX = 0x1A -> 26')
    a = hex_to_int('0x1A')
    print(f'RESPOSTA = {a}')

    print('HEX = 0xF0C -> 3852')
    a = hex_to_int('0xF0C')
    print(f'RESPOSTA = {a}')

    print('HEX = FF -> 255')
    a = hex_to_int('0xFF')
    print(f'RESPOSTA = {a}')
    return


