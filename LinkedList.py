from __future__ import print_function #fixed print("blah", end="") error

from Node import Node

class UnorderedList:

	def __init__(self):
		self.head = None
		self.length = 0
		# self.current = Node()
		return

	def add(self,item):
		newNode = Node(item)
		newNode.set_next(self.head)
		self.head = newNode
		self.length += 1
		return

	def remove(self,item):
		current = self.head
		previous = None
		while(current != None):
			if(current.get_data() == item):
				previous.set_next(current.get_next())
				current = None
				return
			#iteration step
			previous = current
			current = current.get_next()

		self.length -= 1
		return

	def search(self,item):
		current = self.head
		while(current != None):
			if(current.get_data() == item):
				return True
			current = current.get_next()
		return False

	def is_empty(self):
		return self.head == None

	def size(self):
		return self.length

	def print_list(self):
		current = self.head
		while(current != None):
			print(current.get_data(), end = "")
			if(current.get_next() != None):
				print(" --> ", end = "")
			current = current.get_next()
		print()
		return

	def reverse(self):
		prev = None
		next = None
		current = self.head

		while(current != None):
			next = current.get_next()
			current.next = prev
			prev = current
			current = next
		self.head = prev
		return

	def append(self, item):
		current = self.head
		prev = None
		while(current != None):
			prev = current
			current = current.get_next()
		prev.next = Node(item)
		self.length += 1
		return	

	#	Returns 0 if item isn't in the list
	def index(self, item):
		current = self.head
		index = 0
		while(current != None):
			if(current.get_data() == item):
				return index
			index += 1
			current = current.get_next()
		print("Item not found: ", end = "")
		return 		

	def pop(self):
		current = self.head
		self.head = current.get_next()
		return

	def _pop(self, position):
		current = self.head
		prev = None
		for i in range(0,position):
			prev = current
			current = current.get_next()
		prev.next = current.get_next()
		return






