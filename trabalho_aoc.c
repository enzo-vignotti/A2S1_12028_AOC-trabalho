#include <stdio.h>

/*
REGISTRADORES DO IAS

PC  - 12bits - Armazena o endereço da próxima instrução
AC  - 40bits - Armazenamento temporário de dados
MQ  - 40bits - Armazenamento temporário de dados
IR  - 8 bits - Armazena o opcode de uma instrução
MBR - 40bits - Dados de leitura e escrita de memória
IBR - 20bits - Armazena instrução direita (20-39bits)
MAR - 12bits - Armazena um endereço de memória de uma instrução
 */

// estrutura que armazena uma frase de 40 bits do IAS

struct frase{
        unsigned int instrucaoDireita : 12;
        unsigned int opcodeDireito : 8;
        unsigned int instrucaoEsquerda : 12;
        unsigned int opcodeEsquerdo : 8;
}frase;


