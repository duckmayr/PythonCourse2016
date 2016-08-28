class LinkedList(object):
	def __init__(self, value):
		self.start = Node(value)
		self.nodes = 1
		
	def __str__(self): # This is complexity class n. For this, and all later reported complexity classes, I am considering worst-case complexity. I have not found a way to make any of these functions a lower complexity class.
		if self.hasCycle(): return 'This list is cyclical.'
		node = self.start
		result = '['+str(node)
		while node.next:
			result += (', '+str(node.next))
			node = node.next
		return result + ']'		
		
	def __repr__(self):
		return self.__str__()
		
	def length(self):
		return self.nodes		
		
	def findNode(self, value, check = 'start'): # This is complexity class n. 
		if not check: return 'There is no such node'
		if type(value) != int: return 'Please provide an integer value'
		if check == 'start': check = self.start
		if value == check.value: return check
		return self.findNode(value, check.next)	 
			
	def addNode(self, new_value): # This is complexity class n.
		if type(new_value) != int: return 'Please provide an integer value'
		tmp = self.start
		while tmp.next: tmp = tmp.next
		tmp.next = Node(new_value)
		self.nodes += 1
		return self		
		
	def addNodeAfter(self, new_value, after_node): # This is complexity class n.
		if type(new_value) != int: return 'Please provide an integer value'
		if type(after_node) != Node: after_node = self.findNode(after_node)
		if type(after_node) != Node: return 'There is no such after_node'	
		after_node.next = Node(new_value, after_node.next)
		self.nodes += 1
		return self		
		
	def findNodeBefore(self, after_node, newBefore = 'start'): # This is complexity class n.
		if newBefore == 'start': newBefore = self.start
		if newBefore.next == after_node: return newBefore
		return self.findNodeBefore(after_node, newBefore.next)	
		
	def addNodeBefore(self, new_value, before_node): # This is complexity class n.
		if type(new_value) != int: return 'Please provide an integer value'
		if type(before_node) != Node: before_node = self.findNode(before_node)
		if type(before_node) != Node: return 'There is no such before_node'
		if before_node == self.start: self.start = Node(new_value, self.start)
		else:
			newBefore = self.findNodeBefore(before_node)
			newBefore.next = Node(new_value, before_node)
		self.nodes += 1
		return self		
		
	def removeNode(self, node_to_remove): # This is complexity class n.
		if type(node_to_remove) != Node: node_to_remove = self.findNode(node_to_remove)
		if type(node_to_remove) != Node: return 'There is no such node_to_remove'
		if node_to_remove == self.start: self.start = self.start.next
		else:
			newBefore = self.findNodeBefore(node_to_remove)
			newBefore.next = node_to_remove.next
		self.nodes -= 1
		return self	
		
	def removeNodesByValue(self, value): # This is complexity class n^2.
		if type(value) != int: return 'Please provide an integer value'
		self.removeNode(self.findNode(value))
		if self.findNode(value) == 'There is no such node': return self
		return self.removeNodesByValue(value)
		
	def reverse(self): # This is complexity class n.
		tmp = self.start
		while tmp.next: tmp = tmp.next
		first = tmp
		while tmp != self.start:
			tmp.next = self.findNodeBefore(tmp)
			tmp = tmp.next
		self.start.next = None
		self.start = first
		return self
		
	def hasCycle(self): # This is complexity class n.
		counter = 1
		tmp = self.start
		while tmp.next:
			counter += 1
			if counter > self.length(): return True
			tmp = tmp.next
		return False
		
class Node(LinkedList):
	def __init__(self, _value = None, _next = None):
		self.value = _value
		self.next = _next
		
	def __str__(self):
		return str(self.value)
		
	def __repr__(self):
		return self.__str__()