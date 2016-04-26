class Stack:

	def __init__(self):
		self.data = []

	def push(self,item):
		self.data.append(item)

	def pop(self):
		return self.data.pop()

	def top(self):
		return self.data[len(self.data) - 1]

	def is_empty(self):
		return self.data == []

	def size(self):
		return len(self.data)


