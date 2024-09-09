# ------- TRABALHO DE ARQUITETURA E ORGANIZAÇÃO DE COMPUTADORES ------------------
# ALUNOS
# ENZO VIGNOTTI SABINO            - RA: 133791
# GABRIEL MARCOS DA SILVA PERUZZI - RA: 134912
# MATHEUS KOCHEPKI CAMPANER       - RA: 126609

import sys

arquivoSAIDA = 'log_out.txt'
CLOCK = 0
FIM = False

def processaLinha(linha : str) -> int | str:
    """
    Recebe uma *linha* do arquivo de instruções e recupera seu endereço e seu conteúdo separadamente
    """
    endereco = -1
    conteudo = 0
    if linha != '':
        elementos = linha.split(sep='|')
        endereco = int(elementos[0].strip(), 16)      # recupera o endereço e o converte de hexa para inteiro
        # se o endereço for menor do que o endereço inicial das instruções,
        # então o conteúdo será um número inteiro
        if endereco < enderecoInicial:
            conteudo = int(elementos[1].strip(), 16)  # recupera o endereço e o converte de hexa para inteiro
        else:
            conteudo = '|'.join(elementos[1:]) # reconstroi a sintaxe das linhas de instrução
    return endereco, conteudo
    

class RAM():
    def __init__(self, TAMANHO : int):
        self.TAMAMNHO = TAMANHO
        self.RAM = [0]*TAMANHO
    
    def mostraConteudo(self):
        """
        Printa todo o conteúdo da RAM
        """
        print(self.RAM)

    def leRAM(self, endereco : int) -> int:
        """
        Retorna o conteúdo de um *endereco* da RAM
        """
        return self.RAM[endereco]

    def escreveRAM(self, endereco : int, conteudo : int) -> None:
        """
        Recebe um *conteudo* e o escreve no devido *endereco*
        """
        self.RAM[endereco] = conteudo

    def iniciaRAM(self, listaLinhas : list[str]) -> None:
        """
        Recebe as linhas do arquivo de instruções e escreve o conteúdo na memória RAM
        seguindo os endereços indicados
        """
        tamListaLinhas = len(listaLinhas)
        # loop para "limpar" as linhas recebidas
        for i in range(tamListaLinhas):
            listaLinhas[i] = listaLinhas[i].replace('\n', '')
            listaLinhas[i] = listaLinhas[i].replace('0x', '')

        # loop para escrever o conteúdo de cada linha no local correto da RAM
        for i in range(tamListaLinhas):
            endereco, conteudo = processaLinha(listaLinhas[i])
            self.RAM[endereco] = conteudo

    def escreveSAIDA(self, ARQ : str):
        """
        Escreve todo o conteúdo da RAM em um *ARQ* de saída
        """
        SAIDA = open(ARQ, 'w')
        buffer = []
        for i in range(len(self.RAM)):
            endereco = hex(i)
            conteudo = str(self.RAM[i])
            celula = endereco + ' | ' + conteudo + '\n'
            buffer.append(celula)
        SAIDA.writelines(buffer)

class Processador():
    def __init__(self):
        self.PC = 0
        self.AC = 0
        self.MQ = 0
        self.MAR = 0
        self.MBR = 0
        self.IR = '0|0'
        self.R = 0
        self.C = 2
        self.Z = 0
        self.UnidadeControle = UC(self)

    def IRendereco(self) -> int:
        """
        Recupera o campo de endereço da instrução que está no IR
        """
        conteudo = self.IR.split(sep='|')
        endereco = int(conteudo[1].strip(), 16)
        return endereco

    def IRinstrucao(self) -> str:
        """
        Recupera o mnemônico da instrução que está no IR
        """
        conteudo = self.IR.split(sep='|')
        return conteudo[0].strip()

    def mostrarRegistradores(self) -> None:
        """
        Printa o nome dos registradores e seus conteúdos na tela
        """
        print('--------------------------------------------------')
        print(f'CLOCK : {CLOCK}')
        print('--------------------------------------------------')
        print(f'PC  | {self.PC}')
        print(f'MAR | {self.MAR}')
        print(f'MQ  | {self.MQ}')
        print(f'AC  | {self.AC}')
        print(f'MBR | {self.MBR}')
        print(f'IR  | {self.IR}')
        print(f'R   | {self.R}')
        print(f'C   | {self.C}')
        print(f'Z   | {self.Z}')
        print('--------------------------------------------------')


class UC():
    def __init__(self, proc : Processador) -> None:
        self.PROC = proc

    def cicloBusca(self, RAM : RAM) -> str:
        """
        Calcula o endereço da instrução, busca a instrução e decodifica a operação
        """
        global CLOCK

        CLOCK += 1
        self.PROC.MAR = self.PROC.PC

        CLOCK += 1
        self.PROC.MBR = RAM.leRAM(self.PROC.MAR)

        CLOCK += 1
        self.PROC.PC += 1
        self.PROC.IR = self.PROC.MBR

        instrucao = self.PROC.IRinstrucao()
        print('\n--------------------------------------------------')
        print(f'CICLO DE BUSCA - INSTRUÇÃO RECUPERADA : {instrucao}')
        self.PROC.mostrarRegistradores()

    def cicloExecucao(self, RAM : RAM):
        """
        Lê a instrução que deve ser executada e realiza a sequencia de microoperações correspondetes
        """
        global CLOCK
        global FIM

        instrucao = self.PROC.IRinstrucao()

        match instrucao:
            case 'LOADM':
                CLOCK += 1
                self.PROC.MAR = self.PROC.IRendereco()

                CLOCK += 1
                self.PROC.MBR = RAM.leRAM(self.PROC.MAR)

                CLOCK += 1
                self.PROC.AC = self.PROC.MBR

            case 'LOADMQM':
                CLOCK += 1
                self.PROC.MAR = self.PROC.IRendereco()

                CLOCK += 1
                self.PROC.MBR = RAM.leRAM(self.PROC.MAR)

                CLOCK += 1
                self.PROC.MQ = self.PROC.MBR

            case 'STORM':
                CLOCK += 1                
                self.PROC.MBR = self.PROC.AC

                CLOCK += 1
                self.PROC.MAR = self.PROC.IRendereco()

                CLOCK += 1
                RAM.escreveRAM(self.PROC.MAR, self.PROC.MBR)

            case 'STORMR':
                CLOCK += 1                
                self.PROC.MAR = self.PROC.IRendereco()

                CLOCK += 1
                self.PROC.MBR = RAM.leRAM(self.PROC.MAR)

                CLOCK += 1
                conteudo = self.PROC.MBR.split(sep='|')
                conteudo[1] = hex(self.PROC.AC)
                buffer = '|'.join(conteudo)
                self.PROC.MBR = buffer

                CLOCK += 1
                RAM.escreveRAM(self.PROC.MAR, self.PROC.MBR)

            case 'ADDM':
                CLOCK += 1                
                self.PROC.MAR = self.PROC.IRendereco()

                CLOCK += 1
                self.PROC.MBR = RAM.leRAM(self.PROC.MAR)

                CLOCK += 1
                self.PROC.AC += self.PROC.MBR
                
                if (self.PROC.AC < 0): self.PROC.Z = -1
                elif (self.PROC.AC == 0): self.PROC.Z = 0
                else: self.PROC.Z = 1

            case 'SUBM':
                CLOCK += 1
                self.PROC.MAR = self.PROC.IRendereco()

                CLOCK += 1                    
                self.PROC.MBR = RAM.leRAM(self.PROC.MAR)

                CLOCK += 1                    
                self.PROC.AC -= self.PROC.MBR

                if (self.PROC.AC < 0): self.PROC.Z = -1
                elif (self.PROC.AC == 0): self.PROC.Z = 0
                else: self.PROC.Z = 1                

            case 'MULM':
                CLOCK += 1
                self.PROC.MAR = self.PROC.IRendereco()

                CLOCK += 1
                self.PROC.MBR = RAM.leRAM(self.PROC.MAR)

                CLOCK += 1
                self.PROC.AC = self.PROC.MBR * self.PROC.MQ

                if (self.PROC.AC < 0): self.PROC.Z = -1
                elif (self.PROC.AC == 0): self.PROC.Z = 0
                else: self.PROC.Z = 1                

            case 'JUMPM':
                CLOCK += 1
                self.PROC.PC = self.PROC.IRendereco()

            case 'JUMP+M':
                CLOCK += 1
                if self.PROC.AC >= 0:
                    self.PROC.PC = self.PROC.IRendereco()

            case 'END':
                CLOCK += 1
                self.PROC.MAR = 0
                self.PROC.MBR = 0
                self.PROC.AC = 0
                self.PROC.IR = '0|0'
                self.PROC.MQ = 0
                self.PROC.PC = 0
                FIM = True
        print('\n--------------------------------------------------')
        print(f'CICLO DE EXECUÇÃO - INSTRUÇÃO EXECUTADA : {instrucao}')
        self.PROC.mostrarRegistradores()

# =======================================================
# =======================================================

def main(inicio : int, IN : str, OUT : str, modo : str):
    global CLOCK
    global FIM

    memRAM = RAM(100) # RAM criada com um tamanho de 150 palavras
    PROC = Processador()
    ENTRADA = open(IN, 'r')

    linhas = ENTRADA.readlines()
    memRAM.iniciaRAM(linhas)

    # Iniciamos o PC com o endereço inicial do código
    PROC.PC = inicio

    PROC.mostrarRegistradores()

    if modo == '-d':
        while not FIM:
                PROC.UnidadeControle.cicloBusca(memRAM)
                PROC.UnidadeControle.cicloExecucao(memRAM) 
    else:
        while not FIM:
            tecla = input('[S]air / ENTER para continuar : ').upper()
            if tecla == '':
                PROC.UnidadeControle.cicloBusca(memRAM)
            elif tecla == 'S':
                print("\nPROGRAMA ENCERRADO")
                exit()

            tecla = input('[S]air / ENTER para continuar : ').upper()
            if tecla == '':    
                PROC.UnidadeControle.cicloExecucao(memRAM) 
            elif tecla == 'S':
                print("\nPROGRAMA ENCERRADO")
                exit()

    memRAM.escreveSAIDA(OUT)
    print("\nPROGRAMA ENCERRADO COM SUCESSO")

if __name__ == '__main__':

    arquivoInstrucoes = sys.argv[1]

    enderecoInicial = int(sys.argv[2])

    comando = sys.argv[3]
    if comando == '-d':
        main(enderecoInicial, arquivoInstrucoes, arquivoSAIDA, '-d')
    elif comando == '-p':
        main(enderecoInicial, arquivoInstrucoes, arquivoSAIDA, '-p')