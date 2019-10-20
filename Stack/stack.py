
class Stack(object):
	MAX = 10
	"""docstring for Stack"""
	def __init__(self):
		self.data = [None] * self.MAX
		self.top = -1

	def push(self, data):
		if self.top == (self.MAX-1):
			print("Stack is full!\n")
			return
		self.top += 1
		self.data[self.top] = data

	def pop(self):
		if self.top == -1:
			print("Stack is empty!")
			return
		data = self.data[self.top]
		self.top -= 1
		return data

	def display(self):
		data = self.data
		print("\nDisplay Nodes: ")
		top = self.top
		while top > -1:
			print(self.data[top])
			top -= 1


if __name__ == '__main__':
	s = Stack()
	s.push(11)
	s.push(23)
	s.push(-8)
	s.push(16)
	s.push(27)
	s.push(14)
	s.push(20)
	s.push(39)
	s.push(2)
	s.push(15)
	s.push(7)
	s.display()
	i = s.pop()
	if i:
		print("Item popped: {}".format(i))
	i = s.pop()
	if i:
		print("Item popped: {}".format(i))
	i = s.pop()
	if i:
		print("Item popped: {}".format(i))
	i = s.pop()
	if i:
		print("Item popped: {}".format(i))
	i = s.pop()
	if i:
		print("Item popped: {}".format(i))





