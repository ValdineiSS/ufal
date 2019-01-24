import random

def shell_sort(lista):
	h = 1
	while h<len(lista):
		if 3*h+1 < len(lista):
			h = 3*h+1
		else:
			break
	while h!=0:
		print('h: ',h)
		for i in range(h,len(lista)):
			aux = lista[i]
			j = i
			while lista[j-h]>aux:
				lista[j] = lista[j-h] #trocar
				j-=h
				if j<h: #Não dá pra pular
					break
			lista[j] = aux #trocar
		h = h//3
	return lista	

lista = []
for i in range(50):
	lista.append(random.randint(0, 100))
print(lista)
print(shell_sort(lista))