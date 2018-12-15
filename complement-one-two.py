import os

def complemento_1(num):	
	for i in range(len(num)):
		num[i] = "1" if num[i] == "0" else "0"
	
	return "".join(num)

def complemento_2(num):
	num = list(complemento_1(num))
	for i in range(len(num)-1,-1,-1):
		if num[i] == "1":
			num[i] = "0"
		else:
			num[i] = "1"
			break
	if i == -1:
		num += "1"
	
	return "".join(num)

op = "n"
while op != "s":	
	entrada = list(input("Digite um número binário:"))
	num = entrada[:]
	print('complemento 1:',complemento_1(num))
	num = entrada[:]
	print('complemento 2:',complemento_2(num))
	op = input("Deseja sair? (s ou n):")
	os.system("clear")
