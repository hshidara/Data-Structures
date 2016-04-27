#https://www.cs.auckland.ac.nz/courses/compsci105ssc/resources/ProblemSolvingwithAlgorithmsandDataStructures.pdf

print("------------Starting Stack Testing------------")

#Stack

from Stack import *

s = Stack()

#Operations				#Stack Contents			#Return Value
print(s.is_empty()) 	#[] 					True
s.push(4) 				#[4]
s.push('dog') 			#[4,'dog']
print(s.top())			#[4,'dog'] 				'dog'
print(s.push(True)) 	#[4,'dog',True]	
print(s.size()) 		#[4,'dog',True] 		3
print(s.is_empty()) 	#[4,'dog',True] 		False
print(s.push(8.4)) 		#[4,'dog',True,8.4]
print(s.pop()) 			#[4,'dog',True] 		8.4
print(s.pop()) 			#[4,'dog'] 				True
print(s.size()) 		#[4,'dog'] 				2

print("------------Starting Queue Testing------------")

#Queue

from Queue import *

q = Queue()

#Operations 			#Queue Contents 		#Return Value
print(q.is_empty()) 	#[] 					True
q.enqueue(4) 			#[4]
q.enqueue('dog') 		#['dog',4]
q.enqueue(True) 		#[True,'dog',4]
print(q.size()) 		#[True,'dog',4] 		3
print(q.is_empty())		#[True,'dog',4] 		False
q.enqueue(8.4) 			#[8.4,True,'dog',4]
print(q.dequeue()) 		#[8.4,True,'dog'] 		4
print(q.dequeue()) 		#[8.4,True] 			'dog'
print(q.size())			#[8.4,True] 			2

print("------------Starting Linked List Testing------------")
print("------------Starting Node Testing------------")

#Node

from Node import *

n = Node("Hide")

print(n.get_data())

print("------------Unordered Linked List Testing------------")

#Linked List

from LinkedList import *

ll = UnorderedList()
print(ll.is_empty())
ll.add("Hide")
ll.add("is")
ll.add("a")
ll.add("computer")
ll.add("scientist")

print(ll.is_empty())
print(ll.search("Hidekazu"))
print(ll.search("Hide"))
ll.remove("Hide")
ll.print_list()
ll.add("Hide")
ll.print_list()
ll.reverse()
ll.print_list()
ll.append("NewNode")
ll.print_list()
print(ll.index("3"))
ll.pop()
ll.print_list()
ll._pop(2)
ll.print_list()



