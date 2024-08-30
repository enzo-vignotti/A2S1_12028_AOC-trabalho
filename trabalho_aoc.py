import sys
# REGISTRADORES SOLICITADOS
# PC
# MAR
# MBR
# IR
# AC
# M(Q)
# R
# C
# Z

# CONJUNTO DE INSTRUÇÕES DO IAS

# Data transfer
# LOAD MQ       | AC <- MQ
# LOAD MQ,M(X)  | MQ <- mem(X)
# STOR M(X)     | mem(X) <- AC
# LOAD M(X)     | AC <- mem(X)
# LOAD -M(X)    | AC <- -mem(X)
# LOAD |M(X)|   | AC <- |mem(x)|
# LOAD -|M(X)|  | AC <- -|mem(X)|

# Unconditional branch 
# JUMP M(X,0:19)  | Salta para o local de M(X) e recupera sua instrução esquerda
# JUMP M(X,20:39) | Salta para o local de M(X) e recupera sua instrução direita

# Conditional branch
# JUMP+ M(X,0:19)  | Se AC <= 0, JUMP M(X,0:19)
# JUMP+ M(X,20:39) | Se AC <= 0, JUMP M(X,20:39)

# Arithmetic
# ADD M(X)   | AC <- AC + mem(X)
# ADD |M(X)| | AC <- AC + |mem(X)|
# SUB M(X)   | AC <- AC - mem(X)
# SUB |M(X)| | AC <- AC - |mem(X)|
# MUL M(X)   | multiplica mem(X) por MQ, coloca o bits mais significativos em AC e os menos em MQ
# DIV M(X)   | divide AC por mem(X), coloca o quociente no MQ e o resto no AC
# LSH        | AC * 2
# RSH        | AC / 2

# Adress modify
# STOR M(X,8:19)  | Substitui o endereço esquerdo de M(X) pelos 12 bits mais à direita de AC
# STOR M(X,28:39) | Substitui o endereço direito de M(X) pelos 12 bits mais à direita de AC

# MEMÓRIA RAM
# Palavras de 40 bits (5 bytes)


# variáveis
PC = 0
MAR = 0
MBR = 0
IR = 0
AC = 0
MQ = 0
R = 0
C = 0
Z = 0

class RAM():
    """
    Classe que implmenta a memória RAM de um computador
    """
    def __init__(self):
        self.stack = []
        self.heap = []

RAM = []

def leMemoria(RAM, endereco : int):
    RAM.seek(endereco * 40)


class UnidadeControle():
    def subCicloBusca(self):
        MAR = PC
        MBR = leMemoria(MAR)
        PC = PC + I
        IR = MBR


def LOAD_MQ():
    AC = MQ

def LOAD_MQ_MX(endereco):
    MQ = RAM[endereco]

def STOR_MX(endereco):
    RAM[endereco] = AC

def LOAD_MX(endereco):
    AC = RAM[endereco]

# LOAD -M(X)    | AC <- -mem(X)
# LOAD |M(X)|   | AC <- |mem(x)|
# LOAD -|M(X)|  | AC <- -|mem(X)|

def main():
    arquivoInstrucoes = sys.argv[1]
    enderecoInicioCodigo = sys.argv[2]

    # abrimos o arquivo de instruções para leitura
    ENTRADA = open(arquivoInstrucoes, 'rb')
    