def selection_sort(lista):
	for i in range(len(lista)-1):
		menor = i
		for j in range(i+1, len(lista)):
			if lista[j] < lista[menor]:
				menor = j 
		lista[i], lista[menor] = lista[menor], lista[i]
	return lista


print(selection_sort([99,60,39,11,10,3,2,1]))