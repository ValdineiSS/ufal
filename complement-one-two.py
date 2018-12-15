def complemento_1(numero):	
	for i in range(len(numero)):
		numero[i] = "1" if numero[i] == "0" else "0"
	
	return "".join(numero)

def complemento_2(numero):
	c1 = list(complemento_1(numero))
	for i in range(len(numero)-1,0,-1):
		if c1[i] == "1":
			c1[i] = "0"
		else:
			c1[i] = "1"
			break
	if i == -1:
		c1 += "1"
	
	return "".join(c1)

	
		
numero = []
entrada = []
entrada = list(input("Digite um número binário:"))
numero = entrada[:]
print('complemento 1:',complemento_1(numero))
numero = entrada[:]
print('complemento 2:',complemento_2(numero))
