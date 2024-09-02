import sys
# define o número de palavras que cabem na memória RAM
# e o tamanho de cada segmento da RAM

RAM_TAMANHO = 500
segmentoDados = 100
segmentoInstrucoes = RAM_TAMANHO - segmentoDados
assert segmentoDados < RAM_TAMANHO/2
# cria a memória RAM vazia
RAM = [0]*RAM_TAMANHO

# =======================================================
def hex_to_int(hex : str):
    """
    Recebe um valor hexadecimal *hex* em formato de string e retorna seu valor convertido para inteiro
    """
    # limpamos os caracteres '0x' caso existam
    limpo = hex.replace('0x', '')
    # agora percorremos todos os caracteres do número fazendo a conversão
    numChar = len(limpo)
    expMax = numChar - 1
    
    num = 0
    for i in range(numChar):
        base = 1 << 4*(expMax - i)
        char = limpo[i]

        match char:
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
    
    return num

def processaLinha(linha : str) -> list[str]:
    # recuperamos os valores de cada campo
    valores = linha.split(sep='|')
    # retiramos o \n

def escreveRAM(ARQ, RAM : list[int], inicio : int):
    # lendo o valores
    for i in range(inicio):
        linha = ARQ.readline()
        linhaProcessada = processaLinha(linha)

# =======================================================

def main():
    global RAM

    arquivoInstrucoes = sys.argv[1]
    enderecoInicioCodigo = hex_to_int(sys.argv[2])
    # abrigmos o arquivo passado como parâmetro
    ENTRADA = open(arquivoInstrucoes, 'r')
    # escrevemos o conteudo do arquivo na RAM
    escreveRAM(ENTRADA, RAM, enderecoInicioCodigo)

    ENTRADA = open('MVP_instrucoes.txt', 'r')
    for i in range(codigoInicio-2):
        linha = ENTRADA.readline()
        partes = linha.split(sep='|')
        partes[0] = partes[0].replace('0x', '')
        partes[1] = int(partes[1].replace('\n', ''))
        print(linha)
        print(partes)

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


