#algoritmo de busca binária
#procura valor v, olha no meio, se encontrar termina, se não verifica se está abaixo ou acima

def buscaBinaria(valor, lista):

	meio = len(lista)//2

	if valor == lista[meio]:
		return True 
	elif(len(lista) == 1):
		return False
	elif (valor < lista[meio]):
		return buscaBinaria(valor, lista[:meio])
	else:
		return buscaBinaria(valor, lista[meio+1:])

def main():
	valor = 190
	lista = [3,5,10,11,13,14,15,16,16,17,22,190,345,1234,346436,544365436,99999999999]
	print(buscaBinaria(valor, lista))

main()