#estrutura de dados pilha
#operações:
# - empilhar, desempilhar, verificar se está vazia, verificar se está cheia
class Pilha:
	items = [None]
	topo = None
	tam = None

	def __init__(self, tam):
		self.items = [None]*tam 
		self.tam = tam 
		self.topo = 0

	def estaVazia(self):
		return True if self.topo == 0 else False 

	def estaCheia(self):
		return True if self.topo == self.tam else False

	def empilhar(self, item):
		if not self.estaCheia():
			self.items[self.topo] = item 
			self.topo += 1
			return True 
		else:
			return False

	def desempilhar(self):
		if not self.estaVazia():
			self.topo -= 1
			self.items[self.topo] = None
			return True
		else:
			return False 

	def imprimir(self):
		print('items da pilha:')
		for item in reversed(self.items):
			if item != None:
				print(item)


def main():
	p = Pilha(10)

	print('está vazia',p.estaVazia())
	print('está cheia',p.estaCheia())
	print('empilhar',p.empilhar(13))
	print('empilhar',p.empilhar(15))
	print('empilhar',p.empilhar(167))
	print('empilhar',p.empilhar(1))
	print('empilhar',p.empilhar(5))
	#print('desempilhar',p.desempilhar())
	p.imprimir()


main()
