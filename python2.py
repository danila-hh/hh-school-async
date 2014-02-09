def func1(*args):
	print(args[0])

def func2(*args):
	print(args[0])

def func3(*args):
	print(args[0])

class AsyncGroup:
	funcList = []

	def __init__(self):
		pass

	def add(self, func):
		def decaratedFunc(*args):
			try:
				func(*args)		
			except Exception as e:
				self.error_callback(self, e)
			finally: 
				self.funcList.remove(func);	
				if len(self.funcList) == 0:
					self.final_callback();						
		self.funcList.append(func);
		return decaratedFunc;

	def final_callback(self):
	    print("that is all")    

	def error_callback(self, e):
		print(e)

group = AsyncGroup()

func1 = group.add(func1)
func2 = group.add(func2)
func3 = group.add(func3)


func1(1)
func2(3)
func3(4)

# now final_callback should be executed