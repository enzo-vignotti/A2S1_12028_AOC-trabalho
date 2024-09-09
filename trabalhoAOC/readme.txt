Como rodar o programa

1) Certifique-se de que o arquivo de código python e os arquivos .txt com as instruções estão na mesma pasta;
2) Abra a pasta com os arquivos pelo VSCode;
3) Abra o terminal do VSCode
4) Execute o arquivo python por linha de comando. O comando deve ser da seguinte forma:

        	python arquivoCodigo.py arquivoInstrucoes.txt inicioDoCodigo flag

	# A posição "inicioDoCodigo" recebe o endereço da primeira linha do algoritmo descrito no arquivo de 
		instruções: no caso do selection sort, a linha é 20; no caso do termo geral de uma PG, a linha é 15.
	# A "flag" pode ser “-d”, caso queira que o algoritmo seja executado do começo ao fim sem 
		pausas, ou “-p”, caso queira controlar o ritmo de execução do algoritmo manualmente.
	
5) Ao encerrar, o programa emite uma mensagem de programa encerrado e o resultado do processamento poderá 
	ser verificado no arquivo "log_out.txt", que será criado na mesma pasta dos demais arquivos.