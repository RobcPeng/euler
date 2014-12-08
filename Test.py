g = lambda x: x**2
print(g(2))

class Node(object):
	def __init__(self, cargo = None, next = None):
		self.cargo = cargo
		self.next = next
		

	def __str__(self):
		return str(self.cargo)

class LinkedList(object):
	def __init__(self, head = None):
		self.head=head

	def add(self, cargo):
		node = Node(cargo)
		if not self.head:
			self.head = node
		else:
			node.next = self.head
			self.head = node



